from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from ..database.connectDB import db_get
from ..database.models import Student, User

router = APIRouter()

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
        q = q.filter(Student.specialization == specialization)
    if skills:
        q = q.filter(Student.skills == skills)
    if languages:
        q = q.filter(Student.languages == languages)
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