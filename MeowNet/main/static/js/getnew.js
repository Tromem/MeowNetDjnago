document.getElementById('new-application').addEventListener('click',()=>{
    url_get_new_app = '/API/API-GET-NEW-APP/';
    const errormod = document.getElementById('errorinf');
    const errorwindow = document.getElementById('errors');
    fetch(url_get_new_app,{
        method:'POST'
    }).then(response => response.json())
        .then(data => {
            const container = document.getElementById('applications-container');
            
            console.log(container)

            
           

            if (data.error) {
                
                errormod.textContent = data.error;
                errorwindow.style.visibility = 'visible';
                
                setTimeout(() => { 
                    errorwindow.style.visibility = 'hidden';
                    errormod.textContent = ''; }, 3000);
                return
              if (container) {
                        while (container.firstChild) {
                        container.removeChild(container.firstChild);
                        }
}  
            }else if(data.notfound){
                
                
                errormod.textContent = data.notfound;
                 errorwindow.style.visibility = 'visible';
                container.innerHTML = `<div id="instructions" class="instructions">
            Перед началом смены необходимо нажать на иконку часов, чтобы зафиксировать время работы. 
            <br > Для подбора заявок нужно нажать на иконку плюсика, после чего система покажет доступные заявки для обработки. Если требуется информация по тарифам, нужно зайти на общий сайт компании 
            <br> Для поиска данных по адресу клиента следует нажать на иконку дома, ввести адрес и получить всю доступную информацию. 
            {%if user.user_acces >= 2 %}<br>Чтобы найти лицевой счет клиента, необходимо нажать на иконку человека и ввести номер лицевого счета. {%endif%}
            <br>Для закрытия заявки нужно изменить её статус на любой другой, кроме «Новая заявка». Во время работы важно внимательно проверять введенные данные и соблюдать конфиденциальность информации клиентов.
        </div>`
                 setTimeout(() => { 
                    errorwindow.style.visibility = 'hidden';
                    errormod.textContent = ''; }, 3000);
                    
                
            }

             
            if (Array.isArray(data.apps)) {
                data.apps.forEach(app => {
                    const fields = app.fields;
                    container.innerHTML = ''
                    // Создаем карточку
                    const card = document.createElement('div');
                    card.classList.add('application-card');
                    card.innerHTML = `
                        <div class="card-header">
                            <div class="card-id" id='card-id' value='${app.pk}'>ID:${app.pk}</div>
                            <div class="card-date">
                                <label for="app-date-${app.pk}">Дата создания:</label>
                                <input type="text" id="app-date-${app.pk}" value="${fields.data_create}" readonly>
                            </div>
                        </div>
                        <div class="card-body two-columns">
                            <div class="column left-column">
                                <div class="field">
                                    <label for="app-fullname-${app.pk}">ФИО:</label>
                                    <input type="text" id="app-fullname-${app.pk}" value="${fields.user}">
                                </div>
                                <div class="field">
                                    <label for="app-phone-${app.pk}">Телефон:</label>
                                    <input type="text" id="app-phone-${app.pk}" value="${fields.phone}">
                                </div>
                                <div class="field">
                                    <select id="app-status-${app.pk}">
                                        <option value="opt1" ${fields.application_status === 'opt1' ? 'selected' : ''}>Заявка заведена</option>
                                        <option value="opt2" ${fields.application_status === 'opt2' ? 'selected' : ''}>Неуспешно</option>
                                        <option value="opt3" ${fields.application_status === 'opt3' ? 'selected' : ''}>Новая заявка</option>
                                        <option value="opt4" ${fields.application_status === 'opt4' ? 'selected' : ''}>Доработка</option>
                                        <option value="opt5" ${fields.application_status === 'opt5' ? 'selected' : ''}>Юридическая заявка</option>
                                    </select>
                                     <div>Желаемая дата подключения:<input type="datetime-local" name="date_create" id="date_create"v}></div> 
                                     <div> Предыдущая дата: ${fields.Desired_date != null? fields.Desired_date:'Дата не была выбрана'}</div> 
                                    
                                </div>
                            </div>
                            <div class="column right-column">
                                <div class="field">
                                    <label for="app-passport-${app.pk}">Паспорт:</label>
                                    <input type="text" id="app-passport-${app.pk}" value="${fields.pasport || ''}" ${fields.pasport === null ? 'readonly' : ''}>
                                </div>
                                <div class="field">
                                    <label for="app-address-${app.pk}">Адрес:</label>
                                    <input type="text" id="app-address-${app.pk}" value="${fields.adres}">
                                </div>
                                <div class="field">
                                    <label for="app-comment-${app.pk}">Комментарий:</label>
                                    <textarea id="app-comment-${app.pk}">${fields.comment}</textarea>
                                </div>
                                <div class="field">
                                    <label for="app-plan-${app.pk}">Выбранный тариф:</label>
                                    <input type="text" id="app-plan-${app.pk}" value="${fields.tariffield}">
                                </div>
                            </div>
                        </div>
                        <div class="card-actions">
                           
                        </div>
                    `;

                    container.appendChild(card);
                });
            }
        }).then(()=>{
            try{

                document.getElementById('instructions').remove();
            }catch{
                console.log('');
            }
        })
        .catch(err => {
            console.error('Ошибка при получении заявок:', err);
        });
});