import React from 'react';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { ToastContainer } from "react-toastify";
import Header from "./components/Header";
import Footer from "./components/Footer";
import HomePage from "./pages/HomePage";
import PropertiesPage from "./pages/PropertiesPage";

const App = ()=> {
  return (
    <>
      <Router>
        <Header/>
        <main className='py-3'>
          <Routes>
            <Route path='/' Component={HomePage}/>
          </Routes>
          <Routes>
            <Route path='/properties' Component={PropertiesPage}/>
          </Routes>
        </main>
        <Footer/>
      </Router>
      <ToastContainer/>
    </>
  );
}

export default App;
