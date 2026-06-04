
document.addEventListener('DOMContentLoaded',()=>{
    const item = sessionStorage.getItem('error')
    
});
document.getElementById('new-application').addEventListener('click',()=>{
    url_get_new_app = '/API/API-GET-NEW-APP/';
    const wind = window;
    
    const errormod = document.getElementById('errorinf');
    const errorwindow = document.getElementById('errors');
    fetch(url_get_new_app,{
        method:'POST'
    }).then(response => response.json())
        .then(data => {
            
            const container = document.getElementById('applications-container');
            
           

            
           

            if (data.error) {
                
                
                make_message(data.error);
               
               
                return
              if (container) {
                        while (container.firstChild) {
                        container.removeChild(container.firstChild);
                        }
}  
            }else if(data.notfound){
                make_message("Сейчас нет доступных заявок");
                
                errormod.textContent = data.notfound;
                 
               
                
            }

          
        }).then(()=>{
            
            make_message(data.error);
            setInterval(()=>{
                window.location.reload();
            },5000)
            
        })
        .catch(err => {
           setInterval(()=>{
                window.location.reload();
            },5000)
        });
});