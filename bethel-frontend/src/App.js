import React from 'react';
import axios from 'axios';
import logo from './logo_prejub.svg';
import './App.css';
import Icon from '@mdi/react';
import { Container } from '@material-ui/core';
import { mdiYoutubeTv } from '@mdi/js';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <div>
          <p>
            El sitio aun esta en desarrollo, pero puedes visitar nuestro canal de youtube!
          </p>
          <a
          className="App-link"
          href="https://www.youtube.com/channel/UCIWPyY8FTYJtDcCj9YnLXdA"
          target="_blank"
          rel="noopener noreferrer"
          >
          <p>
            <Icon path={mdiYoutubeTv} title="youtube" size={2} color="red"/>
          </p>
          </a>
        </div>
      </header>
    </div>
  );
}

export default App;
