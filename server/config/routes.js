var documents = require("./../controllers/documents.js")

module.exports = function(app){
	app.get("/words", documents.index) // No apostrophes after lines
}