const button = document.getElementById('check-status').addEventListener('click',()=>{
    const  table = document.getElementById("status-applications");
    const button = document.getElementById('check-status')
    console.log(table.style.display)
    if(table.style.display == 'block'){
        button.textContent = 'Открыть статус своих заявок'
        table.style.display ='none';
    }else{
        button.textContent = 'Закрыть статус своих заявок'
        table.style.display = 'block';
    }
})