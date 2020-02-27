from flask import Flask,request,render_template
import config

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
Base = declarative_base()


class Blog(db.Model):
    __tablename__ = 'blog'
    id  = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=True)


db.create_all()


@app.route('/Query/',methods=['POST','GET'])
def index():
    # #新增
    # blog = Blog(title="first blog",content="this is my first blog")
    # db.session.add(blog)
    # db.session.commit()

    # 查询
    # res =Blog.query.filter(Blog.title=="first blog")[0]

    # res =Blog.query.filter(Blog.title=="first blog").first()
    # print(res.content)
    #  #修改
    # blog_edit = Blog.query.filter(Blog.title=="first blog").first()
    # blog_edit.content = "Modified by Ruihua Sun"
    # db.session.commit()
    # #删除
    # blog_delete  = Blog.query.filter(Blog.title=="first blog").first()
    # db.session.delete(blog_delete)
    # db.session.commit()

    res = Blog.query.all()
    for r in res:
        print('%s\t\t%s\r\n'%(r.title,r.content))
    return render_template('query.html',result = res)


@app.route('/Add/', methods=['POST','GET'])
def Add():
    if (request.method == 'POST'):
        # 新增
        blog = Blog(title=request.form['Title'], content=request.form['Content'])
        db.session.add(blog)
        db.session.commit()
    else:
        # 新增
        blog = Blog(title=request.args.get('Title'), content=request.args.get('Content'))
        db.session.add(blog)
        db.session.commit()
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)