document.getElementById('work-shift-button').addEventListener('click',()=>{
    const url_work_shift = '/API/API-Change-work-shift/';
    const errorwindow = document.getElementById('errors');
    const errormod = document.getElementById('errorinf');
    fetch(url_work_shift,{
        method:'POST'
    }).then(response=>response.json()).then(data =>{
        
        if(data.error){
            
            errormod.textContent = data.error
            errorwindow.style.visibility = 'visible';
            setTimeout(() => {
                errormod.textContent = '';
                errorwindow.style.visibility = 'hidden';
            }, 3000);
            return
        };
    }).then(()=>{
        window.location.reload()
        const container = document.getElementById('applications-container')
        if(container){
            while(container.firstChild){
                container.removeChild();
            }
        }
    });
})