
document.addEventListener('DOMContentLoaded', () => {
    // Функция отправки обновленных данных
    function updateCard(id, data) {
        fetch(`/API/API-UPDATE-APLICATION/${id}/`, {  
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') 
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (!response.ok) throw new Error('Ошибка обновления данных');
            return response.json();
        })
        .then(result => {
            document.querySelectorAll('.application-card').forEach(card=>{
                let status_card = card.querySelector('#app-status').value
                switch (status_card){
    case 'opt1':
        card.style.backgroundColor = 'rgb(180, 180, 255)'
        break;
    case 'opt2':
        card.style.backgroundColor = 'rgba(255, 140, 140, 0.6)'
        break;
    case 'opt3':
        card.style.backgroundColor = 'rgb(245, 245, 245)'
        break;
    case 'opt4':
        card.style.backgroundColor = 'rgba(170, 170, 170, 0.45)'
        break;
    case 'opt5':
        card.style.backgroundColor = 'rgba(140, 230, 150, 0.5)'
        break;
}
            })
            console.log('Данные успешно обновлены:', result);
            
        })
        .catch(error => {
            console.error('Ошибка при обновлении:', error);
        });
    }

    // Получаем все карточки
    document.querySelectorAll('.application-card').forEach(card => {
        const rawid = card.querySelector('#card-id').textContent;
        const id = rawid.replace('ID:','').trim();
        
        // Слежение за изменениями всех полей input, select, textarea
        card.querySelectorAll('input, select, textarea').forEach(input => {
            input.addEventListener('change', () => {
                 
                const data = {
                    user: card.querySelector('#app-fullname').value,
                    phone: card.querySelector('#app-phone').value,
                    application_status: card.querySelector('#app-status').value,
                    date_create: card.querySelector('#date_create').value,
                    pasport: card.querySelector('#app-passport').value,
                    adres: card.querySelector('#app-address').value,
                    comment: card.querySelector('#app-comment').value,
                    tariffield: card.querySelector('#app-plan').value
                };
                updateCard(id, data);
            });
        });
    });

    // Функция получения CSRF токена для Django
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
