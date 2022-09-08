var router = require("express").Router();

const { Db } = require("mongodb");
let multer = require("multer");

var storage = multer.diskStorage({
  //하드디스크에 저장
  destination: function (req, file, cb) {
    cb(null, "./public/image");
  },
  filename: function (req, file, cb) {
    cb(null, Date.now() + "-" + file.originalname);
  },
});
var upload = multer({ storage: storage });

router.get("/", function (req, res) {
  //sort 정렬 -1: 내림차순 / 1: 오름차순
  db.collection("photo")
    .find()
    .sort({ _id: -1 })
    .toArray(function (err, result) {
      res.render("gallery/list.ejs", { row: result });
    });
});

router.get("/write", function (req, res) {
  res.render("gallery/write.ejs");
});

router.get("/list", function (req, res) {
  //sort 정렬 -1: 내림차순 / 1: 오름차순
  db.collection("photo")
    .find()
    .sort({ _id: -1 })
    .toArray(function (err, result) {
      res.render("gallery/list.ejs", { row: result });
    });
});

router.post("/ok", upload.single("file"), function (req, res) {
  db.collection("photo_counter").findOne(
    {
      name: "PCounter",
    },
    function (err, result) {
      var g_counter = result.totalRecord;
      var now = new Date();
      db.collection("photo").insertOne(
        {
          wdate: now.toLocaleString(),
          _id: g_counter + 1,
          title: req.body.title,
          name: req.body.name,
          file: req.file.filename,
        },
        function () {
          db.collection("photo_counter").updateOne(
            { name: "PCounter" },
            { $inc: { totalRecord: 1 } },
            function () {
              res.redirect("/gallery/list");
            }
          );
        }
      );
    }
  );
});

//ajax를 이용한 삭제
router.delete("/del", function (req, res) {
  req.body._id = parseInt(req.body._id);
  db.collection("photo").deleteOne(req.body, function (err, result) {
    console.log("삭제 완료");
  });
});

module.exports = router;
