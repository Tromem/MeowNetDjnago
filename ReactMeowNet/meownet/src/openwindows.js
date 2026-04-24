import React, { useEffect, useState } from "react"

const OpenSupport = () =>{
    const [isOpen,setisOpen] = useState(false);
    
    
    useEffect(()=>{
        
        const button = document.getElementById('supportbutton');
        if(button){
            button.addEventListener('click',()=>setisOpen(true));
        }
        return()=>{
            if (button){
                button.removeEventListener('click',()=>setisOpen(true));
            }
        }
    },[])

    const MakeToClose = ()=>{
        const deletaAnim = document.getElementById('support-window');
        deletaAnim.classList.toggle('close-window');
        setTimeout(() => {
            setisOpen(false);
        }, 2000);
        
    }
    return(
            
            <div>
                {isOpen &&(<div className="support-window" id='support-window'>
        <div className="bar-support">
            <div className="text-bar-support">
                Техническая поддержка
            </div>
        </div>
        <div className="inputs-support">
            <div className="text-support-content"> ФИО </div>
            <input type="text" id="FirstName-support"></input>
            <div className="text-support-content"> Номер телефона</div>
            <input type="text" id="Numberphone-support"></input>
            <div className="text-support-content">Описание проблемы</div>
            <textarea id="Report-support"></textarea>
        </div>
        <div className="images-and-buttons">
            <label for="image-hidden-1" id="image-1">Добавить изображение</label><label for="image-hidden-2" id="image-2">Добавить изображение</label>
            <input type="file" id="image-hidden-1" ></input><input type="file" id="image-hidden-2" ></input>
            <button id="close" onClick={()=>MakeToClose()} >Отменить</button><button id="submit">Отправить</button>
        </div>
    </div>)}
                
            </div>        

    )

}
export default OpenSupport