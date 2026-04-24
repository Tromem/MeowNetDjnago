import React ,{useEffect,useState} from "react";
// Доделать что бы карточка отображала инфу тарифа и что бы исчезала при нажатии вне окна 
const Openorder = () =>{
    
    const [isOpen,setisOpen] = useState(false);
    const orderref = React.useRef(null)
   

    const closewindow = () =>{
        setisOpen(false)
    }
    useEffect(()=>{
        setInterval(() => {
            
            

            const buttons = document.querySelectorAll('.button-buy-text');
                const handleClick = () => {
                    setisOpen(true);
                    
                }
            
            buttons.forEach(btn => btn.addEventListener('click',()=>handleClick()));
            return () => {
          buttons.forEach(btn => btn.removeEventListener('click', handleClick()));
        };
        }, 200);
        
    },[])



    return(
        <div>
            {isOpen && (<div class="order" ref={orderref}>
    <div className="bar-order"> <div className="text-bar-order">Заказать подключение</div></div>
    <div className="container-order">
        <div class="input-blocks-order">
            <div className="text-blocks-order-inf">Город</div>
            <input type="text" id="City"></input>
            <div className="text-blocks-order-inf">Адрес</div>
            <input type="text" id="Adres"></input>
            <div className="text-blocks-order-inf">ФИО</div>
            <input type="text" id="FirstName"></input>
            <div className="text-blocks-order-inf">Номер телефона</div>
            <input type="text" id="NumberOfPhoneUser"></input>
        </div>
        
        <div class="order-inf-tarif">
            <div className="order-tarif-bar"><div className="text-order-tarif-bar">Название тарифа</div></div>
            
            <div className="order-name-tarif"><div className="text-order-name-tarif">
                
                <div className="text-order-name-tarif-pos">Тариф бадабумчик</div></div>
            </div>
            
            <div className="order-type-tarif"><img src="static/img/Cpu.png"></img><div className="text-inif-tarif">Высокоскоростной интернет</div></div>
        </div>
        
    </div>
        <button className="cancel" onClick={()=>closewindow()}>Отмена</button>
        <button className="order-button"  onClick={()=>{}}><div className="button-text">Подключиться</div></button>
   </div>)}

        </div>
    )
}
export default Openorder;