document.querySelector('#room-name-submit').onclick = function (e) {
    var roomName = document.querySelector('#room-name-input').value; // достаем имя комнаты которое написал пользователь
    window.location.pathname = '/' + roomName + '/'; // и выстраиваем url
};

var roomName = {{ room_name_json }}; // переменная переданная во views

var chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/' + roomName + '/'); // создаем обьект сокета и выстраиваем url для того что бы ChatConsumer поймал наш url в routing

chatSocket.onmessage = function (e) {
    var data = JSON.parse(e.data); // получаем массив json из event переданного в chatmessage методе
    var message = data['message']; // достаем текст сообщения
    document.querySelector('#chat-log').value += (message + '\n');
};

chatSocket.onclose = function (e) {
    console.error('Chat socket closed unexpected');
    // при закрытии соединения
};

document.querySelector('#chat-message-submit').onclick = function (e) {
    var messageInputDom = document.querySelector('#chat-message-input');
    var message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    // при клике забираем все что написано в поле для сообщения
    // и отправляем с помощью JSON очищенный текст сообщения который будет ловиться receive

    messageInputDom.value = '';
};