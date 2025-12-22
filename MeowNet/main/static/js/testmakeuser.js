

const button = document.getElementById('confrum')

button.addEventListener('click',function(){
    username = document.getElementById('username').value;
    password = document.getElementById('password').value;
    id = document.getElementById('id').value;
    
    fetch('/API/API-CREATE-WORKER/',{
        method:'POST',
        headers:{
            'Content-Type': 'application/json'
        }   
        ,
        body:JSON.stringify({
            'username':username,
            'password':password,
            'id':id
        })
    }).then(response => response.json())
    .then(data =>console.log(data))
    .catch(error => console.error(error));
})

