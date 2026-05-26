
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('phoneSearchForm');
    const phoneInput = document.getElementById('phone');

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        let phone = phoneInput.value.trim();
        if (phone.startsWith('8')) {
            phone = phone.substring(1);
        } else if (phone.startsWith('7')) {
            phone = phone.substring(1);
        }

        // Удаляем пробелы, скобки и тире
        phone = phone.replace(/\D/g, '');

        if (!phone) {
            alert('Введите номер телефона');
            return;
        }

        // Переброс на страницу поиска
        // Пример: /applications/79991234567/
        window.location.href =`phones?phone=${phone}`;
    });
});
// Переделай на переброс в эту же страницу и что бы были там заявки 