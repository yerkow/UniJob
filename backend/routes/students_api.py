from fastapi import APIRouter, Depends, Query, Request
from sqlalchemy.orm import Session
from sqlalchemy import or_
from ..database.connectDB import db_get
from ..database.models import Student, User
from openai import OpenAI
import os
from dotenv import load_dotenv
import json
from fastapi.responses import JSONResponse, StreamingResponse


load_dotenv()
router = APIRouter()

OPENAI_API_KEY = os.getenv("TOKENGPT")
print('ТОКЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕН' ,OPENAI_API_KEY)

@router.post("/api/ai_reasoning")
async def ai_filter(requests: Request):
    data = await requests.json()
    user_query = data["query"]
    skills = data.get("skills", [])
    specializations = data.get("specializations", [])
    languages = data.get("languages", [])
    skills_str = ", ".join(skills)
    specs_str = ", ".join(specializations)
    langs_str = ", ".join(languages)
    prompt = f"""
    Ты — ассистент, который объясняет, как запрос работодателя связан с фильтрами (навыки, специализации, языки).

    Вот список всех возможных навыков: {skills}
    Вот список всех возможных специализаций: {specializations}
    Вот список всех возможных языков: {languages}

    Пользователь написал запрос: "{user_query}"

    Твоя задача — объяснить свой выбор фильтров:
    - Пиши reasoning от первого лица, как будто ты общаешься с человеком.
    - Используй дружелюбный, объясняющий тон, например: "Я выбрал такие фильтры, потому что...", "Мне кажется, что для этого запроса подойдут следующие навыки...", "Я считаю, что...".
    - Не используй фигурные скобки, JSON, ключи, форматирование.
    - Просто объясни, какие фильтры, по твоему мнению, могут быть выбраны по этому запросу и почему.
    """
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENAI_API_KEY,
    )

    def stream_response():
        response = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[{"role": "user", "content": prompt}],
            stream=True,
        )
        for chunk in response:
            if hasattr(chunk, "choices") and chunk.choices:
                delta = chunk.choices[0].delta
                print(delta)
                if hasattr(delta, "content") and delta.content:
                    yield delta.content  # отправляем кусочек сразу

    return StreamingResponse(stream_response(), media_type="text/plain")

@router.post("/api/ai_filter")
async def ai_filter(requests: Request):
    data = await requests.json()
    user_query = data["query"]
    skills = data.get("skills", [])
    specializations = data.get("specializations", [])
    languages = data.get("languages", [])
    prompt = f"""
    Ты — ассистент, который формирует JSON-фильтры по запросу работодателя.

    Вот список всех возможных навыков: {skills}
    Вот список всех возможных специализаций: {specializations}
    Вот список всех возможных языков: {languages}

    Пользователь написал запрос: "{user_query}"

    Твоя задача:
    - Верни **только** JSON-объект строго в таком формате:

    {{
      "filters": {{
        "skills": ["Навык1", "Навык2"],
        "specializations": ["Спец1"],
        "languages": ["Язык1"]
      }}
    }}

    - Без пояснений, без текста до или после.
    - Не используй Markdown или форматирование.
    - Если какой-то список пуст — оставь его пустым.
    - Не придумывай значения, которых нет в списке.
    """
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENAI_API_KEY,
    )   
    response = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[{"role": "user", "content": prompt}],
    )
    content = response.choices[0].message.content
    filters_json = json.loads(content)
    return JSONResponse(content=filters_json)

    


@router.get("/api/search_students")
def search_students(
    city: str = "",
    experience: str = "",
    gender: str = "",
    level: str = "",
    specialization: str = "",
    skills: str = "",
    languages: str = "",
    educationArea: str = "",
    directionName: str = "",
    db: Session = Depends(db_get)
):
    q = db.query(Student).join(User)
    # if query:
    #     q = q.filter(
    #         (User.first_name.ilike(f"%{query}%")) |
    #         (User.last_name.ilike(f"%{query}%")) |
    #         (Student.about_prof.ilike(f"%{query}%")) |
    #         (Student.short_about.ilike(f"%{query}%")) |
    #         (Student.gender.ilikle(f"%{query}%"))
    #     )
    if city:
        q = q.filter(Student.city == city)
    if experience:
        q = q.filter(Student.work_experience == experience)
    if gender:
        q = q.filter(Student.gender == gender)
    if level:
        q = q.filter(Student.education_level == level)    
    if specialization:
        specs = [s.strip() for s in specialization.split(',') if s.strip()]
        if specs:
            q = q.filter(or_(*[Student.specialization.ilike(f"%{s}%") for s in specs]))
    if skills:
        skills_list = [s.strip() for s in skills.split(',') if s.strip()]
        if skills_list:
            q = q.filter(or_(*[Student.skills.ilike(f"%{s}%") for s in skills_list]))
    if languages:
        langs = [s.strip() for s in languages.split(',') if s.strip()]
        if langs:
            q = q.filter(or_(*[Student.languages.ilike(f"%{l}%") for l in langs]))
    if educationArea:
        q = q.filter(Student.education_area == educationArea)
    if directionName:
        q = q.filter(Student.direction_name == directionName)                
    # university фильтр добавь если поле есть
    students = q.all()
    result = []
    for s in students:
        result.append({
            "full_name": f"{s.user.first_name} {s.user.last_name}",
            "university": "",  # если есть поле, замени на s.university
            "city": s.city,
            "experience": s.work_experience,
            "skills": s.skills,
            "languages": s.languages,
            "gender": s.gender,
            "education_level": s.education_level,
            "education_area": s.education_area,
            "direction_name": s.direction_name,
            "specialization": s.specialization,
            "about": s.about,
            "about_prof": s.about_prof,
            "short_about": s.short_about
        })
    return result