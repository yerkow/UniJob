document.addEventListener("DOMContentLoaded", () =>{

    const loginForm = document.getElementById("login-form")
    const registerForm = document.getElementById("register-form")
    const message = document.getElementById("message")
    const showLogin = document.getElementById("show-login")
    const showRegist = document.getElementById("show-register")
    const loginBtn = document.getElementById("login-btn")
    const regBtn = document.getElementById('register-btn')
    const userBtn = document.getElementById("tab-user")
    const orgBtn = document.getElementById('tab-org')

    userBtn.addEventListener('click', () =>{
        userBtn.classList.add('active')
        orgBtn.classList.remove('active')
    })

    orgBtn.addEventListener('click', () =>{
        orgBtn.classList.add('active')
        userBtn.classList.remove('active')
    })

    showLogin.addEventListener('click', () =>{
        registerForm.classList.add("hidden")
        loginForm.classList.remove("hidden")
    })

    showRegist.addEventListener('click', () =>{
        loginForm.classList.add("hidden")
        registerForm.classList.remove("hidden")
    })

    document.getElementById("register-btn").addEventListener("click", async () => {
        const email = document.getElementById("reg-email").value;
        const password = document.getElementById("reg-password").value;
        const config_password = document.getElementById("reg-password2").value;
        const name = document.getElementById("reg-name").value;
        const surname = document.getElementById("reg-surname").value;
        const reg_type = document.querySelector(".tab-btn.active").id === "tab-user" ? "user" : "org";

        if (password !== config_password) {
            showMessage("Пароли не совпадают", "error");
            return;
        }

        const response = await fetch("/api/register", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password, config_password, name, surname, type: reg_type })
        });

        const data = await response.json();
        if (!response.ok) {
            showMessage(data.detail || "Ошибка регистрации", "error");
        } else {
            showMessage("Регистрация успешна. Проверьте почту для подтверждения.", "success");
        }
    });

    document.getElementById("login-btn").addEventListener("click", async () => {
        const email = document.getElementById("login-email").value;
        const password = document.getElementById("login-password").value;

        const response = await fetch("/api/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();
        if (!response.ok) {
            showMessage(data.detail || "Неверные данные", "error");
        } else {
            window.location.href = "/sprofile";
        }
    });

    function showMessage(text, type) {
        message.textContent = text;
        message.className = `message ${type} visible`;
        setTimeout(() => {
            message.className = "message hidden";
        }, 3000);
    }

    // document.getElementById('github-login').onclick = function() {
    //     window.location.href = '/auth/github/login?type=' + 
    //         (document.getElementById('tab-org').classList.contains('active') ? 'org' : 'user');
    // };

    // document.getElementById('github-register').onclick = function() {
    //     window.location.href = '/auth/github/login?type=' + 
    //         (document.getElementById('tab-org').classList.contains('active') ? 'org' : 'user');
    // };
})