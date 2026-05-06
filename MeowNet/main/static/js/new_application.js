document.getElementById('make-new-app').addEventListener('click',()=>{
        
    const name = document.getElementById('name');
    const phone = document.getElementById('phone');
    const connection_type = document.getElementById('connection_type');
    const description = document.getElementById('description');
    const street = document.getElementById('street');
    const city = document.getElementById('city');
    const house = document.getElementById('house');
    const apartment = document.getElementById('apartment');
    const url = '/API/API-MAKE-APP-FROM-SELLER/'
    const req_form = document.getElementById('request-form');
    const errors = document.getElementById('errors')
    const timeout = 3000; 
    

    if(city.value == '' 
        || house.value == '' 
        ||apartment.value == ''
        || street.value == ''
        || name.value == '' 
        || phone.value == ''
        || connection_type.value ==''){
        errors.textContent ='У вас есть незаполеные поля!';
        setTimeout(()=>{errors.textContent = '';},timeout)
        return;
    }

    fetch(url,{
        method:"POST",
         headers:{
             'Content-Type': 'application/json'
        },
        body:JSON.stringify({
            'description':description.value,
            'name':name.value,
            'phone':phone.value,
            'adres':city.value + street.value + house.value + apartment.value,
            'OPTION':"opt2",
            'connection_type':connection_type.value

        })
    }).then(response => response.json().then(data =>{
        req_form.style.visibility = 'hidden';
        name.value = '';
        phone.value = '';
        description.value = '';
        connection_type.value = '';

    }));

});