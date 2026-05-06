const street = document.getElementById('street')
street.addEventListener('input',(e)=>{
    const querry = e.target.value;
    const city = document.getElementById('city').value;
    const resultsContainer = document.getElementById('results-container'); 
   
    if (querry.length < 2) return;
    resultsContainer.innerHTML = '';

    const url = '/API/API-GET-ADRES/';
    fetch(url,{
        method:'POST',
        headers:{
             'Content-Type': 'application/json'
        },
        body:JSON.stringify({
            'adres':querry,
            'city':city
        })
    }).then(response => response.json()).then(data=>{
        values = Object.values(data).flat();
        
        if (values.length > 0){
            values.forEach(result => {
            const resultDiv = document.createElement('option');
            resultDiv.textContent = result['name_adres'];
            resultsContainer.appendChild(resultDiv);
        });
    }else{
        
        
        resultsContainer.textContent = 'Ничего не найдено';
    }
    }).then(()=>{
        
       
    });
    
});

