var express = require('express');
var app = express();
var serv = require('http').Server(app);

app.use(express.static('public'));

app.set('view engine', 'ejs')
app.get('/', (req, res) => {
  res.render('index')
})
 
serv.listen(3000);

console.log("Server started.");

//////////////////////////// SOCKETS ////////////////////////////

// var ROOMS = []
// var roomCounter = 0;

var robot = null;

var io = require('socket.io')(serv,{
  cors: {
    origin: "http://localhost:3000",
    methods: ["GET", "POST"],
    transports: ['websocket', 'polling'],
    credentials: true
    },
    allowEIO3: true});

io.on('connection', (socket) => {

	console.log('socket connection');

  socket.on('message', (msg) => {
    if(msg == 'UI'){
      // var room = Math.random();
      // ROOMS.push(room);
      // socket.emit('serverMsg', `joined ${room}`)
    }
    if(msg == 'Robot'){
      // var room = ROOMS.pop()
      // socket.join(room);
      // socket.emit('serverMsg', `joined ${room}`);

      robot = socket.id
    }
  });

	socket.on('forward_UI', (data, callback) => {

    socket.to(robot).emit('forward_robot', 'fwd');

    callback({
      status: "ok"
    });
	});

  socket.on('left_UI', (data, callback) => {

    socket.to(robot).emit('left_robot', 'lft');

    callback({
      status: "ok"
    });
	});


  socket.on('right_UI', (data, callback) => {

    socket.to(robot).emit('right_robot', 'rgt');

    callback({
      status: "ok"
    });
	});


  socket.on('backwards_UI', (data, callback) => {

    socket.to(robot).emit('backwards_robot', 'bck');

    callback({
      status: "ok"
    });
	});


	socket.on('stop_UI', (data, callback) => {

    socket.to(robot).emit('stop_robot', 'stop');

    callback({
      status: "ok"
    });
	});

  socket.emit('serverMsg', 'hello');

  socket.on('disconnect', () => {
    console.log('user disconnected');
  });

});