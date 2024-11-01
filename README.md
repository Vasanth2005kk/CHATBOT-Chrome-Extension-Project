###### ChatBot Extension Documentation


# Overview

The ChatBot Extension is a Chrome extension that enables a simple chat interface between users and a chatbot backend server, built with Flask and using the Groq API. Users can send messages from the extension's popup interface, which are processed by the backend chatbot server and returned in a formatted response.

# Project Structure

   1. main.py - Backend server (Flask) with chatbot endpoint.
   2. background.js - Service worker for the Chrome extension.
   3. popup.html - HTML structure for the extension’s user interface.
   4. popup.js - Frontend JavaScript for handling user input and communication with the backend.
   5. manifest.json - Metadata file for Chrome extension configuration.

## **1. main.py** (Backend Service)

This file implements a Flask-based API for the chatbot, using the `Groq` API client to interact with a chatbot model.

### Code Walkthrough

- **Flask App Setup**:
  - `Flask` and `CORS` are used to create a web server with cross-origin access.
  - The `Groq` client is initialized with an API key for accessing chatbot services.

- **API Endpoint**: `/chatbot`
  - **Method**: `POST`
  - **Purpose**: Receives messages from the Chrome extension frontend, sends them to the chatbot model, and returns the model’s response.
  - **Request**: Expects a JSON object containing the `conversation` message.
  - **Response**: Returns a JSON object with the chatbot's response.

- **chat_with_chatbot() Function**:
  - Calls the chatbot model with a specified `temperature`, `max_tokens`, and `top_p` to control the response generation.
  - Extracts the text response and returns it to the API endpoint.

- **chatbot_format() Function**:
  - Parses the chatbot response to apply HTML formatting based on special characters (`*` and `-`).

- **Run**:
  - `app.run()` starts the Flask server on `port 5000` in debug mode.

---

## **2. background.js** (Chrome Extension Service Worker)

Handles background tasks for the Chrome extension.

- **chrome.action.onClicked**:
  - Opens `popup.html` in a new tab when the extension icon is clicked.

---

## **3. popup.html** (Extension Frontend Interface)

This HTML file provides a simple UI for the chatbot extension.

### Structure

- **CSS**: Inline styling to control the layout and styling of the conversation box and input fields.
- **HTML Elements**:
  - **#conversation**: A container to display chat history.
  - **#user-input**: An input field where users can type messages.
  - **#submit-button**: A button to submit user messages to the backend.

---

## **4. popup.js** (Frontend JavaScript for popup.html)

Handles the frontend logic of the chatbot interaction.

### Code Walkthrough

- **Event Listeners**:
  - Adds an event listener to detect `Enter` key presses for sending messages.
  - Adds a click event on the `submit-button` to send user input to the backend.

- **chat_with_chatbot(message)**:
  - Uses `XMLHttpRequest` to make a `POST` request to the Flask server (`http://localhost:5000/chatbot`).
  - Sends the user's message in JSON format.
  - Receives and appends the bot's response to the conversation box.

---

## **5. manifest.json** (Chrome Extension Manifest)

Defines the metadata and permissions for the Chrome extension.

### Fields

- **manifest_version**: Specifies version 3 (required for current Chrome extensions).
- **name**: The name displayed in the Chrome extension store and toolbar.
- **version**: Version of the extension.
- **description**: Brief description of the extension's purpose.
- **background**: Declares `background.js` as a service worker for background tasks.
- **action**: Defines `popup.html` as the default UI when the extension icon is clicked.
- **permissions**: Grants permissions for interacting with active tabs and managing tabs.

---

### **How the Application Works**

1. **User Interaction**:
   - The user opens the extension popup, types a message in the input field, and clicks "Send" (or presses `Enter`).

2. **Message Processing**:
   - The `popup.js` script captures the message and sends it to the Flask API (`/chatbot` endpoint) on the local server.
   - The Flask API receives the message, processes it using the `Groq` client, and returns a response.

3. **Displaying Response**:
   - `popup.js` receives the API response and displays it in the conversation box within the popup interface.

---

### **Usage**

1. Start the Flask server by running `main.py`.
   ```bash
   python main.py
   ```
2. Load the Chrome extension:
   - Open Chrome and go to `chrome://extensions`.
   - Enable "Developer mode."
   - Click "Load unpacked" and select the directory containing your project files.

3. Click the extension icon in the Chrome toolbar to interact with the chatbot.

---

### **Security Note**

- Store the `api_key` securely, as hardcoding sensitive data can lead to security vulnerabilities. Consider using environment variables.

### **Dependencies**

- **Flask**: For setting up the web server (`pip install Flask`).
- **Flask-CORS**: For handling CORS (`pip install Flask-CORS`).
- **Groq**: Ensure you have installed the `Groq` client library to interact with the chatbot model.

---