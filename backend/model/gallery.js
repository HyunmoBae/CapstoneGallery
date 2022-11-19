import { Schema, model } from "mongoose";

const GallerySchema = new Schema(
  {
    user: {
      type: String,
      required: true,
      unique: true,
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

const Gallery = model("gallerys", GallerySchema);

export { Gallery };
