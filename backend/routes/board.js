import { Router } from "express";
import { connect, deleteModel } from "mongoose";
import { Board } from "../model/board.js";
import { MONGO_URL } from "../setting.js";

const boardRouter = Router();

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
        { $set: req.body },
        { new: true }
      );
      res.status(200).json(updateboard);
    } catch (error) {
      res.status(500).json("error");
    }
  } else {
    res.status(400).json("url error");
  }
});

//삭제
boardRouter.delete("/delete/:id", async (req, res) => {
  if (req.body._id == req.params.id) {
    try {
      await connect(MONGO_URL);
      const deleteboard = await Board.findById(req.params.id);
      if (!deleteboard) {
        res.status(400).json("Not Found");
      } else {
        await Board.findByIdAndDelete({ _id: req.params.id });
        res.status(200).json(deleteboard);
      }
    } catch (error) {
      res.status(500).json("error");
    }
  } else {
    res.status(404).json("url error");
  }
});

//상세보기
boardRouter.get("detail/:id", async (req, res) => {
  try {
    await connect(MONGO_URL);
    const boarddetail = await Board.findOne({ _id: req.params.id });
    if (!boarddetail) {
      res.status(404).json("Not Found");
    } else {
      res.status(200).json(boarddetail);
    }
  } catch (error) {
    res.status(500).json("error");
  }
});

//글전체
boardRouter.get("/list", async (req, res) => {
  try {
    await connect(MONGO_URL);
    const boardlist = await Board.find();
    boardlist.reverse();
    res.status(200).json(boardlist);
  } catch (error) {
    res.status(500).json("error!");
  }
});

export { boardRouter };
