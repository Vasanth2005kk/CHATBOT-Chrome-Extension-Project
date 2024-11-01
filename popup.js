document.addEventListener("DOMContentLoaded", function() {
    var conversation = document.getElementById("conversation");
    var userInput = document.getElementById("user-input");
    var submitButton = document.getElementById("submit-button");
  
    userInput.addEventListener("keyup", function(event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            submitButton.click();
        }
    });
  
    submitButton.addEventListener("click", function() {
        var userMessage = userInput.value;
        if (userMessage.trim() === "") return;
        
        conversation.innerHTML += "<p>User: " + userMessage + "</p>";
        userInput.value = "";
  
        // Send message to chatbot backend
        chat_with_chatbot(userMessage);
    });
  
    function chat_with_chatbot(message) {
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "http://localhost:5000/chatbot", true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                conversation.innerHTML += "<p>Bot: " + response.response + "</p>";
            }
        };
        xhr.send(JSON.stringify({ conversation: message }));
    }
  });
  