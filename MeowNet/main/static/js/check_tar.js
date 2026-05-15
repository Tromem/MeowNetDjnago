document.addEventListener('DOMContentLoaded',()=>{
    const tarif_active = document.getElementById('tarif-act')
    if (tarif_active.textContent = 'True'){
        tarif_active.textContent = 'Активна';
    }else{
        tarif_active.textContent = 'Недостаточно средств';
    };
});