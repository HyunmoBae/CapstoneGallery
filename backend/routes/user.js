import { Router } from "express";
import { connect } from "mongoose";
import { User } from "../model/user.js";
import { MONGO_URL } from "../setting.js";
import { genSalt, hash } from "bcrypt";
import { Gallery } from "../model/gallery.js";

const userRouter = Router();

userRouter.put("/edit/:id", async (req, res) => {
  if (req.body._id === req.params.id) {
    if (req.body.password) {
      const salt = await genSalt(10);
      req.body.password = await hash(req.body.password, salt);
    }
    try {
      await connect(MONGO_URL);
      const updateUser = await User.findByIdAndUpdate(
        req.params.id,
        { $set: req.body },
        { new: true }
      );
      res.status(200).json(updateUser);
    } catch (error) {
      res.status(500).json(error);
      console.log(error);
    }
  } else {
    res.status(401).json("Not your account");
  }
});

userRouter.get("/detail/:id", async (req, res) => {
  try {
    await connect(MONGO_URL);
    const findUser = await User.findById({ _id: req.params.id });
    if (!findUser) {
      res.status(404).json("User not found");
    } else {
      res.status(200).json(findUser);
    }
  } catch (error) {
    res.status(500).json(error);
  }
});

userRouter.delete("/delete/:id", async (req, res) => {
  if (req.body._id === req.params.id) {
    try {
      await connect(MONGO_URL);
      const deleteUser = await User.findById({ _id: req.params.id });
      if (!deleteUser) {
        res.status(404).json("Not Found");
      } else {
        await User.findByIdAndDelete({ _id: req.params.id });
        await Gallery.findByIdAndDelete({ user: req.params.id });
        res.status(200).json(deleteUser);
      }
    } catch (error) {
      res.status(500).json(error);
    }
  } else {
    res.status(401).json("Not your account");
  }
});

export { userRouter };
