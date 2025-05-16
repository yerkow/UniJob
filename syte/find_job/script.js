// Пример переключения вкладок
document.addEventListener('DOMContentLoaded', function() {
    const tabBtns = document.querySelectorAll('.tab-btn');
    tabBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            tabBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            // Здесь можно добавить логику отображения нужного блока
        });
    });

    // Пример реакции на кнопку "Откликнуться"
    const applyBtns = document.querySelectorAll('.apply-btn');
    applyBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            alert('Вы откликнулись на вакансию!');
        });
    });

    // Пример фильтрации по поиску
    const searchInput = document.querySelector('.search-bar input');
    const jobCards = document.querySelectorAll('.job-card');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const value = this.value.toLowerCase();
            jobCards.forEach(card => {
                const title = card.querySelector('.job-title').textContent.toLowerCase();
                card.style.display = title.includes(value) ? '' : 'none';
            });
        });
    }
});