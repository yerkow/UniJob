document.addEventListener('DOMContentLoaded', function() {

    // 1. Получение элементов DOM
    // --- Модальное окно фильтров ---
    const filterModal = document.getElementById('filterModal');
    const openFiltersBtn = document.getElementById('openFiltersBtn');
    const closeFiltersBtn = document.getElementById('closeFiltersBtn');
    const applyFiltersBtn = document.getElementById('applyFiltersBtn');
    const resetFiltersBtn = document.getElementById('resetFiltersBtn');

    // --- Фильтры и поиск ---
    const searchBtn = document.getElementById('searchBtn');
    const searchInput = document.getElementById('searchInput');
    const regionFilter = document.getElementById('regionFilter');
    const cityFilter = document.getElementById('cityFilter');
    const expFilter = document.getElementById('expFilter');
    const educationLevelFilter = document.getElementById('educationLevelFilter');
    const educationAreaFilter = document.getElementById('educationAreaFilter');
    const directionNameFilter = document.getElementById('directionNameFilter');
    const genderFilter = document.getElementById('genderFilter');
    const studentsList = document.getElementById('studentsList');
    const skillsMultiSelect = document.getElementById('skillsMultiSelect');
    const languagesMultiSelect = document.getElementById('languagesMultiSelect');
    const specializationMultiSelect = document.getElementById('specializationMultiSelect');
    const aiReasoningBox = document.getElementById('aiReasoning');
    const aiReasoningToggle = document.getElementById('aiReasoningToggle');
    const aiReasoningToggleIcon = document.getElementById('aiReasoningToggleIcon');
    const loader = document.getElementById('.loader')

    // 2. Опции для мультиселектов
    const skillsOptions = [
        "JavaScript", "Python", "Java", "C++", "C#", "PHP", "HTML", "CSS", "SQL", "TypeScript",
        "React", "Vue.js", "Angular", "Node.js", "Express.js", "Django", "Flask", "Spring", "Kotlin",
        "Swift", "Objective-C", "Go", "Ruby", "Perl", "Scala", "Rust", "MATLAB", "R", "SAS",
        "Excel", "Word", "PowerPoint", "Outlook", "1C", "Бухгалтерия", "Продажи", "Маркетинг",
        "SEO", "SMM", "Копирайтинг", "UX/UI дизайн", "Графический дизайн", "Figma", "Adobe Photoshop",
        "Adobe Illustrator", "3ds Max", "AutoCAD", "SolidWorks", "Project Management", "Teamwork",
        "Коммуникация", "Публичные выступления", "Критическое мышление", "Аналитика", "Data Science",
        "Machine Learning", "Big Data", "DevOps", "Git", "Docker", "Kubernetes", "Linux", "Windows",
        "Тестирование ПО", "QA", "Jira", "Agile", "Scrum", "Быстрое обучение", "Самоорганизация",
        "Внимательность", "Ответственность", "Лидерство", "Работа в команде", "Планирование",
        "Управление временем", "Стрессоустойчивость", "Обучаемость", "Креативность", "Решение проблем",
        "Ведение переговоров", "Финансовый анализ", "Прототипирование", "Веб-дизайн", "Мобильная разработка",
        "Soft Skills", "Photoshop", "Illustrator", "Вокал", "Фотография", "Английский"
    ];
    const languagesOptions = [
        "Английский язык", "Русский язык", "Казахский язык", "Китайский язык", "Немецкий язык",
        "Французский язык", "Испанский язык", "Итальянский язык", "Турецкий язык", "Корейский язык",
        "Японский язык", "Польский язык", "Чешский язык", "Арабский язык", "Португальский язык",
        "Узбекский язык", "Татарский язык", "Украинский язык", "Белорусский язык", "Грузинский язык",
        "Английский (A1)", "Английский (A2)", "Английский (B1)", "Английский (B2)", "Английский (C1)", "Английский (C2)",
        "Русский (родной)", "Казахский (родной)", "Китайский (HSK4)", "Немецкий (B1)", "Французский (B2)",
        "Казахский C2", "Русский C2", "Английский B2", "Английский B1", "Английский C1"
    ];
    const specializationOptions = [
        "Web-разработка", "Frontend", "Backend", "Fullstack", "Data Science", "Machine Learning",
        "Графический дизайн", "UX/UI дизайн", "Мобильная разработка", "Android", "iOS", "DevOps",
        "Системное администрирование", "Бухгалтерия", "Финансы", "Экономика", "Маркетинг", "SMM",
        "SEO", "Копирайтинг", "Перевод", "Педагогика", "Психология", "Юриспруденция", "Медицина",
        "Фармация", "Химия", "Биология", "Физика", "Математика", "Логистика", "Менеджмент",
        "Проектный менеджмент", "HR", "Рекрутинг", "PR", "Журналистика", "Фотография", "Видеомонтаж",
        "Музыка", "Вокал", "Изобразительное искусство", "Дизайн интерьера", "Архитектура", "Строительство",
        "Информационная безопасность", "Кибербезопасность", "Тестирование ПО", "QA", "GameDev", "3D-моделирование",
        "Бизнес-аналитика", "Продажи", "Работа с клиентами", "Техническая поддержка", "Аналитика данных",
        "Инженерия", "Электроника", "Мехатроника", "Робототехника", "Промышленный дизайн",
        "Математика", "Frontend", "Графический дизайн", "Английский язык", "Менеджмент", "Вокал", "Data Science", "Фотография"
    ];

    // 3. Универсальный компонент мультивыбора и инициализация мультиселектов
    function createMultiSelect(containerId, options, placeholderText) {
        const container = document.getElementById(containerId);
        container.innerHTML = `
            <div class="selected-list"></div>
            <input type="text" class="multi-input" placeholder="${placeholderText}">
            <div class="options-list" style="display:none"></div>
        `;
        const selectedList = container.querySelector('.selected-list');
        const input = container.querySelector('.multi-input');
        const optionsList = container.querySelector('.options-list');
        let selected = [];

        function renderSelected() {
            selectedList.innerHTML = '';
            selected.forEach(val => {
                const tag = document.createElement('span');
                tag.className = 'selected-tag';
                tag.textContent = val;
                const remove = document.createElement('button');
                remove.textContent = '×';
                remove.onclick = () => {
                    selected = selected.filter(s => s !== val);
                    renderSelected();
                };
                tag.appendChild(remove);
                selectedList.appendChild(tag);
            });
        }
        
        function renderOptions(filter = '') {
            optionsList.innerHTML = '';
            let filtered = options.filter(opt => opt.toLowerCase().includes(filter.toLowerCase()) && !selected.includes(opt));
            if (filter && !options.includes(filter) && !selected.includes(filter)) {
            }
            const addItem = document.createElement('div');
            addItem.className = 'option-item';
            addItem.textContent = `Добавить «${filter}»`;
            addItem.onclick = () => {
                selected.push(filter);
                input.value = '';
                optionsList.style.display = 'none';
                renderSelected();
            };
            optionsList.appendChild(addItem);
            filtered.forEach(opt => {
                const item = document.createElement('div');
                item.className = 'option-item';
                item.textContent = opt;
                item.onclick = () => {
                    selected.push(opt);
                    input.value = '';
                    optionsList.style.display = 'none';
                    renderSelected();
                };
                optionsList.appendChild(item);
            });
            optionsList.style.display = (filtered.length || (filter && !options.includes(filter) && !selected.includes(filter))) ? 'block' : 'none';
        }

        input.oninput = () => {
            renderOptions(input.value.trim());
        };
        input.onfocus = () => {
            renderOptions(input.value.trim());
        };
        input.onblur = () => {
            setTimeout(() => optionsList.style.display = 'none', 200);
        };

        // Для передачи выбранных значений
        container.getSelected = () => selected;
        // Для сброса
        container.reset = () => {
            selected = [];
            renderSelected();
        };
        // Для установки выбранных значений программно
        container.setSelected = (arr) => {
            selected = arr.slice();
            renderSelected();
        };

        renderSelected();
    }
    createMultiSelect('skillsMultiSelect', skillsOptions, "Введите навык...");
    createMultiSelect('languagesMultiSelect', languagesOptions, "Введите язык...");
    createMultiSelect('specializationMultiSelect', specializationOptions, "Введите специализацию...");

    // 4. Вспомогательные функции для AI и фильтрации
    async function aiSmartFilter(queryText) {
        const response = await fetch('/api/ai_filter', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                query: queryText,
                skills: skillsOptions,
                specializations: specializationOptions,
                languages: languagesOptions
            })
        });

        try {
            const ai_filter = await response.json();
            console.log(ai_filter)
            // Выставляем выбранные значения в мультиселекты
            skillsMultiSelect.setSelected(ai_filter.filters.skills || []);
            specializationMultiSelect.setSelected(ai_filter.filters.specializations || []);
            languagesMultiSelect.setSelected(ai_filter.filters.languages || []);
        } catch (e) {
            console.log('Ошибка ', e)
        }
    }

    async function aiReasoning(queryText) {
        const response = await fetch('/api/ai_reasoning', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                query: queryText,
                skills: skillsOptions,
                specializations: specializationOptions,
                languages: languagesOptions
            })
        });
        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let result = '';
        document.getElementById('textAiReasoing').textContent = '';
        while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            result += decoder.decode(value, { stream: true });
            document.getElementById('textAiReasoing').textContent = result;
        }
    }

    async function fetchAndRenderStudents() {
        const params = new URLSearchParams({
            query: searchInput.value,
            city: cityFilter.value,
            experience: expFilter.value,
            gender: genderFilter.value,
            level: educationLevelFilter.value,
            specialization: specializationMultiSelect.getSelected().join(','),
            skills: skillsMultiSelect.getSelected().join(','),
            languages: languagesMultiSelect.getSelected().join(','),
            educationArea: educationAreaFilter.value,
            directionName: directionNameFilter.value,
        });
        const response = await fetch(`/api/search_students?${params.toString()}`);
        const students = await response.json();

        studentsList.innerHTML = '';
        if (!students.length) {
            studentsList.innerHTML = '<p>Ничего не найдено</p>';
            return;
        }
        students.forEach(student => {
            studentsList.innerHTML += `
                <div class="student-card">
                    <div class="student-card-header">
                        <div class="student-card-title">${student.full_name || '-'}</div>
                        <div class="student-card-city">${student.city || '-'}</div>
                    </div>
                    <div class="student-card-row">
                        <span class="student-card-label">Образование:</span>
                        <span class="student-card-value">${student.education_level || '-'}</span>
                        <span class="student-card-label">Опыт:</span>
                        <span class="student-card-value">${student.experience || '-'}</span>
                    </div>
                    <div class="student-card-row">
                        <span class="student-card-label">Университет:</span>
                        <span class="student-card-value">${student.university || '-'}</span>
                    </div>
                    <div class="student-card-tags">
                        ${(student.skills || '-').split(',').map(s => `<span class="student-tag">${s.trim()}</span>`).join('')}
                    </div>
                    <div class="student-card-row">
                        <span class="student-card-label">Область:</span>
                        <span class="student-card-value">${student.education_area || '-'}</span>
                        <span class="student-card-label">Направление:</span>
                        <span class="student-card-value">${student.direction_name || '-'}</span>
                    </div>
                    <div class="student-card-row">
                        <span class="student-card-label">Специализация:</span>
                        <span class="student-card-value">${student.specialization || '-'}</span>
                        <span class="student-card-label">Языки:</span>
                        <span class="student-card-value">${student.languages || '-'}</span>
                        <span class="student-card-label">Пол:</span>
                        <span class="student-card-value">${student.gender || '-'}</span>
                    </div>
                    <div class="student-card-footer">
                        ${student.about || student.about_prof || ''}
                    </div>
                </div>
            `;
        });
    }

    // 5. Обработчики событий для фильтров, поиска и модальных окон
    openFiltersBtn.onclick = () => filterModal.classList.add('active');
    closeFiltersBtn.onclick = () => filterModal.classList.remove('active');
    applyFiltersBtn.onclick = () => {
        filterModal.classList.remove('active');
        fetchAndRenderStudents();
    };
    resetFiltersBtn.onclick = () => {
        filterModal.querySelectorAll('select, input').forEach(el => el.value = '');
        fetchAndRenderStudents();
        cityFilter.classList.add('hideable');
        directionNameFilter.classList.add('hideable');
        skillsMultiSelect.reset();
        languagesMultiSelect.reset();
        specializationMultiSelect.reset();
    };
    filterModal.onclick = (e) => {
        if (e.target === filterModal) filterModal.classList.remove('active');
    };

    searchBtn.onclick = async function() {
        await aiReasoning(searchInput.value)
        await aiSmartFilter(searchInput.value)
        await fetchAndRenderStudents();
    };

    searchInput.addEventListener('keydown', async function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            await aiReasoning(searchInput.value)
            await aiSmartFilter(searchInput.value);
            await fetchAndRenderStudents();
        }
    });

    cityFilter.onchange = fetchAndRenderStudents;
    expFilter.onchange = fetchAndRenderStudents;

    // 6. Логика динамического изменения фильтров (направления и города)
    const directionsByArea = {
        "Педагогические науки": [
            "Педагогика и психология",
            "Педагогика дошкольного воспитания и обучения",
            "Подготовка учителей без предметной специализации",
            "Подготовка учителей с предметной специализацией общего развития",
            "Подготовка учителей по естественнонаучным предметам",
            "Подготовка учителей по гуманитарным предметам",
            "Подготовка учителей по языкам и литературе",
            "Подготовка специалистов по социальной педагогике",
            "Специальная педагогика",
            "Профессиональное обучение (по профилю)"
        ],
        "Искусство и гуманитарные науки": [
            "Дизайн",
            "Изобразительное искусство",
            "Музыка",
            "История",
            "Филология"
        ],
        "Информационно-коммуникационные технологии": [
            "Информационные технологии",
            "Программная инженерия",
            "Веб-разработка",
            "Кибербезопасность"
        ]
        // Добавь остальные области и направления по аналогии
    };

    educationAreaFilter.onchange = function() {
        if (educationAreaFilter.value) {
            directionNameFilter.classList.remove('hideable');
            const area = educationAreaFilter.value;
            directionNameFilter.innerHTML = '<option value="">Любое направление</option>';
            if (directionsByArea[area]) {
                directionsByArea[area].forEach(dir => {
                    const opt = document.createElement('option');
                    opt.value = dir;
                    opt.textContent = dir;
                    directionNameFilter.appendChild(opt);
                });
            }
        } else {
            directionNameFilter.classList.add('hideable');
            directionNameFilter.innerHTML = '<option value="">Любое направление</option>';
        }
        directionNameFilter.value = '';
        fetchAndRenderStudents();
    };

    const regionCities = {
        "Астана": ["Астана"],
        "Алматинская область": [
            "Алматы", "Талдыкорган", "Капшагай", "Есик", "Текели", "Сарыозек", "Каскелен", "Уштобе", "Жаркент"
        ],
        "Атырауская область": [
            "Атырау", "Кульсары", "Индербор", "Махамбет", "Доссор", "Жылыой"
        ],
        "Акмолинская область": [
            "Кокшетау", "Степногорск", "Щучинск", "Атбасар", "Есиль", "Макинск", "Акколь"
        ],
        "Актюбинская область": [
            "Актобе", "Хромтау", "Шалкар", "Темир", "Алга", "Кандыагаш", "Эмба"
        ],
        "Восточно-Казахстанская область": [
            "Өскемен", "Семей", "Риддер", "Зыряновск", "Шемонаиха", "Аягоз", "Курчатов"
        ],
        "Жамбылская область": [
            "Тараз", "Шу", "Каратау", "Жанатас", "Сарысу", "Мерке", "Кордай"
        ],
        "Западно-Казахстанская область": [
            "Уральск", "Аксай", "Казталовка", "Жангалин", "Чапаев", "Переметное"
        ],
        "Карагандинская область": [
            "Караганда", "Темиртау", "Жезказган", "Балхаш", "Сарань", "Шахтинск", "Абай", "Приозерск"
        ],
        "Костанайская область": [
            "Костанай", "Рудный", "Лисаковск", "Аркалык", "Житикара", "Тобыл", "Камысты"
        ],
        "Кызылординская область": [
            "Кызылорда", "Аральск", "Байконур", "Жосалы", "Шиели", "Казалы", "Теренозек"
        ],
        "Мангистауская область": [
            "Актау", "Жанаозен", "Бейнеу", "Форт-Шевченко", "Шетпе", "Курык"
        ],
        "Павлодарская область": [
            "Павлодар", "Экибастуз", "Аксу", "Железинка", "Шарбакты", "Иртышск"
        ],
        "Северо-Казахстанская область": [
            "Петропавловск", "Тайынша", "Сергеевка", "Булаево", "Мамлютка", "Кызылжар"
        ],
        "Туркестанская область": [
            "Туркестан", "Шымкент", "Арысь", "Кентау", "Сарыагаш", "Жетысай", "Ленгер", "Тюлькубас"
        ],
        "Улытауская область": [
            "Жезказган", "Сатпаев", "Ұлытау"
        ],
        "Шымкент": ["Шымкент"]
    };

    regionFilter.onchange = function() {
        if (regionFilter.value) {
            cityFilter.classList.remove('hideable');
            const region = regionFilter.value;
            cityFilter.innerHTML = '<option value="">Все города</option>';
            if (regionCities[region]) {
                regionCities[region].forEach(city => {
                    const opt = document.createElement('option');
                    opt.value = city;
                    opt.textContent = city;
                    cityFilter.appendChild(opt);
                });
            }
        } else {
            cityFilter.classList.add('hideable');
            cityFilter.innerHTML = '<option value="">Все города</option>';
        }
        cityFilter.value = '';
        fetchAndRenderStudents();
    };
    // 7. Первая загрузка студентов
    fetchAndRenderStudents();


    // 8. Логика reasoning box (разворачивание/сворачивание)
    function updateReasoningToggle() {
        if (aiReasoningBox.scrollHeight > aiReasoningBox.clientHeight + 5) {
            aiReasoningToggle.style.display = '';
        } else {
            aiReasoningToggle.style.display = 'none';
        }
    }

    aiReasoningToggle.onclick = function() {
        aiReasoningBox.classList.toggle('expanded');
        aiReasoningToggleIcon.innerHTML = aiReasoningBox.classList.contains('expanded') ? '&#8593;' : '&#8595;';
    };

    const origSetReasoning = (text) => {
        aiReasoningBox.textContent = text;
        aiReasoningBox.classList.remove('expanded');
        aiReasoningToggleIcon.innerHTML = '&#8595;';
        setTimeout(updateReasoningToggle, 100); // подождать рендер
    };

    // Используй origSetReasoning для вывода reasoning:
    // origSetReasoning("Текст reasoning...");

    // Если reasoning приходит по частям (stream), вызывай origSetReasoning(result) после окончания стрима
});