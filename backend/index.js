import express from "express";
import { authRouter } from "./routes/auth.js";
import { galleryRouter } from "./routes/gallery.js";
import { userRouter } from "./routes/user.js";

const app = express();
app.use(express.json());

app.use("/api/auth", authRouter);
app.use("/api/user", userRouter);
app.use("/api/gallery", galleryRouter);

app.listen(5000, () => {
  console.log("backend is running");
});

// app.listen(5000, function(req, res) {
//   console.log("아무거나")
// })
