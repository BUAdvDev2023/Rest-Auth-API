from flask import Flask, request, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = '4XAYDw85W5u4J2KzGBEXwOazMYSdUwz99A97E2BBC84E9EE75369CEA65ECF2'
# Run Production
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@db:3306/db'
# Run Locally
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
    email = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(512))
    full_name = db.Column(db.String(128), default='')
    address = db.Column(db.String(256), default='')
    phone_number = db.Column(db.String(16), default='')
    date_of_birth = db.Column(db.Date)
    profile_picture = db.Column(db.String(256), default='')
    is_active = db.Column(db.Boolean, default=True)
    role = db.Column(db.String(32), default='customer')
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def update(self, fields):
        for field, value in fields.items():
            if value is not None and value != '':
                setattr(self, field, value)

    def is_customer(self):
        return self.role == 'customer'

with app.app_context():
    db.create_all()


@app.route('/api/login', methods=['POST'])
def login():
    try:
        username = request.json.get('username')
        password = request.json.get('password')

        user = User.query.filter_by(username=username).first()

        if user and user.verify_password(password):
            return jsonify({ 'username': user.username }), 201, {'Location': url_for('get_user', id = user.id, _external = True)}
        else:
            return jsonify({'error': 'Invalid username or password'}), 401
    except Exception as e:
        return jsonify({'error': f'An error occurred during login: {str(e)}'}), 500


@app.route('/api/users', methods=['POST'])
def new_user():
    try:
        username = request.json.get('username')
        password = request.json.get('password')
        if username is None or password is None:
            return jsonify({'error': 'Username and password are required'}), 400

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({'error': 'Username already in use. Try another username.'}), 400

        user = User(username=username)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return jsonify({ 'username': user.username }), 201, {'Location': url_for('get_user', id = user.id, _external = True)}
    except Exception as e:
        return jsonify({'error': f'An error occurred while creating a new user: {str(e)}'}), 500
    
@app.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    try:
        user = User.query.get(id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        return jsonify({'username': user.username})
    except Exception as e:
        return jsonify({'error': f'An error occurred while fetching user: {str(e)}'}), 500
    
@app.route('/api/users/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        user = User.query.get(id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        data = request.json
        update_fields = {
            'email': data.get('email', user.email),
            'full_name': data.get('full_name', user.full_name),
            'address': data.get('address', user.address),
            'phone_number': data.get('phone_number', user.phone_number),
            'date_of_birth': data.get('date_of_birth', user.date_of_birth),
            'profile_picture': data.get('profile_picture', user.profile_picture),
        }

        user.update(update_fields)

        db.session.commit()
        return jsonify({'username': user.username}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred while updating user: {str(e)}'}), 500


@app.route('/api/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.get(id)
        if not user:
            return jsonify({'error': 'User not found'}), 404

        db.session.delete(user)
        db.session.commit()
        return jsonify({'result': True}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred while deleting user: {str(e)}'}), 500
        
        
@app.route('/api/users/<string:username>', methods=['GET'])
def get_user_username(username):
    try:
        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify({'error': 'User not found'}), 404
        return jsonify({'username': user.username})
    except Exception as e:
        return jsonify({'error': f'An error occurred while fetching user: {str(e)}'}), 500
    
@app.route('/api/users/<string:username>', methods=['PUT'])
def update_user_username(username):
    try:
        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify({'error': 'User not found'}), 404

        data = request.json
        update_fields = {
            'email': data.get('email', user.email),
            'full_name': data.get('full_name', user.full_name),
            'address': data.get('address', user.address),
            'phone_number': data.get('phone_number', user.phone_number),
            'date_of_birth': data.get('date_of_birth', user.date_of_birth),
            'profile_picture': data.get('profile_picture', user.profile_picture),
        }

        user.update(update_fields)

        db.session.commit()
        return jsonify({'username': user.username}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred while updating user: {str(e)}'}), 500


@app.route('/api/users/<string:username>', methods=['DELETE'])
def delete_user_username(username):
    try:
        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify({'error': 'User not found'}), 404

        db.session.delete(user)
        db.session.commit()
        return jsonify({'result': True}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred while deleting user: {str(e)}'}), 500


if __name__ == '__main__':
    # Dev
    # app.run(host='0.0.0.0', port=6525, debug=True)
    # Prod
    app.run(host='0.0.0.0', port=6525)