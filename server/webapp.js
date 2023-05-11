var express = require('express');
const { ExpressPeerServer } = require("peer")
var app = express();
var serv = require('http').Server(app);

app.use(express.static('public'));

app.set('view engine', 'ejs')
app.get('/', (req, res) => {
  res.render('index')
})
 
serv.listen(3000);

const peerServer = ExpressPeerServer(serv, {
	path: "/peerjs",
});

app.use("/", peerServer);

console.log("Server started.");

//////////////////////////// SOCKETS ////////////////////////////

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

  socket.on('join-room', (roomId, userId) => {
    socket.join(roomId)
    socket.to(roomId).emit('user-connected', userId)

    socket.on('disconnect', () => {
      socket.to(roomId).emit('user-disconnected', userId)
    })
  })

  socket.on('message', (msg) => {
    if(msg == 'UI'){
    }
    if(msg == 'Robot'){
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