var router = require("express").Router();

router.get("/", function (req, res) {
  db.collection("board")
    .find()
    .sort({ _id: -1 })
    .toArray(function (err, result) {
      res.render("board/list.ejs", { rows: result });
    });
});

router.get("/write", function (req, res) {
  res.render("board/write.ejs");
});

router.post("/ok", function (req, res) {
  db.collection("count").findOne({ name: "bCounter" }, function (err, result) {
    var totalPost = result.totalRecord;

    db.collection("board").insertOne(
      {
        _id: totalPost + 1,
        title: req.body.title,
        name: req.body.name,
        content: req.body.memo,
        wdate: req.body.wdate,
      },
      function (err, result) {
        db.collection("count").updateOne(
          { name: "bCounter" },
          { $inc: { totalRecord: 1 } },
          function () {
            {
              res.redirect("../board");
            }
          }
        );
        // console.log(req.body);
        // res.send("전송완료"); //반드시 존재햐아함.
      }
    );
  });
});

router.get("/list", function (req, res) {
  //sort 정렬 -1: 내림차순 / 1: 오름차순
  db.collection("board")
    .find()
    .sort({ _id: -1 })
    .toArray(function (err, result) {
      res.render("../board/list.ejs", { rows: result });
    });
});

router.get("/detail/:id", function (req, res) {
  db.collection("board").findOne(
    { _id: parseInt(req.params.id) },
    function (err, result) {
      res.render("board/detail.ejs", { rows: result });
    }
  );
});

router.get("/edit/:id", function (req, res) {
  db.collection("board").findOne(
    { _id: parseInt(req.params.id) },
    function (err, result) {
      res.render("board/edit.ejs", { rows: result });
    }
  );
});

router.put("/edit", function (req, res) {
  db.collection("board").updateOne(
    { _id: parseInt(req.body.id) },
    {
      $set: {
        title: req.body.title,
        name: req.body.name,
        content: req.body.content,
        wdate: req.body.wdate,
      },
    },
    function (err, result) {
      res.redirect("../board/");
    }
  );
});

router.get("/del/:id", function (req, res) {
  db.collection("board").deleteOne(
    { _id: parseInt(req.params.id) },
    function (err, result) {
      res.redirect("/board/");
    }
  );
});

router.get("/search", function (req, res) {
  db.collection("board")
    .find({
      title: RegExp(req.query.value), //RegExp : value값에 있는 값 포함해서 노출
    })
    .toArray(function (err, result) {
      res.render("board/search.ejs", { rows: result });
    });
});

module.exports = router;
