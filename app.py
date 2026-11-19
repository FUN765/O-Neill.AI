from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>REILLY.AI</title>
<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #171717;
    color: white;
    display: flex;
    height: 100vh;
}

/* Sidebar */
.sidebar {
    width: 250px;
    background: #202020;
    padding: 20px;
}

.logo {
    font-size: 27px;
    font-weight: bold;
    margin-bottom: 30px;
}

.new-chat {
    width: 100%;
    padding: 13px;
    border: 1px solid #555;
    border-radius: 10px;
    background: #303030;
    color: white;
    cursor: pointer;
    font-size: 15px;
}

.new-chat:hover {
    background: #414141;
}

/* Main chat */
.main {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
}

.topbar {
    width: 100%;
    padding: 20px;
    border-bottom: 1px solid #333;
    font-size: 18px;
    font-weight: bold;
}

.welcome {
    margin-top: 100px;
    text-align: center;
}

.welcome h1 {
    font-size: 40px;
}

.welcome p {
    color: #aaa;
}

/* Messages */
.messages {
    width: 100%;
    max-width: 800px;
    flex: 1;
    overflow-y: auto;
    padding: 25px;
}

.message {
    padding: 15px 20px;
    border-radius: 15px;
    margin-bottom: 18px;
    max-width: 85%;
    line-height: 1.5;
}

.user {
    background: #343434;
    margin-left: auto;
}

.ai {
    background: #242424;
    margin-right: auto;
}

/* Input */
.input-area {
    width: 90%;
    max-width: 800px;
    margin: 20px;
    padding: 12px;
    background: #303030;
    border: 1px solid #555;
    border-radius: 18px;
    display: flex;
    gap: 10px;
}

.input-area input {
    flex: 1;
    background: transparent;
    border: none;
    outline: none;
    color: white;
    font-size: 16px;
    padding: 10px;
}

.input-area button {
    background: white;
    color: black;
    border: none;
    border-radius: 10px;
    padding: 12px 18px;
    cursor: pointer;
    font-weight: bold;
}

.input-area button:hover {
    background: #ccc;
}
</style>
</head>

<body>

<div class="sidebar">
    <div class="logo">✦ REILLY.AI</div>
    <button class="new-chat" onclick="newChat()">+ New Chat</button>
</div>

<div class="main">

    <div class="topbar">REILLY.AI</div>

    <div class="welcome" id="welcome">
        <h1>Welcome to REILLY.AI</h1>
        <p>What can I help you with today?</p>
    </div>

    <div class="messages" id="messages"></div>

    <div class="input-area">
        <input id="userInput"
        placeholder="Message REILLY.AI..."
        onkeydown="if(event.key==='Enter') sendMessage()">

        <button onclick="sendMessage()">↑</button>
    </div>

</div>

<script>
function sendMessage() {
    let input = document.getElementById("userInput");
    let text = input.value.trim();

    if (!text) return;

    document.getElementById("welcome").style.display = "none";

    let messages = document.getElementById("messages");

    let userMessage = document.createElement("div");
    userMessage.className = "message user";
    userMessage.textContent = text;
    messages.appendChild(userMessage);

    let aiMessage = document.createElement("div");
    aiMessage.className = "message ai";
    aiMessage.textContent = "REILLY.AI response will appear here.";
    messages.appendChild(aiMessage);

    input.value = "";
    messages.scrollTop = messages.scrollHeight;
}

function newChat() {
    document.getElementById("messages").innerHTML = "";
    document.getElementById("welcome").style.display = "block";
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
