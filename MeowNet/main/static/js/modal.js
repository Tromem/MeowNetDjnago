document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('buy-modal');
    const closeBtn = document.getElementById('modal-close');
    const buyButtons = document.querySelectorAll('.card-buy-btn');
    

    const modalType = document.querySelector('.modal-card-type');
    const modalName = document.querySelector('.modal-card-name');
    const modalSpeed = document.querySelector('.modal-card-speed-text');
    const modalPrice = document.querySelector('.modal-card-price');
    

    // Открытие модального окна при клике на кнопку «Купить»
    buyButtons.forEach(button => {
        button.addEventListener('click', () => {
            const card = button.closest('.card');
            const buttonmod = document.getElementById('modal-buy-btn');
            buttonmod.value = button.value;
            // Копируем данные с карточки в модальное окно
            modalType.textContent = card.querySelector('.card-type').textContent;
            modalName.textContent = card.querySelector('.card-name').textContent;
            modalSpeed.textContent = card.querySelector('.card-speed span').textContent;
            modalPrice.textContent = card.querySelector('.card-price').textContent;

            modal.style.display = 'block';
        });
    });

    // Закрытие при клике на крестик
    closeBtn.addEventListener('click', () => {
        modal.style.display = 'none';
    });

    // Закрытие при клике на фон
    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.style.display = 'none';
        }
    });

    
});

const button_mod = document.getElementById('modal-buy-btn');
const modal = document.getElementById('buy-modal'); 
    button_mod.addEventListener('click', (e) => {
        e.preventDefault();
        const url = '/API/API-POST-Application/';
        const phone = document.getElementById('user-phone');
        const name = document.getElementById('user-name');
        const adres = document.getElementById('Adres-user');
        const connection_type = document.getElementById('modal-buy-btn');
        
        fetch(url,{
            method:"POST",
            headers:{'content-type':'application/json'},
            body:JSON.stringify({
                'description':'Хочу подключить интернет',
                'name':name.value,
                'phone':phone.value,
                'adres':adres.value,
                'opt':"opt3",
                'connection_type':connection_type.value,
                'tarif':button_mod.value
            })
        })
        modal.style.display = 'none';
        
    });