import express from "express";
import path from "path";
import { authRouter } from "./routes/auth.js";
import { boardRouter } from "./routes/board.js";
import { galleryRouter } from "./routes/gallery.js";
import { userRouter } from "./routes/user.js";
import { partyRouter } from "./routes/party.js";
import { imageRouter } from "./routes/image.js";

const app = express();
app.use(express.json());

const __dirname = path.resolve();
app.use("/images", express.static(path.join(__dirname, "/images")));

app.use("/api/auth", authRouter);
app.use("/api/user", userRouter);
app.use("/api/gallery", galleryRouter);
app.use("/api/board", boardRouter);
app.use("/api/party", partyRouter);
app.use("/api/image", imageRouter);

app.listen(5000, () => {
  console.log("backend is running");
});

// app.listen(5000, function(req, res) {
//   console.log("아무거나")
// })
