// Короче в этом файле сделай обработчик нажатий трех кнопок где будут отправляться данные из полей, нейронка ебаная не хочет думай думай сам , потом попытайся доделать профиль и можешь начинать делать бумажную часть
//Так же можно что нить засунуть в общие настройки 

// Функция для получения CSRF токена из формы
function getCSRFToken() {
    const tokenInput = document.querySelector('[name=csrfmiddlewaretoken]');
    return tokenInput ? tokenInput.value : '';
};

function addtarif(){
    const addbuttontarif =  document.getElementById('addbuttontarif');
    addbuttontarif.addEventListener('click',()=>{
        const nametarif = document.getElementById('add-nametarif');
        const price = document.getElementById('add-price');
        const price_to_connect = document.getElementById('add-price_to_connect');
        const discounts = document.getElementById('add-discounts');
        const time_to_end_discount = document.getElementById('add-time_to_end_discount');
        const Mounts_discount = document.getElementById('add-Mounts_discount');
        const speed = document.getElementById('add-speed');
        const tv_chanels = document.getElementById('add-tv_chanels');
        const typetarif = document.getElementById('add-typetarif');
        if(nametarif.value == '' || price.value == '' || price_to_connect.value == '' ||speed.value == '' ||tv_chanels.value == '' || typetarif.value == ''  ){
            alert('Заполните все поля!');
            return
        };
        const url = '/API/API-TARIF-WORKER/';
        fetch(url,{
            method:'POST',
            headers:{
                'content-type':'application/json',
                'X-CSRFToken':getCSRFToken()
            },
            body:JSON.stringify({
                'nametarif':nametarif.value,
                'price': price.value,
                'price_to_connect': price_to_connect.value,
                'discounts': discounts.value,
                'time_to_end_discount': time_to_end_discount.value,
                'Mounts_discount': Mounts_discount.value,
                'speed': speed.value,
                'tv_chanels': tv_chanels.value,
                'typetarif': typetarif.value,
            }),
        }).then(response => response.json()).then(data=>{
            if (data.error){
                console.log(data.error)
            };
        }).then(()=>{
            nametarif.value = '';
            price.value = '';
            price_to_connect.value = '';
            discounts.value = '';
            time_to_end_discount.value = '';
            Mounts_discount.value = '';
            speed.value = '';
            tv_chanels.value = '';
            typetarif.value = 1;
        });
        
        

    });
              


};
function changetarif(){
    const changebuttontarif =  document.getElementById('changebuttontarif');
    changebuttontarif.addEventListener('click',()=>{
        const change_tarif_id = document.getElementById('change-tarif_id');
        const nametarif = document.getElementById('change-nametarif');
        const price = document.getElementById('change-price');
        const price_to_connect = document.getElementById('change-price_to_connect');
        const discounts = document.getElementById('change-discounts');
        const time_to_end_discount = document.getElementById('change-time_to_end_discount');
        const Mounts_discount = document.getElementById('change-Mounts_discount');
        const speed = document.getElementById('change-speed');
        const tv_chanels = document.getElementById('change-tv_chanels');
        const typetarif = document.getElementById('change-typetarif');
        
        const url = '/API/API-TARIF-WORKER/';
        fetch(url,{
            method:'PATCH',
            headers:{
                'content-type':'application/json',
                'X-CSRFToken':getCSRFToken()
            },
            body:JSON.stringify({
                'change_tarif_id':change_tarif_id.value,
                'nametarif':nametarif.value,
                'price': price.value,
                'price_to_connect': price_to_connect.value,
                'discounts': discounts.value,
                'time_to_end_discount': time_to_end_discount.value,
                'Mounts_discount': Mounts_discount.value,
                'speed': speed.value,
                'tv_chanels': tv_chanels.value,
                'typetarif': typetarif.value,
            }),
        }).then(response => response.json()).then(data=>{
            if (data.error){
                alert(data.error)
            };
        }).then(()=>{
            nametarif.value = '';
            price.value = '';
            price_to_connect.value = '';
            discounts.value = '';
            time_to_end_discount.value = '';
            Mounts_discount.value = '';
            speed.value = '';
            tv_chanels.value = '';
            typetarif.value = 1;
        
        });

    });
};
function achivetarif(){
    const delbuttontarif = document.getElementById('delbuttontarif');
    const addbuttonarchive = document.getElementById('addacrhive');
    const del_id = document.getElementById('del-id');
    delbuttontarif.addEventListener('click',()=> ajaxtarif(true,del_id));
    addbuttonarchive.addEventListener('click',()=> ajaxtarif(false,del_id));
}

function ajaxtarif(type,del_id){
        
        console.log(type)
        const url = '/API/API-TARIF-WORKER/';
        fetch(url,{
            method:'DELETE',
            headers:{
                'content-type':'application/json',
                'X-CSRFToken':getCSRFToken()
            },
            body:JSON.stringify({
                'typework':type,
                'tarif-id':del_id.value

            }),
        }).then(response => response.json()).then(data=>{
            if (data.error){
                alert(data.error)
            };
        }).then(()=>{

        })
}

addtarif()
achivetarif()
changetarif()