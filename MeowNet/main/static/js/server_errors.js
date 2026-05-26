document.addEventListener('DOMContentLoaded', () => {

    // ---------- Сохранение статуса сервера ----------
    const saveButton = document.getElementById('save-server-status');
    saveButton.addEventListener('click', async () => {
        const status = document.getElementById('status').value;
        const techInf = document.getElementById('Tech_inf').value;
        const forWho = document.getElementById('for_who').value;
        const timeToEnd = document.getElementById('time_to_end').value;

        // Проверка на заполненность
        if (!status || !techInf || !timeToEnd) {
            alert('Пожалуйста, заполните все обязательные поля для сохранения статуса!');
            return;
        }

        try {
            const response = await fetch('/API/server-status/update/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({
                    status: status === 'True',
                    Tech_inf: techInf,
                    for_who: forWho,
                    time_to_end: timeToEnd
                })
            });

            const data = await response.json();

            if (response.ok && data.success) {
                alert('Статус сервера успешно обновлён!');
            } else {
                alert('Ошибка: ' + (data.error || 'Не удалось сохранить статус'));
            }

        } catch (err) {
            alert('Ошибка запроса: ' + err);
        }
    });

    // ---------- Удаление выбранных отключений ----------
    const resetButton = document.getElementById('reset-selected');
    resetButton.addEventListener('click', async () => {
        const checkboxes = document.querySelectorAll('input[name="reset_ids"]:checked');
        if (!checkboxes.length) {
            alert('Выберите хотя бы одно отключение для удаления!');
            return;
        }

        const ids = Array.from(checkboxes).map(cb => cb.value);

        try {
            const response = await fetch('/API/server-status/reset-selected/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ ids: ids })
            });

            const data = await response.json();

            const resultDiv = document.getElementById('reset-result');

            if (response.ok && data.success) {
                resultDiv.style.color = 'green';
                resultDiv.textContent = 'Выбранные отключения успешно удалены!';

                // Удаляем строки из таблицы
                ids.forEach(id => {
                    const row = document.querySelector(`input[value="${id}"]`).closest('tr');
                    if (row) row.remove();
                });

            } else {
                resultDiv.style.color = 'red';
                resultDiv.textContent = 'Ошибка: ' + (data.error || 'Не удалось удалить отключения');
            }

        } catch (err) {
            alert('Ошибка запроса: ' + err);
        }
    });

    // ---------- Функция для получения CSRF токена ----------
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let cookie of cookies) {
                cookie = cookie.trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

});