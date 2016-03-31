var words = require("./../controllers/words.js")

module.exports = function(app){
	app.get("/words", words.index) // No apostrophes after lines
	app.get("/words/pick_words", words.pick_words)
}