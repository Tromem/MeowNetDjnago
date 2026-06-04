document.getElementById('work-shift-button').addEventListener('click',()=>{
    const url_work_shift = '/API/API-Change-work-shift/';
    const errorwindow = document.getElementById('errors');
    const errormod = document.getElementById('errorinf');
    fetch(url_work_shift,{
        method:'POST'
    }).then(response=>response.json()).then(data =>{
        
        if(data.error){
            
           make_message(data.error);
            setInterval(()=>{
                window.location.reload();
                
            },5000)
            return;
        };
        make_message("Смена была обновлена!");
            setInterval(()=>{
                window.location.reload();
            },5000)
    });
})