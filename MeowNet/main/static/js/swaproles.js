const buttonsswap = document.querySelectorAll(".button-submit-swap");
const url = '/API/API-SWAP-ROLE/';
buttonsswap.forEach(btn=>{
    const checkEl = document.getElementById(`swap-user-select-${btn.value}`).value;
    btn.addEventListener('click',()=>{
       const optionEL = document.getElementById(`swap-user-select-${btn.value}`).value;
       const UserIdForSwap = btn.value;
        if(optionEL != checkEl){

            fetch(url,{
                method:'POST',
                headers:{
                    'Content-Type': 'application/json'
                },
                body:JSON.stringify({
                    'acces_swap': optionEL,
                    'userid': parseInt(UserIdForSwap)
                })
            })
        }
    })
    
});