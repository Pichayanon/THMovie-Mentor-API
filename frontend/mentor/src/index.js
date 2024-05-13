import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import About from './components/About'
import Contact from './components/Contact'
import GenrePage from './components/GenrePage'
import PlatformPage from './components/PlatformPage'
import Visualization from './components/Visualization';


const router = createBrowserRouter([
  {
      path: "/",
      element: <App />
  },
  {
      path: "about",
      element: <About />
  },
  {
      path: "contact",
      element: <Contact />
  },
  {
      path: "genre",
      element: <GenrePage />
  },
  {
      path: "platform",
      element: <PlatformPage />
  },
  {
      path: "visualization",
      element: <Visualization />
  },
])

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
