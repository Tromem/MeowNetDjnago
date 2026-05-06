document.getElementById('find-adres').addEventListener('click',()=>{
    const table_adres = document.getElementById('address-info');
    const city = document.getElementById('city');
    const adres = document.getElementById('street');
    const house = document.getElementById('house');
    const url = '/API/API-GET-TECH-INF/';
    const req_form = document.getElementById('request-form');
    
    table_adres.style.visibility ='hidden'; 
    const errors = document.getElementById('errors');
    errors.style.color = 'red'
    const timeout = 3000;
    
    if (adres.value == "" || house.value == "" ){
        console.log(adres.textContent)
        errors.textContent = 'Вы не заполнили все поля!';
        setTimeout(() => {
           errors.textContent = ''; 
        }, timeout);
        return
    }
    fetch(url,{
        method:'POST',
         
        headers:{
                        'Content-Type': 'application/json'
                    },
        body:JSON.stringify({
            'city':city.value,
            'adres':adres.value,   
            'house':house.value
        })
        
                    
    }).then(response => response.json()).then(data =>{
        const techsupp = document.getElementById('techsupp');
        const type_connect = document.getElementById('type-connect');
        const tech_inf = document.getElementById('tech-inf');
        var tech_supp;
        var problems = 'Неполадок не обнаруженно'
        const req_form = document.getElementById('request-form');
        ParsedData = JSON.parse(data.response)[0];

        Fields = ParsedData.fields;
        
        if (Fields.tech_opportunity == "НТХВ"){
            tech_supp = 'НТХВ'
            techsupp.style.color = 'red'
        }else if(Fields.ports > 0){
            tech_supp = 'Есть ТХВ';
            techsupp.style.color = 'green'
        }else{
            tech_supp = 'НТХВ';
            techsupp.style.color = 'red'
        }
        if (ParsedData.problem != null){
            problems = ParsedData.problem
        }
        techsupp.textContent = tech_supp;
        console.log(Fields)
        type_connect.textContent = Fields.tech_opportunity;
        tech_inf.textContent = problems;
        table_adres.style.visibility ='visible'; 

        
        

       

    }).then(()=>{
         req_form.style.visibility = 'visible';
    }).catch((error)=>{
        
        errors.textContent = "Адрес не найден!"
        setTimeout(() => {
            errors.textContent = ""
        }, timeout);
        
        
    })


});