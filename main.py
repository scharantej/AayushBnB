 
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

# Create a Flask app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aayushbnb.db'
app.config['SECRET_KEY'] = 'super secret key'
db = SQLAlchemy(app)

# Define the User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Define the Property model
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

# Create the login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Create the database tables
db.create_all()

# Define the routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('properties'))
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('properties'))
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('properties'))
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('login.html')

@app.route('/properties')
@login_required
def properties():
    properties = Property.query.all()
    return render_template('properties.html', properties=properties)

@app.route('/property/<int:property_id>')
@login_required
def property_details(property_id):
    property = Property.query.get_or_404(property_id)
    return render_template('property_details.html', property=property)

@app.route('/book', methods=['POST'])
@login_required
def book():
    property_id = request.form['property_id']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    num_guests = request.form['num_guests']
    # Add booking logic here
    flash('Booking successful!', 'success')
    return redirect(url_for('properties'))

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
