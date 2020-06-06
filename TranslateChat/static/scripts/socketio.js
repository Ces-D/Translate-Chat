// Client Side
// 'addEventListener' will check socket connection for new events when
// 'DOMContentLoaded' event has fired aka when HTML doc loaded and parsed
document.addEventListener('DOMContentLoaded', () => {
     var socket = io.connect('http://' + document.domain + ':' + location.port);

     // creating event buckets
     socket.on('connect',() => {
        socket.send("I am connected");
     });
// may not need
// consider using JQUERY
     socket.on('message', data => {
        const p = document.createElement('p');
        const br = document.createElement('br');
        p.innerHTML = data;
        // refer to chat.html for the query selected
        document.querySelector('#display-message-section').append(p);
     });
// may not need
     socket.on('some-event', data =>{
        console.log(data)
     });

     // the most vital part, sends to page and not log
    document.querySelector('#send_message').onclick = () => {
        socket.send(document.querySelector('#user_message').value);
    }
})