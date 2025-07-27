import { useState } from 'react';
import { useImmer } from 'use-immer';
import api from '../api';
import ChatMessages from './ChatMessages';
import ChatInput from './ChatInput';

function Chatbot() {
  // We don't need chatId anymore, so it has been removed.
  const [messages, setMessages] = useImmer([]);
  const [newMessage, setNewMessage] = useState('');

  const isLoading = messages.length > 0 && messages[messages.length - 1].loading;

  async function submitNewMessage() {
    const trimmedMessage = newMessage.trim();
    if (!trimmedMessage || isLoading) return;

    // Add user message and a loading state for the assistant's reply
    setMessages(draft => {
      draft.push({ role: 'user', content: trimmedMessage });
      draft.push({ role: 'assistant', content: '', loading: true });
    });
    setNewMessage('');

    try {
      // FIX: Call the single, stateless sendMessage function from your API service
      const agentText = await api.sendMessage(trimmedMessage);

      // FIX: Update the last message (the loading one) with the full response
      setMessages(draft => {
        draft[draft.length - 1].content = agentText;
        draft[draft.length - 1].loading = false;
      });

    } catch (err) {
      console.error("Error sending message:", err);
      setMessages(draft => {
        draft[draft.length - 1].loading = false;
        draft[draft.length - 1].error = true;
      });
    }
  }

  return (
    <div className='relative grow flex flex-col gap-6 pt-6'>
      {messages.length === 0 && (
        <div className='mt-3 font-urbanist text-primary-blue text-xl font-light space-y-2'>
          <p>👋 Welcome!</p>
          <p>I am powered by the latest technology from Google Gemini.</p>
          <p>Ask me anything.</p>
        </div>
      )}
      <ChatMessages
        messages={messages}
        isLoading={isLoading}
      />
      <ChatInput
        newMessage={newMessage}
        isLoading={isLoading}
        setNewMessage={setNewMessage}
        submitNewMessage={submitNewMessage}
      />
    </div>
  );
}

export default Chatbot;
