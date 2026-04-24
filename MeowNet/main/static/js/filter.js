// Скрипт для фильтрации пользователей по ролям
document.addEventListener('DOMContentLoaded', function() {
    const roleFilter = document.getElementById('roleFilter'); 
    const tableRows = document.querySelectorAll('table tbody tr'); 

    // Обработчик изменения фильтра
    roleFilter.addEventListener('change', function() {
        const selectedRole = roleFilter.value; 

        // Перебираем все строки таблицы
        tableRows.forEach(row => {
            const roleCell = row.querySelector('select'); 
            const role = roleCell ? roleCell.value : ''; 

            // Если выбранный фильтр пустой (Все), показываем все строки
            if (selectedRole === '' || selectedRole === role) {
                row.style.display = ''; 
            } else {
                row.style.display = 'none'; 
            }
        });
    });
});