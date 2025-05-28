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
    function applyFilters() {
      const search = document.getElementById("searchInput").value.toLowerCase();
      const city = document.getElementById("cityFilter").value;
    
      const cards = document.querySelectorAll(".vacancy-card");
    
      cards.forEach(card => {
        const title = card.getAttribute("data-title").toLowerCase();
        const cardCity = card.getAttribute("data-city");
    
        const matchesSearch = title.includes(search);
        const matchesCity = city === "" || cardCity === city;
    
        if (matchesSearch && matchesCity) {
          card.classList.add("show");
        } else {
          card.classList.remove("show");
        }
      });
    }
    
    // Вызываем поиск при загрузке для отображения всех вакансий
    window.onload = applyFilters;
});
