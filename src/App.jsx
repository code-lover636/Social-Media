import { BrowserRouter, Routes, Route} from 'react-router-dom';

import {Welcome, Login, Home} from './Pages';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" exact element={<Welcome />} />
        <Route path="/login" element={<Login />} />
        <Route path="/home" element={<Home />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
