import React from "react";

const Auth = () =>{

    return (
        <div>
            <div class="login">
    <div class="log-container">
        <img src='/static/img/Net.png' alt=""></img>
        <div class="logoAuth">MeowNet</div>
        <div class="text-login"><text>Вход в личный кабинет </text></div>
        <div class="choice">
            <div><button class="User-id"> Лицевой счет</button></div>
            <div><button class="number-phone-user">Логин</button></div>
    </div>
        <div class="databar">
            
                <input  name = 'username'type="text" placeholder="Логин" id="login" ></input>
                <input  name='password' type="password" placeholder="Пароль" id="password"></input>
            
        </div>
        
        <div ><button class="confrum-button">Продолжить</button></div>
        
        <div class="user-legal"> 
            <text> Нажимая кнопку “Войти”,вы принимаете условия пользовательского соглашения</text></div>
        <hr></hr>
            <div class="forgotpassword"><text><a href="">Забыли пароль?</a></text> </div>
    </div>
        
    </div>
        </div>
    )

}
export default Auth;