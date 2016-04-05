import sqlite3
from contextlib import closing
from datetime import datetime
from flask import Flask,request, session, g, redirect, \
				url_for, abort, render_template, flash

# configuration
DATABASE = './test.db'
DEBUG = True
SECRET_KEY = 'development key'

# create application
app = Flask(__name__)
app.config.from_object(__name__)

# database things
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

def init_db():
	with closing(connect_db()) as db:
		with app.open_resource('schema.sql',mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

@app.before_request
def before_request():
	g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
	db = getattr(g,'tb',None)
	if db is not None:
		db.close()

@app.route('/')
def show_msgs():
	cur = g.db.execute('select name,comment,time from Message order by id desc')
	msgs = [dict(name=row[0],comment=row[1],time=row[2]) for row in cur.fetchall()]
	return render_template('show_msgs.html',entries=msgs)

@app.route('/add',methods=['POST'])
def add_msg():
	data = [request.form['name'],request.form['comment'],str(datetime.now())]
	g.db.execute('insert into Message(name,comment,time) values (?,?,?)',data)
	g.db.commit()
	flash('New comment was successfully posted!')
	return redirect(url_for('show_msgs'))
	
if __name__ == '__main__':
	app.run()