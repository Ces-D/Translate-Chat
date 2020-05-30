// Client Side
// 'addEventListener' will check socket connection for new events when
// 'DOMContentLoaded' event has fired aka when HTML doc loaded and parsed
document.addEventListener('DOMContentLoaded', () => {
     var socket = io.connect('http://' + document.domain + ':' + location.port);

     // creating event buckets
     socket.on('connect',()=>{
        socket.send("I am connected");
     });

     socket.on('message', data => {
        console.log(`Message received: ${data}`)
     });

     socket.on('some-event', data =>{
        console.log(data)
     });
    document.querySelector('#send_message').onclick = () => {
        socket.send(document.querySelector('#user_message').value);
    }
})