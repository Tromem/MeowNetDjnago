document.getElementById('balance-batton-add').addEventListener('click',()=>{
    const balance = document.getElementById('balasne');
    const url = 'API/Add-balance/';
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'json/application'
        },
        
    }).then(()=>{
        const balance_money = balance.textContent;
        
        let balance_inf = parseInt(balance_money.replace(/[A-Za-zа-яА-ЯёЁ.]/g,''));
        balance_inf+=1000;
        console.log(balance_inf);
        balance.textContent = balance_inf + "руб.";
        make_message('Баланс успешно пополнен!');
    });
    

});