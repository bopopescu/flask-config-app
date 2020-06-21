from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)


class Member(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True)
	password = db.Column(db.String(20))
	email = db.Column(db.String(30))
	joined_date = db.Column(db.DateTime)

	orders = db.relationship('Order', backref='member', lazy='True')

	def __repr__(self):
		return '<Member %r>' % self.username

class Order(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	price = db.Column(db.Integer)
	member_id = db.Column(db.Integer, db.ForeignKey('member.id'))


@app.route('/base')
def base():
	return render_template('base.html')


if __name__ == '__main__':
	app.run(debug=True)