document.getElementById('balance-batton-add').addEventListener('click',()=>{
    const url = 'API/Add-balance/';
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'json/application'
        },
        
    })

});