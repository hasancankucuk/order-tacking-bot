import React, { JSX, useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate, useLocation } from 'react-router-dom';
import './App.css';
import { Chatbot } from './components/chatbot/Chatbot';
import { Menu } from './components/menu/Menu';
import {
  Introduction,
  DatabaseViewer,
  SQLPlayground,
  BotArchitecture,
  TestCases,
  // EvaluationMetrics,
  Settings,
  Login
} from './pages';


function RequireAuth({ children }: { children: JSX.Element }) {
  const location = useLocation();
  const user = localStorage.getItem('user');
  if (!user) {
    return <Navigate to="/login" state={{ from: location }} replace />;
  }
  return children;
}

function App() {
  const [showChatbot, setShowChatbot] = useState(false);
  console.log('Backend URL:', process.env.REACT_APP_BACKEND_URL)
  const user = localStorage.getItem('user');
  return (
    <Router>
      <div className="App">
        <div className="uk-grid-match uk-child-width-1-4@m uk-child-width-1-4@s" uk-grid="true">
          {user && (
            <div style={{ minWidth: 220, maxWidth: 280, height: '100vh', position: 'sticky', top: 0 }} className='uk-height-1-1'>
              <Menu />
            </div>

          )}
          <div style={{ flex: 1, minWidth: 0 }}>
            <Routes>
              <Route path="/login" element={<Login />} />
              <Route path="/" element={<RequireAuth><Navigate to="/introduction" replace /></RequireAuth>} />
              <Route path="/introduction" element={<RequireAuth><Introduction /></RequireAuth>} />
              <Route path="/database-viewer" element={<RequireAuth><DatabaseViewer /></RequireAuth>} />
              <Route path="/sql-playground" element={<RequireAuth><SQLPlayground /></RequireAuth>} />
              <Route path="/bot-architecture" element={<RequireAuth><BotArchitecture /></RequireAuth>} />
              <Route path="/test-cases" element={<RequireAuth><TestCases /></RequireAuth>} />
              {/* <Route path="/evaluation-metrics" element={<RequireAuth><EvaluationMetrics /></RequireAuth>} /> */}
              <Route path="/chatbot" element={<RequireAuth><Chatbot /></RequireAuth>} />
              <Route path="/settings" element={<RequireAuth><Settings /></RequireAuth>} />
            </Routes>
          </div>
        </div>
      </div>
      <div
        className="fab"
        onClick={() => setShowChatbot((prev) => !prev)}
        title="Open Chatbot"
      >
        🤖
      </div>
      {showChatbot && (
        <div style={{
          position: "fixed",
          bottom: 100,
          right: 32,
          zIndex: 1001,
        }}>
          <Chatbot />
        </div>
      )}
    </Router>
  );
}

export default App;
