const buttonfind = document.getElementById('find').addEventListener('click',()=>{
    const findfield = document.getElementById('accountNumber').value;
    const find_table = document.getElementById('table-user-inf');
    const errors = document.getElementById('errors');
    if (find_table){
        
        find_table.remove();
    }
    
    if(findfield != '' && parseInt(findfield) && findfield.length == 12){

        const url = '/API/API-GET-USER/';
        fetch(
            url,
            {
                method:'POST',
                headers:{
                        'Content-Type': 'application/json'
                    },
                    body:JSON.stringify({
                        'id': findfield
                    })
            }
        ).then().then(response => response.json()).then(data => {
            if(data.username == undefined){
                errors.textContent = 'Пользователь не был найден!';
            setTimeout(()=>{
                errors.textContent = '';
            },3000)
                return;};
            const container = document.getElementById('accountDetails');
            container.style.display = 'block';
           
            let table = document.createElement('table');
            table.id = 'table-user-inf'
            container.appendChild(table);
           
            console.log(data.username)
            table.appendChild(createTableRow('ФИО',data.userlastname));
            table.appendChild(createTableRow('Логин', data.username ));
            table.appendChild(createTableRow('Номер телефона',data.numberphone ));
            table.appendChild(createTableRow('Паспортные данные',data.pasport ));
            table.appendChild(createTableRow('Адрес',data.address ));
            table.appendChild(createTableRow('Баланс',`${data.balance}руб` ));
            table.appendChild(createTableRow('Тариф', data.usertarif ));
            
            const installerName = document.getElementById('installerName');
            const adres = document.getElementById('adres');
            const installerPhone = document.getElementById('installerPhone');
            const installerDescription = document.getElementById('installerDescription');
           
            installerName.value = data.userlastname;
            adres.value = data.address;
            installerPhone.value = data.numberphone;
    
            
            
        })
    }
    
});

function createTableRow(headerText, contentText) {
    let row = document.createElement('tr');
    
    let th = document.createElement('th');
    th.textContent = headerText;
    
    let td = document.createElement('td');
    td.textContent = contentText;
    
    row.appendChild(th);
    row.appendChild(td);
    return row;
}

