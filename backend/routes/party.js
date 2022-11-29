import { Router } from "express"
import { connect } from "mongoose"
import { Party } from "../model/party.js"
import { MONGO_URL } from "../setting.js";

const partyRouter = Router()

// 글 쓰기
partyRouter.post("/write", async (req, res) => {
	const newParty = new Party(req.body)
	try {
    await connect(MONGO_URL);

		const saveParty = await newParty.save()
		res.status(200).json(saveParty)
	} catch (err) {
		res.status(500).json(err)
	}
})
// 글 수정
partyRouter.put("/write/:id", async (req, res) => {
	if(req.params.id === req.body._id) {
		try {
			await connect(MONGO_URL);
	
			const findParty = await Party.findById(req.params.id)
			if(!findParty) {
				res.status(404).json("party Not Found")
			} else if (findParty.user !== req.body.user) {
					res.status(401).json("Not Your party")
			} else {
				const updateParty = await Party.findByIdAndUpdate(req.params.id, {
					$set: req.body
				}, { new: true })
				res.status(200).json(updateParty)
			}
		} catch (err) {
			res.status(500).json(err)
		}
	} else {
		res.status(400).json("url error")
	}
})
// 글 삭제
partyRouter.delete("/delete/:id", async (req, res) => {
	if(req.params.id !== req.body._id) {
		res.status(400).json("url error")
	} else {
		try {
			await connect(MONGO_URL);
			
			const findParty = await Party.findById(req.params.id)
			if(!findParty) {
				res.status(404).json("party Not Found")
			} else if (findParty.user !== req.body.user) {
				res.status(401).json("Not Your party")
			} else {
				await Party.findByIdAndDelete(req.params.id)
				res.status(200).json("Delete Your party")
			}
		} catch (err) {
			res.status(500).json(err)
		}
	}
})
// 글 하나
partyRouter.get("/detail/:id", async (req, res) => {
	try {
    await connect(MONGO_URL);

		const findParty = await Party.findById(req.params.id)
		res.status(200).json(findParty)
	} catch (err) {
		res.status(500).json(err)
	}
})
// 글 전체
partyRouter.get("/list", async (req, res) => {
	try {
    await connect(MONGO_URL);

		const partyList = await Party.find()
		partyList.reverse()
		res.status(200).json(partyList)
	} catch (err) {
		res.status(500).json(err)
	}
})

export { partyRouter }