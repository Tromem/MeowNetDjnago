const button = document.getElementById('settings-button');

button.addEventListener('click',function(){
    const settings = document.getElementById('settings');
    if (settings.style.display != "none"){
        settings.style.display = "none";
    }else{
        settings.style.display = "block";
    }
    
    
    
});