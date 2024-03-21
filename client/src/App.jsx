import React from 'react';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import Header from "./components/Header";
import Footer from "./components/Footer";
import HomePage from "./pages/HomePage";
import PropertiesPage from "./pages/PropertiesPage";
import NotFound from './components/NotFound';
import LoginPage from './pages/LoginPage'

const App = ()=> {
  return (
    <>
      <Router>
        <Header/>
        <main className='py-3'>
          <Routes>
            <Route path='/' Component={HomePage}/>
            <Route path='/properties' Component={PropertiesPage}/>
            <Route path='/login' Component={LoginPage}/>
            <Route path='*' Component={NotFound}/>
          </Routes>
          <ToastContainer theme='dark'/>
        </main>
        <Footer/>
      </Router>
    </>
  );
}

export default App;
