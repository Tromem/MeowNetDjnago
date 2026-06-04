document.getElementById('changepassword-button').addEventListener('click',()=>{
    const password = document.getElementById('new-password');
    const login = document.getElementById('changepassword-select');
    const url = '/API/API-Change-Password-worker/';

    fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        newpassword: password.value,
        login: login.value
    })
})
.then(response => response.json())
.then(data => {
    password.value = '';
    make_message("Пароль успешно заменен!");
})
.catch(error => {
    console.error('Ошибка:', error);
    make_message("Ошибка при смене пароля");
});
});
document.getElementById('edituser-button').addEventListener('click',()=>{
    const lastName = document.getElementById('edit-fullname');
    const login = document.getElementById('edituser-select');
    const url = '/API/API-Change-Name/';

   fetch(url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        newlastName: lastName.value,
        login: login.value
    })
})
.then(response => response.json())
.then(data => {
    lastName.value = '';

    make_message("ФИО сотрудника успешно изменено!");
})
.catch(error => {
    console.error(error);
});
})