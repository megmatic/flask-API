from flask import Flask, render_template

app = Flask(__name__)
posts = [
    {
        'author': 'Megggg',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 1st, 2021'
    },
    {
        'author': 'Jimmyyyyyy',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 2nd, 2021'
    }
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title='About')


if __name__ == '__main__':
    app.run(debug=True)
