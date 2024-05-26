from flask import Flask, render_template, request,redirect, url_for
from Homework35_model import db, Cars
import psycopg2
app = Flask(__name__)

HOST = 'localhost'
PORT = 5432
DATABASE = 'flask_db'
USER = 'postgres'
PASSWORD = 'XX132Files'

app.secret_key = 'secret'

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    all_data = Cars.query.all()

    return render_template('index.html', cars= all_data)

@app.route('/insert', methods=["POST"])
def insert():
    if request.method == "POST":
        manufacturer = request.form['manufacturer']
        model = request.form['model']
        instock = request.form['instock']
        price = request.form['price']

        car_data = Cars(manufacturer,model,instock,price)
        db.session.add(car_data)
        db.session.commit()
        return redirect(url_for('index'))



@app.route('/edit/<id>/', methods=["GET","POST"])
def edit(id):
    car_data = Cars.query.get(id)
    car_data.manufacturer = request.form['manufacturer']
    car_data.model = request.form['model']
    car_data.instock = request.form['instock']
    car_data.price = request.form['price']
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
