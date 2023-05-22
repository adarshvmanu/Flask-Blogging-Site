from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blogposts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model
class blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(100), nullable=False)
    blog_subtitle = db.Column(db.String(50))
    blog_content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

    def __repr__(self): 
        return 'Blog post ' + str(self.id)    


# Routes
@app.route('/')
def index():
    all_blogs = blogpost.query.order_by(blogpost.date_created.desc()).all()
    return render_template('index.html', blogs=all_blogs)

@app.route('/<int:id>')
def blog(id):
    blog = blogpost.query.filter_by(id=id).one()
    return render_template('blog.html', blog=blog)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/add_blog', methods=['POST'])
def add_blog():
    if request.method == 'POST':
        title = request.form['blog_title']
        subtitle = request.form['blog_subtitle']
        content = request.form['blog_content']
        new_blog = blogpost(blog_title=title, blog_subtitle=subtitle, blog_content=content, date_created=datetime.now())
        db.session.add(new_blog)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/admin')
def admin():
    all_blogs = blogpost.query.order_by(blogpost.date_created.desc()).all()
    return render_template('admin.html', blogs=all_blogs)

if __name__ == '__main__':
    app.run(debug=True)