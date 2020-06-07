// Client Side
// 'addEventListener' will check socket connection for new events when
// 'DOMContentLoaded' event has fired aka when HTML doc loaded and parsed
document.addEventListener('DOMContentLoaded', () => {

    // Connect to web socket
     var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + "/chat");

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

           // Display current user message
           if (data.msg) {
                const p = document.createElement('p');
                const span_username = document.createElement('span');
                const br = document.createElement('br')
                 // Display user's own message
                if (data.username == username) {
                    p.setAttribute("class", "my-msg");

                    // Username
                    span_username.setAttribute("class", "my-username");
                    span_username.innerText = data.username;

                    // HTML to append
                    p.innerHTML += span_username.outerHTML + br.outerHTML + data.msg + br.outerHTML

                    //Append
                    document.querySelector('#display-message-section').append(p);
                }
           }
    })

