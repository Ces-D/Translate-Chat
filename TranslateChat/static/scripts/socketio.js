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

                    // Append
                    document.querySelector('#display-message-section').append(p);
                }

               // Display other user's Messages
               else if (typeof data.username!== 'undefined'){
                    p.setAttribute("class", "other-msg");

                    // Username
                    span_username.setAttribute("class", "other-username");
                    span_username.innerText = data.username;

                    // HTML to append
                    p.innerHTML += span_username.outerHTML + br.outerHTML + data.msg + br.outerHTML

                    // Append
                    document.querySelector('#display-message-section').append(p);
               }

           }
           scrollDownChatWindow();
    });

    // Select a room
    document.querySelectorAll('.select-room').forEach(p => {
        p.onclick = () => {
            let newRoom = p.innerHTML

            // Check if user already in the room
            if (newRoom === room) {
                msg = `You are already in ${room} room.`;
                printSysMsg(msg);

                // else put user in the newRoom
            } else {
                leaveRoom(room);
                joinRoom(newRoom);
                room = newRoom;
            }
        };
    });

    // Leave room
    function leaveRoom(room) {
        socket.emit('leave', {'username': username, 'room':room});
    }

    //Join room
    function joinRoom(room){
        socket.emit('join', {'username':username, 'room':room});

        // Clear message area
        document.querySelector('#display-message-section').innerHTML = '';

        // Autofocus on text box
        document.querySelector('#user_message').focus();
    }

    // Scroll chat window down
    function scrollDownChatWindow(){
        const chatWindow = document.querySelector('#display-message-section');
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

}

