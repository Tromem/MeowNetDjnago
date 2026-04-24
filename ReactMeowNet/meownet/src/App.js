

import React, { useState } from 'react';
import {BrowserRouter as  Router,Route ,Routes,Navigate} from 'react-router-dom'
import Main from './pages';
import OpenSupport from './openwindows';
import { Helmet } from 'react-helmet';
import Openorder from './openorder';
import Auth from './auth';



const HomePage =() =>{
  return (
  <div>
    <Main/>
    <OpenSupport/>
    
    <Openorder/>
  </div>
  
)
}
const Profilepage = () =>{
  const [isRegistred, SetisRegistred] = useState(false); 
  if(!isRegistred){
    return <Navigate to='/'/>;
  }
  return <h2>Не люди</h2>
}
const Autorization =() =>{
    
  return (
    <div>     
      <OpenSupport/>
      <Auth/>
    </div>
  )
}
const  App =()=>(
  <Router>
    <div>
        <Routes>
        <Route path='/user/auth' element={<Autorization/>}></Route>
        <Route path='/profile' element={<Profilepage/>}></Route>
        <Route path='/' element={<HomePage/>}></Route>
        </Routes>
      
    </div>
  </Router>
);

export default App;
