const deletebutton = document.getElementById('delete-button');
deletebutton.addEventListener('click',()=>{
    
    const getselectoption = document.getElementById('deleteuser-slect');
    const option_select = getselectoption.querySelector(`[value="${getselectoption.value}"]`);
    
    const url = '/API/API-DELETE-WORKER/'
    if( getselectoption.value.length != 0  ||  isNaN(getselectoption.value)){
        console.log(getselectoption.value.length)
        fetch(url,{
            method:"POST",
            headers:{
                'Content-Type': 'application/json'
            },
            body:JSON.stringify({
                userid:parseInt(getselectoption.value),
               
    
            })
        }).then(()=>{
            message = document.getElementById('Message');
            message.style.display = 'none';
            message.textContent = "Пользователь был удален";
            message.classList.add('anim');
           
            message.style.display = 'block';
            setTimeout(() => {
                message.style.display = 'none';
            }, 3000);
        });
        getselectoption.removeChild(option_select);
        
    }
});