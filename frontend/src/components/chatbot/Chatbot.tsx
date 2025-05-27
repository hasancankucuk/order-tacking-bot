import { useState, useRef, useEffect } from 'react';
import { clearSession, listProducts, postMessage } from '../../services';

type Message = {
  from: 'user' | 'bot';
  text: string;
  image: string | null;
  pdf_url: string | null;
};

export const Chatbot = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [open, setOpen] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement | null>(null);
  const sessionId = 'user123';

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, open]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    setMessages((prev) => [...prev, { from: 'user', text: input, image: null, pdf_url: null }]);

    try {
      const data = await postMessage(sessionId, input);
      data.forEach((msg: any) => {
        setMessages((prev) => [
          ...prev,
          {
            from: 'bot',
            text: msg.text || '',
            image: msg.image || null,
            pdf_url: msg.custom?.pdf_url || null,
          },
        ]);
      });
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          from: 'bot',
          text: 'Sorry, the chatbot service is currently unavailable. However, you can still use the dashboard to manage your orders and database.',
          image: null,
          pdf_url: null
        },
      ]);
    }
    setInput('');
  };

  const clearChat = async () => {
    const response = await clearSession(sessionId);
    if (response) {
      setMessages([]);
      setInput('');
    } else {
      console.error('Failed to clear session');
    }
  }

  const handleListing = async () => {
    const response = await listProducts(sessionId);
    if (response) {
      response.forEach((msg: any) => {
        setMessages((prev) => [
          ...prev,
          {
            from: 'bot',
            text: msg.text || '',
            image: msg.image || null,
            pdf_url: msg.custom?.pdf_url || null,
          },
        ]);
      });
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    sendMessage();
  };

  if (!open) {
    return (
      <button
        className="chatbot-fab"
        onClick={() => setOpen(true)}
        style={{
          position: 'fixed',
          bottom: 32,
          right: 32,
          width: 64,
          height: 64,
          borderRadius: '50%',
          background: '#1976d2',
          color: 'white',
          border: 'none',
          boxShadow: '0 2px 8px rgba(0,0,0,0.2)',
          fontSize: '2rem',
          zIndex: 1000,
          cursor: 'pointer',
        }}
        title="Open Chatbot"
      >
        🤖
      </button>
    );
  }

  return (
    <div
      className="chatbot-overlay"
      style={{
        position: 'fixed',
        bottom: 110,
        right: 32,
        zIndex: 1001,
        maxWidth: 400,
        width: '90vw',
      }}
    >
      <div
        className="uk-card uk-card-default uk-card-body"
        style={{
          borderRadius: 16,
          boxShadow: '0 4px 24px rgba(0,0,0,0.18)',
          padding: 0,
          position: 'relative',
        }}
      >
        <button
          onClick={() => setOpen(false)}
          style={{
            position: 'absolute',
            top: 8,
            right: 12,
            background: 'none',
            border: 'none',
            fontSize: 24,
            color: '#888',
            cursor: 'pointer',
            zIndex: 2,
          }}
          aria-label="Close Chatbot"
        >
          ×
        </button>
        <div className="uk-container" style={{ paddingTop: 24 }}>
          <h3 className="uk-card-title">Order Bot</h3>
        </div>
        <hr className="uk-divider-icon" />
        <div className="uk-margin">
          <div
            className="uk-overflow-auto uk-height-medium uk-background-muted uk-padding-small uk-border-rounded"
            style={{ maxHeight: 350 }}
          >
            {messages.length === 0 && (
              <div className="uk-text-center uk-margin">
                <p style={{ color: '#888' }}>Start a conversation with the bot!</p>
                <ul className='uk-list'>
                  <li><button className='uk-button uk-button-default' onClick={handleListing}>List of products</button></li>
                </ul>
              </div>
            )}
            {messages.map((msg, idx) => {
              const isProductCard = msg.from === 'bot' && msg.image;

              return (
                <div
                  key={idx}
                  className={`uk-margin-small chatbot-message chatbot-message--${msg.from}`}
                  style={{
                    display: 'flex',
                    flexDirection: msg.from === 'user' ? 'row-reverse' : 'row',
                    alignItems: 'flex-start',
                  }}
                >
                  {isProductCard ? (
                    <div
                      className="uk-card uk-card-default"
                      style={{
                        width: '100%',
                        borderRadius: 12,
                        padding: 12,
                        boxShadow: '0 2px 8px rgba(0,0,0,0.05)',
                      }}
                    >
                      <img
                        src={msg.image!}
                        alt="Product"
                        style={{
                          width: '100%',
                          maxHeight: 180,
                          objectFit: 'contain',
                          borderRadius: 8,
                          marginBottom: 8,
                        }}
                      />
                      <div>
                        {msg.text.split('\n').map((line, i) => (
                          <p key={i} style={{ margin: '4px 0' }}>{line}</p>
                        ))}
                      </div>
                    </div>
                  ) : (
                    <div
                      style={{
                        maxWidth: '70%',
                        background: msg.from === 'user' ? '#e6f7ff' : '#f4f4f4',
                        color: '#222',
                        borderRadius: msg.from === 'user' ? '16px 16px 4px 16px' : '16px 16px 16px 4px',
                        padding: '10px 14px',
                        margin: '4px',
                        boxShadow: '0 1px 4px rgba(0,0,0,0.04)',
                        fontWeight: 400,
                        fontSize: '1rem',
                        wordBreak: 'break-word',
                      }}
                    >
                      <div style={{ fontSize: '0.9em', marginBottom: 4, color: '#888' }}>
                        {msg.from === 'user' ? '👤 You' : '🤖 Bot'}
                      </div>
                      <div>{msg.text}</div>
                      {msg.pdf_url && (
                        <div className="uk-margin-small-top">
                          <iframe
                            src={msg.pdf_url}
                            title="PDF Invoice"
                            width="100%"
                            height="400px"
                            style={{ border: '1px solid #ccc', borderRadius: 4 }}
                          />
                          <div style={{ marginTop: 8 }}>
                            <a href={msg.pdf_url} target="_blank" rel="noopener noreferrer" className="uk-link">
                              Download Invoice PDF
                            </a>
                          </div>
                        </div>
                      )}
                    </div>
                  )}
                </div>
              );
            })}
            <div ref={messagesEndRef} />
          </div>
        </div>
        <form
          className="uk-margin-remove"
          onSubmit={handleSubmit}
          style={{ padding: "12px 16px", backgroundColor: "#fafafa", borderTop: "1px solid #ddd" }}
        >
          <div className="uk-grid-small uk-flex-middle" uk-grid="true">
            <div className="uk-width-expand">
              <input
                className="uk-input"
                type="text"
                placeholder="Type your message..."
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={(e) => {
                  if (e.key === 'Enter' && !e.shiftKey) handleSubmit(e);
                }}
                style={{
                  borderRadius: "8px",
                  padding: "8px 12px",
                  fontSize: "14px"
                }}
              />
            </div>
            <div className="uk-width-auto">
              <button
                className="uk-button uk-button-primary"
                type="submit"
                style={{
                  fontSize: "14px",
                  padding: "6px 12px",
                  borderRadius: "6px",
                  marginRight: "6px"
                }}
              >
                Send
              </button>
              <button
                className="uk-button uk-button-default"
                data-uk-icon="icon: trash"
                onClick={clearChat}
                style={{
                  fontSize: "14px",
                  padding: "6px 12px",
                  borderRadius: "6px"
                }}
              >
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  );
};