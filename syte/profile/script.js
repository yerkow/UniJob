// Пример: обработка клика по "Добавить проект"

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
document.addEventListener('DOMContentLoaded', function() {
    // Получаем email из куки
    const email = getCookie('email');
    if (email) {
        fetch(`/sprofile/data?email=${encodeURIComponent(email)}`)
            .then(response => response.json())
            .then(data => {
                if (!data.error) {
                    // Пример: вставить данные в поля профиля
                    if (data.gpa) document.querySelector('input[placeholder="Зарплата"]').value = data.gpa;
                    if (data.full_name) document.querySelector('textarea[placeholder="Расскажите о себе..."]').value = data.full_name;
                    if (data.achievements) document.querySelector('textarea[placeholder="Продайте себя..."]').value = data.achievements;
                    // Добавь другие поля по аналогии
                }
            });
    }

    // Пример: обработка клика по "Добавить проект"
    document.querySelectorAll('.add-btn').forEach(function(btn) {
        btn.onclick = function() {
            alert('Здесь будет форма добавления!');
        };
    });
});