document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('tab-main').onclick = function() {
        document.getElementById('tab-main-content').style.display = '';
        document.getElementById('tab-resume-content').style.display = 'none';
        this.style.borderBottom = '2px solid #4a90e2';
        this.style.color = '#4a90e2';
        document.getElementById('tab-resume').style.borderBottom = 'none';
        document.getElementById('tab-resume').style.color = '#444';
    };
    document.getElementById('tab-resume').onclick = function() {
        document.getElementById('tab-main-content').style.display = 'none';
        document.getElementById('tab-resume-content').style.display = '';
        this.style.borderBottom = '2px solid #4a90e2';
        this.style.color = '#4a90e2';
        document.getElementById('tab-main').style.borderBottom = 'none';
        document.getElementById('tab-main').style.color = '#444';
    };

    // Обработка отправки формы резюме
    const resumeForm = document.getElementById('resume-form');
    if (resumeForm) {
        resumeForm.addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Резюме успешно сохранено!');
            // Здесь можно добавить отправку данных на сервер через fetch/AJAX
        });
    }
});

