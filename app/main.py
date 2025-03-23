from flask import Flask, jsonify
from app.db import init_app, db
from app.data_model import User

app = Flask(__name__)
init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return jsonify({"message": "Flask App Running!"})

@app.route('/add_user/<username>')
def add_user(username):
    user = User(username=username)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": f"User {username} added."})

@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    user_list = [{"id": user.id, "username": user.username} for user in users]
    return jsonify(user_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)