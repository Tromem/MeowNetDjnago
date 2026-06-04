
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
                
                
                
                alert(data.error);
               
                return
              if (container) {
                        while (container.firstChild) {
                        container.removeChild(container.firstChild);
                        }
}  
            }else if(data.notfound){
                
                alert("Сейчас нет доступных заявок");
                errormod.textContent = data.notfound;
                 
               
                
            }

          
        }).then(()=>{
            alert(data.error)
            window.location.reload();
        })
        .catch(err => {
            window.location.reload();
        });
});