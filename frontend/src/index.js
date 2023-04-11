import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { ColorModeScript, ChakraProvider, theme } from '@chakra-ui/react';
import 'react-toastify/dist/ReactToastify.css';
// import ParticlesComponent from './components/Particle';
import Particle from './components/Particle.js';




const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(

  <div className="mainClass">
    <Particle />
    <ChakraProvider theme={theme}>
      <ColorModeScript />
      <App />
    </ChakraProvider>
  </div>
);

