from flask import Flask, render_template, url_for
app = Flask(__name__)

names = [
    {
        'name': 'Zymiere Hargrove',
        'location': 'Room 46',
        'stauts': 'Present',
    },
    {
        'name': 'Zymiere Hargrove',
        'location': 'Room 46',
        'stauts': 'Present',
    },

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', names=names)


@app.route("/admin")
def admin():
    return render_template(admin.html', title=Admin Page')


@app.route("/student")
def student():
    return render_template(student.html', title=Student Page')


@app.route("/login")
def login():
    return render_template(login.html', title=Admin Login')

if __name__ == '__main__':
    app.run(debug=True)