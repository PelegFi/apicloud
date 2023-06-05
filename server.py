from flask import Flask , request
from flask_cors import CORS
from flask_restful import Api , Resource
from models.db import db
from models.dishe_category  import Category , Dish

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://database_user:JMWXbcm3@tesetdatabase.postgres.database.azure.com/postgres'

app.config['SECRET_KEY']='hjvgsadf'
CORS(app)
db.init_app(app)
api=Api(app)

with app.app_context():
    db.create_all()


class categoriesALL(Resource):
    def get(self):
        categories=Category.query.all()
        categorylist=[category.serialize() for category in categories]
        return categorylist
    
class categoriesONE(Resource):
    def get(self):
        category_id = request.args.get('category_id')

        if category_id:
            current_category = Category.query.filter_by(id=category_id).first()
            dishes_list = [dish.serialize() for dish in current_category.dishes]
        else:
            all_dishes = Dish.query.all()
            dishes_list = [dish.serialize() for dish in all_dishes]
        return dishes_list


        
    
api.add_resource(categoriesALL , '/categories')
api.add_resource(categoriesONE , '/dishes')


app.run(debug=True , host="0.0.0.0")