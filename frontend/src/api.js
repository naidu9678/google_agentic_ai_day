// src/agentService.js

// The URL of your locally running FastAPI backend
const BASE_URL = 'http://127.0.0.1:8000';

/**
 * Sends a message to the agent backend and gets a response.
 * @param {string} message The user's message to send.
 * @returns {Promise<string>} The agent's text response.
 */
async function sendMessage(message) {
  // We call the single "/chat" endpoint
  const res = await fetch(BASE_URL + '/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    // The body matches the API's expected format: {"message": "..."}
    body: JSON.stringify({ message: message }),
  });

  // Handle potential errors from the API
  if (!res.ok) {
    const errorData = await res.json();
    console.error("API Error:", errorData);
    return Promise.reject({ status: res.status, data: errorData });
  }

  // Parse the JSON response and return the agent's text
  const data = await res.json();
  return data.response;
}

export default {
  sendMessage,
};
