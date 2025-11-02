import { useState } from "react";
import "./App.css";

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [isTyping, setIsTyping] = useState(false);

  // Send text to backend
  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage = { text: input, sender: "user" };
    setMessages([...messages, userMessage]);
    setInput("");
    setIsTyping(true);

    try {
      const res = await fetch("http://127.0.0.1:8000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: userMessage.text }),
      });

      const data = await res.json();
      const botMessage = { text: data.reply, sender: "nami" };

      setMessages((prev) => [...prev, botMessage]);
      speak(botMessage.text);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        { text: "⚠️ Error connecting to Nami.", sender: "nami" },
      ]);
    } finally {
      setIsTyping(false);
    }
  };

  // 🎙️ Voice input
  const handleVoiceInput = () => {
    const recognition = new (window.SpeechRecognition ||
      window.webkitSpeechRecognition)();
    recognition.lang = "en-US";
    recognition.onresult = (event) => {
      setInput(event.results[0][0].transcript);
    };
    recognition.start();
  };

  // 🔊 Voice output
  const speak = (text) => {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = "en-US";
    speechSynthesis.speak(utterance);
  };

  return (
    <div className="app">
      <h1 className="title">Nami 💫</h1>

      <div className="chat-box">
        {messages.map((msg, i) => (
          <div key={i} className={`msg ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
        {isTyping && <p className="typing">Nami is typing...</p>}
      </div>

      <div className="controls">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
        />
        <button className="send-btn" onClick={handleSend}>
          Send
        </button>
        <button className="mic-btn" onClick={handleVoiceInput}>
          🎙️
        </button>
      </div>
    </div>
  );
}

export default App;

