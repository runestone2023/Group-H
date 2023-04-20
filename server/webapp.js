var express = require('express');
var app = express();
var serv = require('http').Server(app);

app.set('view engine', 'ejs')
app.get('/', (req, res) => {
  res.render('index')
})
 
serv.listen(3000);

console.log("Server started.");

var io = require('socket.io')(serv,{
  cors: {
    origin: "http://localhost:3000",
    methods: ["GET", "POST"],
    transports: ['websocket', 'polling'],
    credentials: true
    },
    allowEIO3: true});
io.sockets.on('connection', function(socket){
	console.log('socket connection');
 
	socket.on('forward',function(data, callback){
		console.log(data);

    //
    callback({
      status: "ok"
    });
	});

  socket.emit('serverMsg', 'hello');

});