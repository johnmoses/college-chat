import datetime
from config.db import db


class Course(db.Model):
    __tablename__ = 'courses_course'

    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=True)

    # students = db.relationship('User', backref='coursescoursestudents', secondary='courses_registrants', viewonly=True, cascade='all,delete')
    # registrations = db.relationship('Registration', backref='coursescourseregistrations', cascade='all,delete')

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return 'Course {}'.format(self.id)


class Registration(db.Model):
    __tablename__ = 'courses_registration'

    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    comment = db.Column(db.Text(), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    course_id = db.Column(db.Integer, db.ForeignKey('courses_course.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('User.id'))

    course = db.relationship("Course", backref="coursesregistrationcourse", viewonly=True, cascade='all,delete')
    registrant = db.relationship('User', backref="coursesregistrant", cascade='all,delete')

    def __init__(self, course_id, student_id):
        self.course_id = course_id
        self.student_id = student_id

    def __repr__(self):
        return 'Registration {}'.format(self.id)
