
document.querySelector(".save-btn").addEventListener("click", async function (e) {
    e.preventDefault();

    // собираем все input'ы
    const inputs = document.querySelectorAll(".input-user");

    const data = {
        full_name: inputs[0].value,
        phone: inputs[1].value,
        address: inputs[2].value,
        new_password: inputs[3].value
    };

    try {
        const response = await fetch("/API/api-change-settings/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data)
        }).then(()=>{
            make_message("Ваши данные успешно изменены!")
        });

        const result = await response.json();
        console.log("Ответ сервера:", result);

    } catch (error) {
        console.error("Ошибка запроса:", error);
    }
});
