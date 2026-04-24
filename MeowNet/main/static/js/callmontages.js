// Получаем элементы модального окна и кнопки
const modal = document.getElementById("installerModal");
const btn = document.getElementById("requestInstallerBtn");
const closeModal = document.getElementById("closeModal");

// Открытие модального окна
btn.onclick = function() {
    modal.style.display = "block";
}

// Закрытие модального окна
closeModal.onclick = function() {
    modal.style.display = "none";
}

// Закрытие модального окна при клике вне окна
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Обработка отправки заявки
document.getElementById('installerForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('installerName').value;
    const phone = document.getElementById('installerPhone').value;
    const description = document.getElementById('installerDescription').value;
    const adres = document.getElementById('adres').value;
    const problem = document.getElementById('problem').value;
    console.log(problem)
    url = '/API/API-POST-Application/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body:JSON.stringify({
                        'name':name ,
                        'phone':phone ,
                        'description':description ,
                        'adres':adres ,
                        'opt':'opt2',
                        'problem':parseInt(problem),
                    })
    })

    modal.style.display = "none";

    // Вывод сообщения или отправка на сервер
    alert("Ваша заявка на вызов монтажника отправлена!");
});