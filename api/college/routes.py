from flask import request, jsonify, redirect, render_template, url_for, flash, session
from college import bp
from college.controllers import CollegeController


@bp.route('/course')
@bp.route('/course/<course_id>')
def course(course_id=''):
    courses = CollegeController.get_courses()
    course = None
    if course_id != '':
        course = CollegeController.get_course(course_id)
    return render_template('course.html', courses=courses, course=course)


@bp.route('/course/create', methods=['GET', 'POST'])
def create_course():
    user_id = session['user_id']
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        course = CollegeController.create_course(name,description)
        if course:
            flash('Course already exists!', category='error')

            return redirect(url_for('chats.chat'))
    return render_template('create_course.html')
