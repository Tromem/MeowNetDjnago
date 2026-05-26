document.getElementById('openModalBtn').onclick = function() {
    document.getElementById('createAppModal').style.display = 'block';
}

document.getElementById('closeModalBtn').onclick = function() {
    document.getElementById('createAppModal').style.display = 'none';
}

window.onclick = function(event) {
    if (event.target == document.getElementById('createAppModal')) {
        document.getElementById('createAppModal').style.display = 'none';
    }
}

document.getElementById('modalSaveBtn').onclick = function() {
    const data = {
        user: document.getElementById('modal-fullname').value,
        phone: document.getElementById('modal-phone').value,
        application_status: document.getElementById('modal-status').value,
        Desired_date: document.getElementById('modal-date_create').value,
        pasport: document.getElementById('modal-passport').value,
        adres: document.getElementById('modal-address').value,
        comment: document.getElementById('modal-comment').value,
        tariffield: document.getElementById('modal-plan').value,
        problem: document.getElementById('modal-problem').value 
    };
    for (let key in data) {
    if (!data[key] || data[key].trim() === "") {
        alert("Заполните все поля!");
        return;
    }
}

    console.log("Данные новой заявки:", data);

    document.getElementById('createAppModal').style.display = 'none';
    const url_new_app = '/API/Add-app-worker/';

    fetch(url_new_app,{
        method:'POST',
        headers:{'Content-type':'json/application'},
        body:JSON.stringify(data)
    }).then(response=>response.json()).then( data=>{
        window.location.reload()
    });
}