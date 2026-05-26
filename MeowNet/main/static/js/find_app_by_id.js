

const input = document.getElementById('searchInput');
const url_find_app = '/API/API-FIND-APP/';

input.addEventListener('keydown',(event)=>{
    if(event.key ==='Enter'){
        
        fetch(url_find_app,{
            method:'POST',
            headers:{
                 'Content-Type': 'application/json'
            },
            body:JSON.stringify({
                id:input.value
            })
        }).then(response => response.json()).then(data=>{
            if(data.error){
                alert(data.error)
                return
            }
            container = document.getElementById('applications-container');
            const card = document.createElement('div')
            card.classList.add('application-card');
            card.innerHTML = `
                        <div class="card-header">
                            <div class="card-id" id='card-id' value="${data.app.pk}">ID: ${data.app.pk}</div>
                            <div class="card-date">
                                <label for="app-date-${data.app.pk}">Дата создания:</label>
                                <input type="text" id="app-date-${data.app.pk}" value="${data.app.data_create}" readonly>
                            </div>
                        </div>
                        <div class="card-body two-columns">
                            <div class="column left-column">
                                <div class="field">
                                    <label for="app-fullname-${data.app.pk}">ФИО:</label>
                                    <input type="text" id="app-fullname-${data.app.pk}" value="${data.app.user}">
                                </div>
                                <div class="field">
                                    <label for="app-phone-${data.app.pk}">Телефон:</label>
                                    <input type="text" id="app-phone-${data.app.pk}" value="${data.app.phone}">
                                </div>
                                <div class="field">
                                    <select id="app-status-${data.app.pk}">
                                        <option value="opt1" ${data.app.application_status === 'opt1' ? 'selected' : ''}>Заявка заведена</option>
                                        <option value="opt2" ${data.app.application_status === 'opt2' ? 'selected' : ''}>Неуспешно</option>
                                        <option value="opt3" ${data.app.application_status === 'opt3' ? 'selected' : ''}>Новая заявка</option>
                                        <option value="opt4" ${data.app.application_status === 'opt4' ? 'selected' : ''}>Доработка</option>
                                        <option value="opt5" ${data.app.application_status === 'opt5' ? 'selected' : ''}>Юридическая заявка</option>
                                    </select>
                                    <div>Желаемая дата подключения:<input type="datetime-local" name="date_create" id="date_create"v}></div> 
                                    <div > Предыдущая дата: ${data.app.Desired_date != null? data.app.Desired_date:'Дата не была выбрана'}</div>
                                </div>
                            </div>
                            <div class="column right-column">
                                <div class="field">
                                    <label for="app-passport-${data.app.pk}">Паспорт:</label>
                                    <input type="text" id="app-passport-${data.app.pk}" value="${data.app.pasport || ''}" ${data.app.pasport === null ? 'readonly' : ''}>
                                </div>
                                <div class="field">
                                    <label for="app-address-${data.app.pk}">Адрес:</label>
                                    <input type="text" id="app-address-${data.app.pk}" value="${data.app.adres}">
                                </div>
                                <div class="field">
                                    <label for="app-comment-${data.app.pk}">Комментарий:</label>
                                    <textarea id="app-comment-${data.app.pk}">${data.app.comment}</textarea>
                                </div>
                                <div class="field">
                                    <label for="app-plan-${data.app.pk}">Выбранный тариф:</label>
                                    <input type="text" id="app-plan-${data.app.pk}" value="${data.app.tariffield}">
                                </div>
                            </div>
                        </div>
                        <div class="card-actions">
                            
                        </div>
                    `;

                    container.appendChild(card);
        }).then(()=>{
                window.location.reload()
                const instr = document.getElementById('instructions')
                if(instr){
                    instr.remove();
                }
            
        })
    };
})