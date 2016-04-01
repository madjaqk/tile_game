var express = require("express");
var path = require("path");

var app = express();

var bodyParser = require("body-parser");
app.use(bodyParser.urlencoded({extended: true}))
app.use(bodyParser.json())
app.use(express.static(path.join(__dirname, "/client")))
app.use(express.static(__dirname + "/node_modules"))

require("./server/config/mongoose.js")

var routes_setter = require('./server/config/routes.js');
routes_setter(app);

app.listen(8000, function() {
	console.log("listening on port 8000")
})