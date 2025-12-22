const button1 = document.getElementById('confrum');

button1.addEventListener('click',function(){
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    let id = document.getElementById('id').value;
    let tech = document.getElementById('tech').checked;
    let sales = document.getElementById('sales').checked;
    let access;
    
    if(tech && sales){
        document.getElementById('textinf').textContent = 'Выберите что то одно';
        access = null;

    }else if(tech){
        access = 1;
    }else if(sales){
        access = 2;
    }
   if(access != null || access != undefined){
     fetch('/API/API-CREATE-WORKER/',{
        method:'POST',
        headers:{
            'Content-Type': 'application/json'
        }   
        ,
        body:JSON.stringify({
            'username':username,
            'password':password,
            'id':id,
            'access':access
        })
    }).then(response => response.json())
    .then(data =>console.log(data))
    .catch(error => console.error(error));
   }

   
})

