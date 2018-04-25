"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)




@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')
    print github

    first, last, github = hackbright.get_student_by_github(github)
    title_grade = hackbright.get_grades_by_github(github)


	# first, last, github = hackbright.get_student_by_github(github)
	# lst = hackbright.get_grades_by_github(github)

    # first, last, github = hackbright.get_student_by_github(github)

	
	# lst = hackbright.get_grades_by_github(github)


    html = render_template("student_info.html",
    						first=first,
    						last=last,
    						github=github,
    						title_grade=title_grade)

    return html

@app.route('/test')
def test(github):
	github = 'jhacks'
	first, last, github = hackbright.get_student_by_github(github)
	lst = hackbright.get_grades_by_github(github)
	print "hello"

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student-add-form")
def student_creation():
	"""Takes user to student add form"""

	return render_template("student_creation.html")


@app.route("/student-add", methods=['POST'])
def add_student():
	"""Add student"""

	first = request.form.get("first")
	print str(first)
	last = request.form.get("last")
	github = request.form.get("github")

	hackbright.make_new_student(first, last, github)


	return render_template("student_added.html",
							github=str(github))



if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
