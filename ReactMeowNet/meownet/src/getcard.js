import React, { useEffect, useState } from 'react';
import Openorder from './openorder';


const MakeCard = ()=>{
    const [data,setData] = useState([]);
    
    useEffect(()=>{
    const url = 'http://127.0.0.1:8000/API/API-GET-CARDS/';
    fetch(url).then(response => response.json()).then(data=>{
        
        setData(data);
        
    })

    },[]);
    
    
   

    return(
        
        <div className='cards-container'>
                {Array.isArray(data) && data.map(item=>(
                    
                
                <div className="card" id={`card-`+item.pk} key={item.pk}>
                    
                    <div className="tarif-type"><div className="tarif-type-text"></div>
                    {item.fields.typetarif === 1 &&("Интернет")}
                    {item.fields.typetarif === 2 &&("Телевидение")}
                    {item.fields.typetarif === 3 &&("Интернет + Телевидение")}
                    </div>
                    <div>
                        <div className="tarif-name"><div className="tarif-name-text"></div>{item.fields.Tarif_name}</div>
                        
                        <hr></hr>
                    </div>
                    
                    <div class="tarif-speed-word">
                        <img src="static/img/Cpu.png" alt=""></img>
                        <div className="tarif-speed-word-text">{item.fields.typetarif === 1 &&("Высокоскоростной интернет")} </div>
                     </div>
                    <hr></hr>
                    <div className="tarif-inf">
                       
                        <div className="prise"> <div className="prise-text">{item.fields.price}руб. </div> </div>
                        <div className="speed"> <div className="speed-text">{item.fields.speed}Мбит/c </div></div>
                       
                    </div>
                    
                    <div className="button-buy"><button className="button-buy-text" order-key={item.pk}>Купить</button></div>
                </div>


                ))}
                
        </div>
    )
        
}

export default MakeCard