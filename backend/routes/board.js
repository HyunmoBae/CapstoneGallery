import { Router } from "express";
import { connect } from "mongoose";
import { Board } from "../model/board";
import { MONGO_URL } from "../setting";

const boardRouter = Router();

boardRouter.post;

//생성
boardRouter.post("/write", async (req, res) => {
  const newBoard = new Board(req.body);
  try {
    await connect(MONGO_URL);
    const saveboard = await newBoard.save();
    res.status(200).json(saveboard);
  } catch (error) {
    res.status(500).json("error");
  }
});

//수정
boardRouter.put("/write/:id", async (req, res) => {
  if (req.body._id == req.params.id) {
    try {
      await connect(MONGO_URL);
      const updateboard = await Board.findByIdAndUpdate(
        req.params.id,
        {
          $set: req.body,
        },
        { new: true }
      );
      res.status(200).json(updateboard);
    } catch (error) {
      res.status(500).json("error");
    }
    res.status(400).json("url error");
  }
});

//삭제

//상세보기
boardRouter.get("detail/:id", async (req, res) => {
  try {
    await connect(MONGO_URL);
    const gallerydetail = await Board.findOne({ _id: req.params.id });
    if (!gallerydetail) {
      res.status(404).json("Not Found");
    } else {
      res.status(200).json(gallerydetail);
    }
  } catch (error) {
    res.status(500).json("error");
  }
});

//글전체

export { boardRouter };
