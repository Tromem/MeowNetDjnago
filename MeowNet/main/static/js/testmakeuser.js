
const button1 = document.getElementById('confrum');

button1.addEventListener('click',function(){
    let username = document.getElementById('username');
    let password = document.getElementById('password');
    let AccesLvl = document.getElementById('makeuser-select');
    let userLastName = document.getElementById('user-last-name');
    
    

   if( username.value.length >= 5 && password.value.length >= 5 && userLastName.value.length >= 5  ){
    
    fetch('/API/API-CREATE-WORKER/',{
        method:'POST',
        headers:{
            'Content-Type': 'application/json'
        }   
        ,
        body:JSON.stringify({
            'username':username.value ,
            'password':password.value ,
            'access':AccesLvl.value ,
            'user_last_name': userLastName.value 
        })
    }).then(response => response.json())
    .then(() =>{
       fetch('/API/API-GET-USER/',{
            method:'POST',
        headers:{
            'Content-Type': 'application/json'
        }   
        ,
        body:JSON.stringify({
            'username':username.value ,
        })
       }).then(response=>response.json()).then(data =>{
        delete_select = document.getElementById('deleteuser-slect');
        option = document.createElement('option');
        option.text = data.username; 
        option.value = data.id;
        delete_select.appendChild(option); 
       });
        
    })
    .then(()=>{
        username.value = '';
        password.value  = '';
        userLastName.value ='';
    })
    .catch(error =>{
        
        console.error(error)
    });
   }

   
})

