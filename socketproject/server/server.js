const http = require('http') //to bring http module beacause we are create a http server 
const server = http.createServer()//create a server

const socketio = require('socket.io') 

const io = socketio(server, {
    cors : {
        origin : 'http://127.0.0.1:8000',
        methods : ['GET', 'POST']
    }
})

io.on('connection', socket=> {
    console.log('connected')
    console.log(socket.id)
})

//create the listener om port 8000 --  ()=> this is callback function
server.listen(8000, ()=> console.log('listening on port 8000'))