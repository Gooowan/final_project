console.log('Hello from index.js');

const username = document.getElementById('username');
const message = document.getElementById('message');


function handle_click() {
    console.log(username.value);
    console.log(message.value);
}