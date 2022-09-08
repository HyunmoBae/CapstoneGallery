const express = require("express");
const app = express();
const MongoClient = require("mongodb").MongoClient;
const methodOverride = require("method-override");

app.use(methodOverride("_method"));
app.use(express.urlencoded({ extended: true }));
app.set("view engine", "ejs");
app.use(express.static("public"));

MongoClient.connect(
  "mongodb+srv://admin:qwer1234@cluster0.zmhutc5.mongodb.net/?retryWrites=true&w=majority",
  function (err, client) {
    if (err) return console.log(err);
    db = client.db("nodeapp");
    app.listen(8888, function () {
      console.log("웹서버 실행중입니다.");
    });
  }
);

app.get("/", function (req, res) {
  res.render("../index.ejs");
});

app.use("/board", require("./routes/board.js"));
app.use("/gallery", require("./routes/gallery.js"));
