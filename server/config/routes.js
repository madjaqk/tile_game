var words = require("./../controllers/words.js")

module.exports = function(app){
	app.get("/words/pick_words", words.pick_words)
	app.post("/words/find_score", words.find_score)
}