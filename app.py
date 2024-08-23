from flask import Flask, render_template

app = Flask(__name__)

# Dados simulados para os cursos
courses = [
    {"id": 1, "title": "Curso de Python", "description": "Aprenda Python do básico ao avançado.", "instructor": "João Silva"},
    {"id": 2, "title": "Curso de HTML e CSS", "description": "Domine a criação de páginas web.", "instructor": "Maria Souza"},
    {"id": 3, "title": "Curso de Flask", "description": "Desenvolva aplicações web com Flask.", "instructor": "Carlos Oliveira"}
]

@app.route('/')
def index():
    return render_template('index.html', courses=courses)

@app.route('/course/<int:course_id>')
def course(course_id):
    course = next((c for c in courses if c["id"] == course_id), None)
    return render_template('course.html', course=course)

if __name__ == '__main__':
    app.run(debug=True)
