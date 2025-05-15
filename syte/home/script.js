// Пример переключения вкладок (Вакансии/События/Резюме)
document.addEventListener('DOMContentLoaded', function() {
    const btns = document.querySelectorAll('.tab-btn');
    btns.forEach(btn => {
        btn.addEventListener('click', function() {
            btns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            // Здесь можно добавить логику отображения нужного блока
        });
    });

    // User menu logic
    const userMenuBtn = document.getElementById('userMenuBtn');
    const userMenu = document.getElementById('userMenu');
    document.addEventListener('click', function(e) {
        if (userMenuBtn.contains(e.target)) {
            userMenu.classList.toggle('active');
        } else if (!userMenu.contains(e.target)) {
            userMenu.classList.remove('active');
        }
    });
});