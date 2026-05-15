const buttons = document.querySelectorAll('.save-btn')
buttons.forEach(button =>{
    button.addEventListener('click',()=>{
       fetch('/API/API-MakeUser/',{
        method:"POST",
        headers:{'Content-Type': 'application/json'},
        body:JSON.stringify({
            id:button.value
        })
    
       })
    })
})