from models.db import db 

class Category(db.Model):
    __tablename__ = 'Category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    image = db.Column(db.Text)

    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "image":self.image
        }

class Dish(db.Model):
    __tablename__ = 'Dish'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, default="")
    image = db.Column(db.Text, default="")
    is_gluten_free = db.Column(db.Boolean, default=False)
    is_vegeterian = db.Column(db.Boolean, default=False)
    category_id_id = db.Column(db.Integer, db.ForeignKey('Category.id'))
    category = db.relationship('Category', backref=db.backref('dishes'))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "price": self.price,
            "description": self.description,
            "is_gluten_free": self.is_gluten_free,
            "is_vegeterian": self.is_vegeterian,
            "category_id_id": self.category_id_id
        }


