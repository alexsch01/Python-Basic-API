from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [ 
    {
        'author': "Person1",
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date': 'May 3, 2019'
    },
    {
        'author': "Mary Jane",
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date': 'May 4, 2019'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title="About")

if __name__ == '__main__':
    app.run(debug=True)
