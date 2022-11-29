import { Router } from "express";
import multer, { diskStorage } from "multer";

const imageRouter = Router();

const storage = diskStorage({
  destination: (req, file, cb) => {
    cb(null, "images/");
  },
  filename: (req, file, cb) => {
    cb(null, Date.now() + file.originalname);
    //cb(null, req.body.filename);
  },
});

const upload = multer({ storage: storage });
imageRouter.post("/", upload.single("file"), (req, res) => {
  res.status(200).json("upload Success");
});

export { imageRouter };
