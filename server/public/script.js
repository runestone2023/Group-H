const socket = io('/')
const videoGrid = document.getElementById('video-grid')
const myVideo = document.createElement('video')
myVideo.autoPlay = true
myVideo.playsInline = true
myVideo.muted = true
const peers = {}
window.navigator.mediaDevices.getUserMedia({
  video: true,
  audio: false
}).then(stream => {
  addVideoStream(myVideo, stream)

  const myPeer = new Peer(undefined, {
    host: 'robotserver.live',
    path: '/peerjs',
    proxied: true
  })

  myPeer.on('call', call => {
    call.answer(stream)
    const video = document.createElement('video')
    call.on('stream', userVideoStream => {
      addVideoStream(video, userVideoStream)
    })
  })

  socket.on('user-connected', userId => {
    connectToNewUser(userId, stream)
  })
  socket.on('user-disconnected', userId => {
    if (peers[userId]) peers[userId].close()
  })
  
  myPeer.on('open', id => {
    socket.emit('join-room', ROOM_ID, id)
  })
  
  function connectToNewUser(userId, stream) {
    const call = myPeer.call(userId, stream)
    const video = document.createElement('video')
    call.on('stream', userVideoStream => {
      addVideoStream(video, userVideoStream)
    })
    call.on('close', () => {
      video.remove()
    })
  
    peers[userId] = call
  }
  
  function addVideoStream(video, stream) {
    video.srcObject = stream
    
    video.autoPlay = true
    video.playsInline = true
    video.muted = true
  
    video.addEventListener('loadedmetadata', () => {
      video.play()
    })
    videoGrid.append(video)
  }
})