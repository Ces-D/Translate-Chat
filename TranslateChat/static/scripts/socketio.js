// Client Side
// 'addEventListener' will check socket connection for new events when
// 'DOMContentLoaded' event has fired aka when HTML doc loaded and parsed
document.addEventListener('DOMContentLoaded', () => {

    // Connect to web socket
     var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    // Get username
    const username = document.querySelector('#get-username').innerHTML;

    // Set default room
    let room = "Lounge"
    joinRoom("Lounge");

    // Send Messages
    document.querySelector('#send_message').onclick = () => {
        socket.emit('incoming-msg',{'msg': document.querySelector('#user_message').value,
        'username':username, 'room':room});

        document.querySelector('#user_message').value ='';
    };

    // Display all Incoming Messages
    socket.on('message', data => {
           // Display current message
           if (data.msg) {
                const p = document.createElement('p');
                const span_username = document.createElement('span');
                const span_timestamp = document.createElement('span');
                const br = document.createElement('br')
        }})
    }


