const button = document.getElementById('submit-btn-problem');
button.addEventListener('click',()=>{
    const text = document.getElementById('problem-id');
    const url = '/API/API-NEW-SUP-APP/';
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify({
            'text':text.value
        })
    }).then(response => response.json()).then(data=>{
        if(data.error){
            alert(data.error);
            return;
        }
        alert('Заявка была успешно отправлена');
        text.value = '';

    })
});