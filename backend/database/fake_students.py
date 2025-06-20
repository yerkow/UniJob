from .models import User, Student
from fastapi import APIRouter, Form, Depends, Request
from sqlalchemy.orm import Session
from .connectDB import db_get
import random
import logging

logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)
def create_fake_students(db: Session =  Depends(db_get())):
    fake_data = [
        {
            "email": "nursultan@mail.com",
            "password": "123",
            "first_name": "Нурсултан",
            "last_name": "Ермеков",
            "types": "user",
            "student": {
                "short_about": "Ответственный, коммуникабельный",
                "region": "Астана",
                "city": "Астана",
                "birth_date": "2000-01-01",
                "gender": "Мужской",
                "phone": "87010001122",
                "desired_salary": 500000,
                "about": "Люблю учиться",
                "about_prof": "Python, Excel",
                "work_experience": "Стажировка",
                "achievements": "Победитель олимпиады",
                "education_level": "Бакалавриат",
                "education_area": "Информационно-коммуникационные технологии",
                "direction_name": "Информационные технологии",
                "specialization": "Web-разработка",
                "skills": "Python, Excel",
                "languages": "Казахский C2, Русский C2, Английский B2"
            }
        },
        {
            "email": "aigerim@mail.com",
            "password": "123",
            "first_name": "Айгерим",
            "last_name": "Серикова",
            "types": "user",
            "student": {
                "short_about": "Быстро учусь",
                "region": "Алматинская область",
                "city": "Алматы",
                "birth_date": "2001-05-10",
                "gender": "Женский",
                "phone": "87020002233",
                "desired_salary": 600000,
                "about": "Люблю командную работу",
                "about_prof": "Java, Soft Skills",
                "work_experience": "Работа",
                "achievements": "Участник хакатона",
                "education_level": "Магистратура",
                "education_area": "Педагогические науки",
                "direction_name": "Педагогика и психология",
                "specialization": "Математика",
                "skills": "Java, Soft Skills",
                "languages": "Казахский C2, Русский C2, Английский B1"
            }
        },
        {
            "email": "daulet@mail.com",
            "password": "123",
            "first_name": "Даулет",
            "last_name": "Жумабеков",
            "types": "user",
            "student": {
                "short_about": "Трудолюбивый",
                "region": "Туркестанская область",
                "city": "Шымкент",
                "birth_date": "1999-03-15",
                "gender": "Мужской",
                "phone": "87030003344",
                "desired_salary": 550000,
                "about": "Люблю спорт",
                "about_prof": "C++, Teamwork",
                "work_experience": "Работа",
                "achievements": "Призёр соревнований",
                "education_level": "Бакалавриат",
                "education_area": "Информационно-коммуникационные технологии",
                "direction_name": "Программная инженерия",
                "specialization": "Frontend",
                "skills": "C++, Teamwork",
                "languages": "Казахский C2, Русский C2, Английский B2"
            }
        },
        {
            "email": "gulnaz@mail.com",
            "password": "123",
            "first_name": "Гульназ",
            "last_name": "Турсынова",
            "types": "user",
            "student": {
                "short_about": "Креативная",
                "region": "Карагандинская область",
                "city": "Караганда",
                "birth_date": "2002-07-22",
                "gender": "Женский",
                "phone": "87040004455",
                "desired_salary": 480000,
                "about": "Люблю дизайн",
                "about_prof": "Photoshop, Illustrator",
                "work_experience": "Стажировка",
                "achievements": "Победитель конкурса дизайна",
                "education_level": "Бакалавриат",
                "education_area": "Искусство и гуманитарные науки",
                "direction_name": "Дизайн",
                "specialization": "Графический дизайн",
                "skills": "Photoshop, Illustrator",
                "languages": "Казахский C2, Русский C2, Английский B1"
            }
        },
        {
            "email": "yerzhan@mail.com",
            "password": "123",
            "first_name": "Ержан",
            "last_name": "Калиев",
            "types": "user",
            "student": {
                "short_about": "Пунктуальный",
                "region": "Актюбинская область",
                "city": "Актобе",
                "birth_date": "2000-11-30",
                "gender": "Мужской",
                "phone": "87050005566",
                "desired_salary": 520000,
                "about": "Люблю программировать",
                "about_prof": "JavaScript, HTML",
                "work_experience": "Стажировка",
                "achievements": "Участник IT-форума",
                "education_level": "Бакалавриат",
                "education_area": "Информационно-коммуникационные технологии",
                "direction_name": "Веб-разработка",
                "specialization": "Frontend",
                "skills": "JavaScript, HTML, CSS",
                "languages": "Казахский C2, Русский C2, Английский B2"
            }
        },
        {
            "email": "aliya@mail.com",
            "password": "123",
            "first_name": "Алия",
            "last_name": "Мухамеджанова",
            "types": "user",
            "student": {
                "short_about": "Ответственная",
                "region": "Павлодарская область",
                "city": "Павлодар",
                "birth_date": "2003-02-18",
                "gender": "Женский",
                "phone": "87060006677",
                "desired_salary": 470000,
                "about": "Люблю английский язык",
                "about_prof": "Soft Skills, Английский",
                "work_experience": "Нет",
                "achievements": "Сертификат IELTS",
                "education_level": "Бакалавриат",
                "education_area": "Педагогические науки",
                "direction_name": "Подготовка учителей по языкам и литературе",
                "specialization": "Английский язык",
                "skills": "Soft Skills, Английский",
                "languages": "Казахский C2, Русский C2, Английский B2"
            }
        },
        {
            "email": "askar@mail.com",
            "password": "123",
            "first_name": "Аскар",
            "last_name": "Сагынбаев",
            "types": "user",
            "student": {
                "short_about": "Лидер",
                "region": "Жамбылская область",
                "city": "Тараз",
                "birth_date": "1998-09-09",
                "gender": "Мужской",
                "phone": "87070007788",
                "desired_salary": 700000,
                "about": "Люблю управлять проектами",
                "about_prof": "Project Management",
                "work_experience": "Работа",
                "achievements": "Руководитель студенческого проекта",
                "education_level": "Магистратура",
                "education_area": "Информационно-коммуникационные технологии",
                "direction_name": "Кибербезопасность",
                "specialization": "Менеджмент",
                "skills": "Project Management, Teamwork",
                "languages": "Казахский C2, Русский C2, Английский C1"
            }
        },
        {
            "email": "zhanel@mail.com",
            "password": "123",
            "first_name": "Жанель",
            "last_name": "Абдрахманова",
            "types": "user",
            "student": {
                "short_about": "Коммуникабельная",
                "region": "Костанайская область",
                "city": "Костанай",
                "birth_date": "2002-04-12",
                "gender": "Женский",
                "phone": "87080008899",
                "desired_salary": 490000,
                "about": "Люблю вокал",
                "about_prof": "Вокал, Soft Skills",
                "work_experience": "Стажировка",
                "achievements": "Победитель вокального конкурса",
                "education_level": "Бакалавриат",
                "education_area": "Искусство и гуманитарные науки",
                "direction_name": "Музыка",
                "specialization": "Вокал",
                "skills": "Вокал, Soft Skills",
                "languages": "Казахский C2, Русский C2, Английский B1"
            }
        },
        {
            "email": "nurbolat@mail.com",
            "password": "123",
            "first_name": "Нурболат",
            "last_name": "Сулейменов",
            "types": "user",
            "student": {
                "short_about": "Аналитик",
                "region": "Западно-Казахстанская область",
                "city": "Уральск",
                "birth_date": "2001-08-25",
                "gender": "Мужской",
                "phone": "87090009900",
                "desired_salary": 650000,
                "about": "Люблю анализ данных",
                "about_prof": "Data Science, Python",
                "work_experience": "Работа",
                "achievements": "Победитель Data Science Cup",
                "education_level": "Магистратура",
                "education_area": "Информационно-коммуникационные технологии",
                "direction_name": "Информационные технологии",
                "specialization": "Data Science",
                "skills": "Data Science, Python",
                "languages": "Казахский C2, Русский C2, Английский C1"
            }
        },
        {
            "email": "dinara@mail.com",
            "password": "123",
            "first_name": "Динара",
            "last_name": "Кабдолова",
            "types": "user",
            "student": {
                "short_about": "Творческая",
                "region": "Восточно-Казахстанская область",
                "city": "Семей",
                "birth_date": "2004-12-03",
                "gender": "Женский",
                "phone": "87100001123",
                "desired_salary": 450000,
                "about": "Люблю фотографию",
                "about_prof": "Фотография, Photoshop",
                "work_experience": "Нет",
                "achievements": "Победитель фотоконкурса",
                "education_level": "Бакалавриат",
                "education_area": "Искусство и гуманитарные науки",
                "direction_name": "Дизайн",
                "specialization": "Фотография",
                "skills": "Фотография, Photoshop",
                "languages": "Казахский C2, Русский C2, Английский B1"
            }
        },
        {
            "email": "ivanov@mail.com",
            "password": "123",
            "first_name": "Иван",
            "last_name": "Иванов",
            "types": "user",
            "student": {
                "short_about": "Люблю backend и базы данных",
                "region": "Алматинская область",
                "city": "Алматы",
                "birth_date": "2000-06-15",
                "gender": "Мужской",
                "phone": "87011112233",
                "desired_salary": 600000,
                "about": "Работал с PostgreSQL и Node.js",
                "about_prof": "Node.js, SQL, PostgreSQL",
                "work_experience": "Работа",
                "achievements": "Победитель хакатона",
                "education_level": "Бакалавриат",
                "education_area": "Информационно-коммуникационные технологии",
                "direction_name": "Программная инженерия",
                "specialization": "Backend",
                "skills": "Node.js, SQL, PostgreSQL, Git, Docker",
                "languages": "Русский C2, Английский B2"
            }
        },
        {
            "email": "elena@mail.com",
            "password": "123",
            "first_name": "Елена",
            "last_name": "Петрова",
            "types": "user",
            "student": {
                "short_about": "Креативный дизайнер",
                "region": "Карагандинская область",
                "city": "Караганда",
                "birth_date": "2001-03-22",
                "gender": "Женский",
                "phone": "87022223344",
                "desired_salary": 550000,
                "about": "Работаю в Figma и Adobe Photoshop",
                "about_prof": "Figma, Adobe Photoshop, UX/UI дизайн",
                "work_experience": "Стажировка",
                "achievements": "Победитель конкурса дизайна",
                "education_level": "Бакалавриат",
                "education_area": "Искусство и гуманитарные науки",
                "direction_name": "Дизайн",
                "specialization": "UX/UI дизайн",
                "skills": "Figma, Adobe Photoshop, UX/UI дизайн",
                "languages": "Русский C2, Английский B1"
            }
        },
        {
            "email": "sergey@mail.com",
            "password": "123",
            "first_name": "Сергей",
            "last_name": "Ким",
            "types": "user",
            "student": {
                "short_about": "Интересуюсь DevOps и автоматизацией",
                "region": "Астана",
                "city": "Астана",
                "birth_date": "1999-12-01",
                "gender": "Мужской",
                "phone": "87033334455",
                "desired_salary": 700000,
                "about": "Люблю автоматизировать процессы",
                "about_prof": "DevOps, Docker, Kubernetes, Linux",
                "work_experience": "Работа",
                "achievements": "Участник DevOps Bootcamp",
                "education_level": "Магистратура",
                "education_area": "Информационно-коммуникационные технологии",
                "direction_name": "Информационные технологии",
                "specialization": "DevOps",
                "skills": "DevOps, Docker, Kubernetes, Linux, Git",
                "languages": "Русский C2, Английский C1"
            }
        },
        {
            "email": "madina@mail.com",
            "password": "123",
            "first_name": "Мадина",
            "last_name": "Ахметова",
            "types": "user",
            "student": {
                "short_about": "Люблю преподавать и работать с детьми",
                "region": "Павлодарская область",
                "city": "Павлодар",
                "birth_date": "2002-09-10",
                "gender": "Женский",
                "phone": "87044445566",
                "desired_salary": 500000,
                "about": "Педагог по математике",
                "about_prof": "Педагогика, Математика, Soft Skills",
                "work_experience": "Стажировка",
                "achievements": "Лучший молодой педагог 2023",
                "education_level": "Бакалавриат",
                "education_area": "Педагогические науки",
                "direction_name": "Педагогика и психология",
                "specialization": "Математика",
                "skills": "Педагогика, Математика, Soft Skills",
                "languages": "Казахский C2, Русский C2, Английский B2"
            }
        },
        {
            "email": "alex@mail.com",
            "password": "123",
            "first_name": "Алексей",
            "last_name": "Смирнов",
            "types": "user",
            "student": {
                "short_about": "Frontend-разработчик",
                "region": "Туркестанская область",
                "city": "Шымкент",
                "birth_date": "2001-11-05",
                "gender": "Мужской",
                "phone": "87055556677",
                "desired_salary": 650000,
                "about": "Делаю сайты на React и Vue.js",
                "about_prof": "React, Vue.js, JavaScript, HTML, CSS",
                "work_experience": "Работа",
                "achievements": "Участник Frontend Meetup",
                "education_level": "Бакалавриат",
                "education_area": "Информационно-коммуникационные технологии",
                "direction_name": "Веб-разработка",
                "specialization": "Frontend",
                "skills": "React, Vue.js, JavaScript, HTML, CSS",
                "languages": "Русский C2, Английский B2"
            }
        },
        {
            "email": "aliya2@mail.com",
            "password": "123",
            "first_name": "Алия",
            "last_name": "Жумагалиева",
            "types": "user",
            "student": {
                "short_about": "HR и рекрутинг",
                "region": "Атырауская область",
                "city": "Атырау",
                "birth_date": "2000-04-18",
                "gender": "Женский",
                "phone": "87066667788",
                "desired_salary": 600000,
                "about": "Работаю с персоналом и подбором кадров",
                "about_prof": "HR, Рекрутинг, Коммуникация",
                "work_experience": "Работа",
                "achievements": "Лучший HR года",
                "education_level": "Магистратура",
                "education_area": "Экономика и управление",
                "direction_name": "Менеджмент",
                "specialization": "HR",
                "skills": "HR, Рекрутинг, Коммуникация",
                "languages": "Русский C2, Английский B1"
            }
        },
        {
            "email": "dmitry@mail.com",
            "password": "123",
            "first_name": "Дмитрий",
            "last_name": "Волков",
            "types": "user",
            "student": {
                "short_about": "Data Scientist",
                "region": "Костанайская область",
                "city": "Костанай",
                "birth_date": "1998-08-30",
                "gender": "Мужской",
                "phone": "87077778899",
                "desired_salary": 800000,
                "about": "Работаю с Big Data и машинным обучением",
                "about_prof": "Python, Data Science, Machine Learning, Big Data",
                "work_experience": "Работа",
                "achievements": "Победитель Data Science Challenge",
                "education_level": "Магистратура",
                "education_area": "Информационно-коммуникационные технологии",
                "direction_name": "Информационные технологии",
                "specialization": "Data Science",
                "skills": "Python, Data Science, Machine Learning, Big Data",
                "languages": "Русский C2, Английский C1"
            }
        },
         {
        "email": "aibek_99@mail.com",
        "password": "123",
        "first_name": "Айбек",
        "last_name": "Сулейменов",
        "types": "user",
        "student": {
            "short_about": "Python-разработчик с опытом",
            "region": "Алматинская область",
            "city": "Алматы",
            "birth_date": "1999-03-15",
            "gender": "Мужской",
            "phone": "87011234567",
            "desired_salary": 600000,
            "about": "Увлекаюсь машинным обучением",
            "about_prof": "Python, SQL, Machine Learning",
            "work_experience": "3 года",
            "achievements": "Разработал рекомендательный алгоритм",
            "education_level": "Бакалавриат",
            "education_area": "Информационные технологии",
            "direction_name": "Data Science",
            "specialization": "Machine Learning",
            "skills": "Python, SQL, Machine Learning, Git",
            "languages": "Казахский (родной), Английский B2"
        }
    },
    {
        "email": "gulnara_2000@gmail.com",
        "password": "123",
        "first_name": "Гулнара",
        "last_name": "Каримова",
        "types": "user",
        "student": {
            "short_about": "UX/UI дизайнер с фокусом на Figma",
            "region": "Астана",
            "city": "Астана",
            "birth_date": "2000-08-22",
            "gender": "Женский",
            "phone": "87059876543",
            "desired_salary": 450000,
            "about": "Создаю удобные интерфейсы",
            "about_prof": "Figma, UX/UI дизайн",
            "work_experience": "1.5 года",
            "achievements": "Дизайн для мобильного банка",
            "education_level": "Бакалавриат",
            "education_area": "Дизайн",
            "direction_name": "UX/UI дизайн",
            "specialization": "UX/UI дизайн",
            "skills": "Figma, Adobe XD, Прототипирование, Soft Skills",
            "languages": "Русский (родной), Английский B1"
        }
    },
    {
        "email": "erlan_dev@yandex.kz",
        "password": "123",
        "first_name": "Ерлан",
        "last_name": "Бектемиров",
        "types": "user",
        "student": {
            "short_about": "Fullstack разработчик",
            "region": "Туркестанская область",
            "city": "Шымкент",
            "birth_date": "1997-11-05",
            "gender": "Мужской",
            "phone": "87776543210",
            "desired_salary": 750000,
            "about": "Работаю с React и Node.js",
            "about_prof": "JavaScript, React, Node.js",
            "work_experience": "5 лет",
            "achievements": "Запустил 3 крупных проекта",
            "education_level": "Бакалавриат",
            "education_area": "Информационные технологии",
            "direction_name": "Web-разработка",
            "specialization": "Fullstack",
            "skills": "JavaScript, React, Node.js, Docker, Git",
            "languages": "Казахский C2, Русский C2, Английский B2"
        }
    },
    {
        "email": "diana_photo@bk.ru",
        "password": "123",
        "first_name": "Диана",
        "last_name": "Садыкова",
        "types": "user",
        "student": {
            "short_about": "Профессиональный фотограф",
            "region": "Атырауская область",
            "city": "Атырау",
            "birth_date": "2001-04-18",
            "gender": "Женский",
            "phone": "87071112233",
            "desired_salary": 300000,
            "about": "Снимаю портреты и события",
            "about_prof": "Фотография, Photoshop",
            "work_experience": "Без опыта",
            "achievements": "Портфолио в Instagram",
            "education_level": "Бакалавриат",
            "education_area": "Изобразительное искусство",
            "direction_name": "Фотография",
            "specialization": "Фотография",
            "skills": "Фотография, Adobe Photoshop, Коммуникация",
            "languages": "Казахский (родной), Русский C2"
        }
    },
    {
        "email": "timur_music@mail.com",
        "password": "123",
        "first_name": "Тимур",
        "last_name": "Калиев",
        "types": "user",
        "student": {
            "short_about": "Вокалист и педагог",
            "region": "Восточно-Казахстанская область",
            "city": "Семей",
            "birth_date": "1996-09-30",
            "gender": "Мужской",
            "phone": "87029998877",
            "desired_salary": 350000,
            "about": "Обучаю вокалу и музыке",
            "about_prof": "Вокал, Музыка",
            "work_experience": "4 года",
            "achievements": "Выступления в театрах",
            "education_level": "Бакалавриат",
            "education_area": "Музыкальное искусство",
            "direction_name": "Музыка",
            "specialization": "Вокал",
            "skills": "Вокал, Пение, Обучение, Креативность",
            "languages": "Казахский C2, Русский C2"
        }
    },
    {
        "email": "aida_hr@gmail.com",
        "password": "123",
        "first_name": "Айда",
        "last_name": "Нурмухамбетова",
        "types": "user",
        "student": {
            "short_about": "HR-специалист",
            "region": "Карагандинская область",
            "city": "Караганда",
            "birth_date": "1998-06-14",
            "gender": "Женский",
            "phone": "87058887766",
            "desired_salary": 400000,
            "about": "Нахожу таланты для компаний",
            "about_prof": "HR, Рекрутинг",
            "work_experience": "2 года",
            "achievements": "Настроила систему найма",
            "education_level": "Бакалавриат",
            "education_area": "Управление персоналом",
            "direction_name": "HR",
            "specialization": "Рекрутинг",
            "skills": "Recruiting, Communication, Teamwork, Agile",
            "languages": "Казахский C2, Русский C2, Английский A2"
        }
    },
    {
        "email": "nurik_dev@protonmail.com",
        "password": "123",
        "first_name": "Нуржан",
        "last_name": "Темирбеков",
        "types": "user",
        "student": {
            "short_about": "Junior Frontend разработчик",
            "region": "Павлодарская область",
            "city": "Павлодар",
            "birth_date": "2002-01-25",
            "gender": "Мужской",
            "phone": "87772223344",
            "desired_salary": 250000,
            "about": "Только начинаю в IT",
            "about_prof": "HTML, CSS, JavaScript",
            "work_experience": "Без опыта",
            "achievements": "Прошел курс по веб-разработке",
            "education_level": "Бакалавриат",
            "education_area": "Информационные технологии",
            "direction_name": "Web-разработка",
            "specialization": "Frontend",
            "skills": "HTML, CSS, JavaScript, Git",
            "languages": "Казахский C2, Русский C2, Английский A2"
        }
    },
    {
        "email": "aruzhan_finance@mail.com",
        "password": "123",
        "first_name": "Аружан",
        "last_name": "Абдулина",
        "types": "user",
        "student": {
            "short_about": "Финансовый аналитик",
            "region": "Актюбинская область",
            "city": "Актобе",
            "birth_date": "1995-12-10",
            "gender": "Женский",
            "phone": "87017776655",
            "desired_salary": 500000,
            "about": "Оптимизирую бюджеты компаний",
            "about_prof": "Excel, Финансы",
            "work_experience": "5 лет",
            "achievements": "Повысила рентабельность на 20%",
            "education_level": "Магистратура",
            "education_area": "Финансы и кредит",
            "direction_name": "Финансы",
            "specialization": "Финансовый анализ",
            "skills": "Excel, Финансы, Бюджетирование, Аналитика",
            "languages": "Казахский C2, Русский C2, Английский B1"
        }
    },
    {
        "email": "maxat_android@yandex.kz",
        "password": "123",
        "first_name": "Максат",
        "last_name": "Жумагулов",
        "types": "user",
        "student": {
            "short_about": "Android-разработчик",
            "region": "Жамбылская область",
            "city": "Тараз",
            "birth_date": "2000-07-08",
            "gender": "Мужской",
            "phone": "87073334455",
            "desired_salary": 550000,
            "about": "Создаю приложения для Android",
            "about_prof": "Kotlin, Android Studio",
            "work_experience": "2 года",
            "achievements": "Приложение в Google Play",
            "education_level": "Бакалавриат",
            "education_area": "Информационные технологии",
            "direction_name": "Мобильная разработка",
            "specialization": "Android",
            "skills": "Kotlin, Android Studio, Git, QA",
            "languages": "Казахский (родной), Русский C2, Английский B1"
        }
    },
    {
        "email": "zere_design@gmail.com",
        "password": "123",
        "first_name": "Зерез",
        "last_name": "Иманова",
        "types": "user",
        "student": {
            "short_about": "Графический дизайнер",
            "region": "Северо-Казахстанская область",
            "city": "Петропавловск",
            "birth_date": "2001-02-17",
            "gender": "Женский",
            "phone": "87056667788",
            "desired_salary": 300000,
            "about": "Создаю логотипы и баннеры",
            "about_prof": "Adobe Photoshop, Illustrator",
            "work_experience": "Без опыта",
            "achievements": "Портфолио в Behance",
            "education_level": "Бакалавриат",
            "education_area": "Графический дизайн",
            "direction_name": "Графический дизайн",
            "specialization": "Графический дизайн",
            "skills": "Adobe Photoshop, Illustrator, Внимательность, Креативность",
            "languages": "Казахский C2, Русский C2, Английский A2"
        }
    },
    {
        "email": "serik_data@mail.com",
        "password": "123",
        "first_name": "Серік",
        "last_name": "Қасымов",
        "types": "user",
        "student": {
            "short_about": "Data Scientist",
            "region": "Костанайская область",
            "city": "Костанай",
            "birth_date": "1997-10-09",
            "gender": "Мужской",
            "phone": "87779990011",
            "desired_salary": 800000,
            "about": "Анализирую большие данные",
            "about_prof": "Python, Data Science",
            "work_experience": "4 года",
            "achievements": "Публикации в научных журналах",
            "education_level": "Магистратура",
            "education_area": "Прикладная математика",
            "direction_name": "Data Science",
            "specialization": "Data Science",
            "skills": "Python, R, Big Data, Machine Learning",
            "languages": "Казахский C2, Русский C2, Английский B2"
        }
    },
    {
        "email": "aida_marketing@bk.ru",
        "password": "123",
        "first_name": "Айда",
        "last_name": "Сатыбалдиева",
        "types": "user",
        "student": {
            "short_about": "SMM-специалист",
            "region": "Западно-Казахстанская область",
            "city": "Уральск",
            "birth_date": "1999-05-20",
            "gender": "Женский",
            "phone": "87018889900",
            "desired_salary": 350000,
            "about": "Работаю с соцсетями брендов",
            "about_prof": "SMM, SEO",
            "work_experience": "2 года",
            "achievements": "Увеличила охват на 50%",
            "education_level": "Бакалавриат",
            "education_area": "Маркетинг",
            "direction_name": "Маркетинг",
            "specialization": "SMM",
            "skills": "SMM, SEO, Photoshop, Soft Skills",
            "languages": "Казахский C2, Русский C2, Английский B1"
        }
    },
    {
        "email": "bekzat_linux@yandex.kz",
        "password": "123",
        "first_name": "Бекзат",
        "last_name": "Абдрахманов",
        "types": "user",
        "student": {
            "short_about": "DevOps-инженер",
            "region": "Карагандинская область",
            "city": "Темиртау",
            "birth_date": "1996-04-01",
            "gender": "Мужской",
            "phone": "87775556677",
            "desired_salary": 900000,
            "about": "Работаю с Linux и Docker",
            "about_prof": "DevOps, Linux",
            "work_experience": "6 лет",
            "achievements": "Автоматизировал деплой",
            "education_level": "Бакалавриат",
            "education_area": "Информационные технологии",
            "direction_name": "DevOps",
            "specialization": "DevOps",
            "skills": "Linux, Docker, Kubernetes, Git",
            "languages": "Казахский C2, Русский C2, Английский B2"
        }
    },
    {
        "email": "marzhan_accounting@gmail.com",
        "password": "123",
        "first_name": "Маржан",
        "last_name": "Тулеева",
        "types": "user",
        "student": {
            "short_about": "Бухгалтер",
            "region": "Кызылординская область",
            "city": "Кызылорда",
            "birth_date": "1994-11-12",
            "gender": "Женский",
            "phone": "87054443322",
            "desired_salary": 450000,
            "about": "Веду учет на 1С",
            "about_prof": "Бухгалтерия, Excel",
            "work_experience": "8 лет",
            "achievements": "Оптимизация налогов",
            "education_level": "Бакалавриат",
            "education_area": "Бухгалтерский учет",
            "direction_name": "Бухгалтерия",
            "specialization": "Бухгалтерия",
            "skills": "1C, Excel, Бухгалтерия, Ответственность",
            "languages": "Казахский C2, Русский C2"
        }
    },
    {
        "email": "nurly_teach@mail.com",
        "password": "123",
        "first_name": "Нурлы",
        "last_name": "Байжанов",
        "types": "user",
        "student": {
            "short_about": "Учитель английского",
            "region": "Восточно-Казахстанская область",
            "city": "Өскемен",
            "birth_date": "1993-09-05",
            "gender": "Мужской",
            "phone": "87074445566",
            "desired_salary": 300000,
            "about": "Обучаю английскому языку",
            "about_prof": "Английский язык, Обучение",
            "work_experience": "7 лет",
            "achievements": "IELTS 8.0",
            "education_level": "Бакалавриат",
            "education_area": "Лингвистика",
            "direction_name": "Английский язык",
            "specialization": "Английский язык",
            "skills": "Английский, Обучение, Коммуникация",
            "languages": "Казахский C2, Русский C2, Английский C1"
        }
    }
]

    for data in fake_data:
        user = User(
            email=data["email"],
            hashed_password=data["password"],  # для теста можно без хеша
            first_name=data["first_name"],
            last_name=data["last_name"],
            types=data["types"]
        )
        db.add(user)
        db.commit()
        student = Student(
            user_id=user.id,
            **data["student"]
        )
        db.add(student)
        db.commit()