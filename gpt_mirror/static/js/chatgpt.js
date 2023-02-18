document.addEventListener('DOMContentLoaded', function () {
    const btnSend = document.querySelector('#btn-send');
    const msgInput = document.querySelector('#msg');
    const messageList = document.querySelector('.message-list');

    btnSend.addEventListener('click', ()=>{
        sendMessage();
    });

    msgInput.addEventListener('keyup', e => {
        if (e.key === 'Enter' || e.keyCode === 13) {
            sendMessage();
        } 
    });

    function sendMessage() {
        let msg = msgInput.value.trim();
        if (!msg) return;

        const li = document.createElement('li');
        const meMessage = makeMeMessage(msg);
        li.appendChild(meMessage);
        messageList.appendChild(li);
        meMessage.scrollIntoView();
        msgInput.disabled = true;
        btnSend.disabled = true;
        btnSend.textContent = "Sending...";

        fetch(document.URL, {
            method: 'POST',
            body: JSON.stringify({"prompt": msg}),
            headers: {
                'Content-type': 'application/json; charset=UTF-8'
            }
        }).then(response => {
            return response.text();
        }).then(text => {
            const li = document.createElement('li');
            const message = makeGptMessage(text);
            li.appendChild(message);
            messageList.appendChild(li);
            message.scrollIntoView();
            msgInput.value = "";
        }).catch(err => {
            alert(err);
        }).finally(()=>{
            msgInput.disabled = false;
            btnSend.disabled = false;
            btnSend.textContent = "Send";
            msgInput.focus();
        });
    }

    function makeMeMessage(message) {
        let messageCard = document.createElement('div');
        messageCard.classList.add('message');
        messageCard.classList.add('message-me');
        let body = document.createElement('div');
        body.classList.add('message-body');
        body.innerText = message;
        messageCard.appendChild(body);
        return messageCard;
    }

    function makeGptMessage(message) {
        let messageCard = document.createElement('div');
        messageCard.classList.add('message');
        messageCard.classList.add('message-gpt');
        let body = document.createElement('div');
        body.classList.add('message-body');
        body.innerText = message;
        messageCard.appendChild(body);
        return messageCard;
    }
});