document.addEventListener('DOMContentLoaded', () => {
    const select = document.getElementById('users-app');
    const cards = document.querySelectorAll('.application-card');

    select.addEventListener('change', () => {
        const selectedUserId = select.value;

        cards.forEach(card => {
            const ownerId = card.getAttribute('data-owner-id');

            if (!selectedUserId || selectedUserId === ownerId) {
                card.style.display = 'block'; // показываем
            } else {
                card.style.display = 'none'; // скрываем
            }
        });
    });
});

const buttons = document.querySelectorAll('.save-btn');

    buttons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const appId = btn.value; // забираем id заявки
            console.log('Нажата кнопка заявки с ID:', appId);
            const csrftoken = getCookie('csrftoken');
            
            fetch(window.location.href, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken // CSRF для Django
                },
                body: JSON.stringify({id: appId})
            })
        });
    });

    function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}