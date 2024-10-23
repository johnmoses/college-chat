# """
# API functions
# """
from .models import db, Course, Registration

class CollegeController:
    def __init__(self):
        pass

    def get_courses():
        courses = Course.query.all()
        return courses if courses else []
    
    def get_course(id):
        course = Course.query.filter_by(id=id).first()
        return course if course else []

    def create_course(name,description):
        course = Course(name,description)
        db.session.add(course)
        db.session.commit()

    def get_registrations():
        registrations = Registration.query.all()
        return registrations if registrations else []
    
    def get_registration(id):
        registration = Registration.query.filter_by(id=id).first()
        return registration if registration else []

    def create_registration(course_id,student_id):
        registration = Registration(course_id,student_id)
        db.session.add(registration)
        db.session.commit()
