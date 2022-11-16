import { Schema, model } from "mongoose";

const UserSchema = new Schema(
  {
    id: {
      type: String,
      required: true,
      unique: true,
    },
    password: {
      type: String,
      required: true,
    },
    email: {
      type: String,
      required: true,
      unique: true,
    },
    major: {
      type: String,
    },
    tel: {
      type: String,
    },
  },
  { timestamps: true }
);

const User = model("users", UserSchema);

export { User };
