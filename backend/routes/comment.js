import { Router } from "express";
import { connect } from "mongoose";
import { Comment } from "../model/comment.js";
import { MONGO_URL } from "../setting.js";

const commentRouter = Router();

// 댓글 쓰기
commentRouter.post("/write", async (req, res) => {
  let newComment = new Comment(req.body);
  try {
    await connect(MONGO_URL);
    const savecomment = await newComment.save();
    res.status(200).json(savecomment);
  } catch (error) {
    res.status(500).json("error");
  }
});

// 댓글 수정
commentRouter.put("/edit/:id", async (req, res) => {
  if (req.body._id !== req.params.id) {
    res.status(400).json("URL Error");
  } else {
    try {
      await connect(MONGO_URL);
      const findComment = await Comment.findById(req.params.id);
      if (!findComment) {
        res.status(404).json("Comment Not Found");
      } else if (findComment.user !== req.body.user) {
        res.status(401).json("Not your Comment");
      } else {
        const updateComment = await Comment.findByIdAndUpdate(
          req.params.id,
          { $set: req.body },
          { new: true }
        );
        res.status(200).json(updateComment);
      }
    } catch (err) {
      res.status(500).json(err);
    }
  }
});

// 댓글 삭제
commentRouter.delete("/delete/:id", async (req, res) => {
  // 고아 댓글 있으면 안 되기 때문에
  // isDeleted = false 할 예정
  if (req.params.id !== req.body._id) {
    res.status(400).json("URL Error");
  } else {
    try {
      await connect(MONGO_URL);

      const findComment = await Comment.findById(req.params.id);
      if (!findComment) {
        res.status(404).json("Comment Not Found");
      } else if (findComment.user !== req.body.user) {
        res.status(401).json("Not your Comment");
      } else {
        const updateComment = await Comment.findByIdAndUpdate(
          req.params.id,
          { $set: { isDeleted: true } },
          { new: true }
        );
        res.status(200).json(updateComment);
      }
    } catch (err) {
      res.status(500).json(err);
    }
  }
});

// 댓글 전체 불러오기
commentRouter.get("/list", async (req, res) => {
  try {
    await connect(MONGO_URL);
    const commentList = await Comment.find({ isDeleted: false });
    res.status(200).json(commentList);
  } catch (err) {
    res.status(500).json(err);
  }
});

export { commentRouter };

/**
 * https://velog.io/@ehgks0000/%EB%8C%93%EA%B8%80-%EB%8C%80%EB%8C%93%EA%B8%80
 */
