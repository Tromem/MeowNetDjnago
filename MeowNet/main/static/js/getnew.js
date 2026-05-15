
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
            
            console.log(container)

            
           

            if (data.error) {
                
                errormod.textContent = data.error;
                errorwindow.style.visibility = 'visible';
                
                setTimeout(() => { 
                    errorwindow.style.visibility = 'hidden';
                    errormod.textContent = ''; }, 3000);
                return
              if (container) {
                        while (container.firstChild) {
                        container.removeChild(container.firstChild);
                        }
}  
            }else if(data.notfound){
                
                
                errormod.textContent = data.notfound;
                 errorwindow.style.visibility = 'visible';
               
                 setTimeout(() => { 
                    errorwindow.style.visibility = 'hidden';
                    errormod.textContent = ''; }, 3000);
                    
                
            }

          
        }).then(()=>{
            sessionStorage.setItem('error',data.error)
            window.location.reload();
        })
        .catch(err => {
            console.error('Ошибка при получении заявок:', err);
        });
});