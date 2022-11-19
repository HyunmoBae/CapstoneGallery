import { Router } from "express";
import { connect } from "mongoose";
import { Gallery } from "../model/gallery.js";
import { MONGO_URL } from "../setting.js";

const galleryRouter = Router();

//글 쓰기
galleryRouter.post("/write", async (req, res) => {
  const newGallery = new Gallery(req.body);
  try {
    await connect(MONGO_URL);
    const saveGallery = await newGallery.save();
    res.status(200).json(saveGallery);
  } catch (error) {
    res.status(500).json("error");
  }
});

//글 수정
galleryRouter.put("/write/:id", async (req, res) => {
  if (req.body._id == req.params.id) {
    try {
      await connect(MONGO_URL);
      const updategallery = await Gallery.findByIdAndUpdate(
        req.params.id,
        { $set: req.body },
        { new: true }
      );
      res.status(200).json(updategallery);
    } catch (error) {
      res.status(500).json("error");
    }
  } else {
    res.status(400).json("url error");
  }
});

//글 삭제
galleryRouter.delete("/delete/:id", async (req, res) => {
  if (req.body._id == req.params.id) {
    try {
      await connect(MONGO_URL);
      const deleteGallery = await Gallery.findById({ _id: req.params.id });
      if (!deleteGallery) {
        res.status(404).json("Not Found");
      } else {
        await Gallery.findByIdAndDelete({ _id: req.params.id });
        res.status(200).json(deleteGallery);
      }
    } catch (error) {
      res.status(500).json("error");
    }
  } else {
    res.status(400).json("url error");
  }
});

//글 상세
galleryRouter.get("/detail/:id", async (req, res) => {
  try {
    await connect(MONGO_URL);
    const gallerydetail = await Gallery.findOne({ _id: req.params.id });
    if (!gallerydetail) {
      res.status(404).json("NotFound");
    } else {
      res.status(200).json(gallerydetail);
    }
  } catch (error) {
    res.status(500).json("error");
  }
});

//글 전체
galleryRouter.get("/list", async (req, res) => {
  try {
    await connect(MONGO_URL);
    const gallerylist = await Gallery.find();
    gallerylist.reverse();
    res.status(200).json(gallerylist);
  } catch (error) {
    res.status(500).json("error");
  }
});

export { galleryRouter };
