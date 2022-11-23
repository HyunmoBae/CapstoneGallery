import { Schema, model } from "mongoose"

const PartySchema = new Schema ({
	user: {
		type: String,
		required: true,
	},
	title: {
		type: String,
		required: true,
	},
	photo: {
		type: String,
		default: "",
	},
	content: {
		type: String,
		default: "",
	},
	like: {
		type: Number,
		default: 0,
	},
	hit: {
		type: Number,
		default: 0,
	},
}, { timestamps: true })

const Party = model("partys", PartySchema)

export { Party }