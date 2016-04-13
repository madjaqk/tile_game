// Controller

// var mongoose = require("mongoose")
// var Document = mongoose.model("Document")
var words = require("./../../wordlists/10k_legal.json")
var scores = require("./../../wordlists/word_scores.json")

module.exports = (function(){
	return {
		pick_words: function(req, res){
			output = {}
			for(var i = 3; i <= 6; i++){
				var keys = Object.keys(words[i])
				return_word = keys[Math.floor(Math.random()*keys.length)]
				output[i] = {word: return_word, score: words[i][return_word]}
			}
			res.json(output)
		},
		find_score: function(req, res){
			output = {}
			for(var i=3; i<=6; i++){
				output[i] = scores[i][req.body[i].join("")]
			}
			res.json(output)
		}
	}
})()