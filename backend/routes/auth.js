import { Router } from "express";
import { connect } from "mongoose";
import { User } from "../model/user.js";
import { MONGO_URL } from "../setting.js";
import { genSalt, hash, compare } from "bcrypt";

const authRouter = Router();
// const User = mongoose.model("user", UserSchema);

authRouter.post("/register", async (req, res) => {
  try {
    await connect(MONGO_URL);
    const salt = await genSalt(10);
    const hashPassword = await hash(req.body.password, salt);
    const newUser = new User({
      id: req.body.id,
      password: hashPassword,
      email: req.body.email,
      major: req.body.major,
      tel: req.body.tel,
      //      password: hashPassword,
    });
    const user = await newUser.save();
    res.status(200).json(user);
  } catch (error) {
    res.status(500).json(error);
    console.log(error);
  }
});

authRouter.post("/login", async (req, res) => {
  try {
    await connect(MONGO_URL);
    const user = await User.findOne({ id: req.body.id });
    if (!user) {
      res.status(404).json("not found");
    } else {
      const vaildated = await compare(req.body.password, user.password);

      if (!vaildated) {
        res.status(400).json("wrong password");
      } else {
        res.status(200).json("login success");
      }
    }
  } catch (error) {
    res.status(500).json(err);
    console.log(error);
  }
});

export { authRouter };
