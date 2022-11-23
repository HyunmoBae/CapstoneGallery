import { Schema, model } from "mongoose";

const BoardSchema = new Schema(
  {
    user: {
      type: String,
      required: true,
    },
    title: {
      type: String,
      require: true,
    },
    photo: {
      type: String,
    },
    content: {
      type: String,
    },
    like: {
      type: Number,
      default: 0,
    },
    hit: {
      type: Number,
      default: 0,
    },
  },
  { timestamps: true }
);

const Board = model("boards", BoardSchema);

export { Board };
