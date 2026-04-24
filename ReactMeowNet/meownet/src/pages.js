import React from "react";
import MakeCard from "./getcard";

// Доделать отображения и пропы
const Main = ({FirstName ,LastName}) => (
<div>
    
        <div class="backgroundimagecat"><img src="{%static 'img/backgroundcat.png'%}" alt=""></img></div>
        <div class="tarif">
            <div class="parent-decor-text-tarif">
                 <div class="decor-text-tarif">Тарифы</div>
            </div>
            <div class="tarifbuttons">
                <div class="internetbutton"><div class="text-button">Интернет</div></div>
                <div class="tvbutton"><div class="text-button">Телевидение</div></div>
            </div>


               <MakeCard/>

            <img src="static/img/lapa2.png" class="lapa2"></img>
            <img src="static/img/lapa1.png"  class="lapa1" ></img>
            <div class="arrow">
                <img src="static/img/arrow.png"  id="left-arrow"></img>
                <img src="static/img/arrow.png"  id="right-arrow"></img></div>

            <div class="button-tarif">

            </div>
        </div>
               
   <footer>
    <hr></hr>
    123
   </footer>
</div>
);


export default Main;
