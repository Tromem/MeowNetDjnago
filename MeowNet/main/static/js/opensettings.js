const button = document.getElementById('settings-button');

const settings = document.getElementById('settings');
    settings.style.display = "none";

button.addEventListener('click',function(){
    
    if (settings.style.display == "none"){
        settings.style.display = "block";
        
    
    }else{
        settings.style.display = "none";
        
    }
    
    
    
});