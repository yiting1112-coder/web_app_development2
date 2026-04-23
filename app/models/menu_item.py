from datetime import datetime
from app.models import db

class MenuItem(db.Model):
    __tablename__ = 'menu_item'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Integer, nullable=False)
    is_available = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    order_items = db.relationship('OrderItem', backref='menu_item', lazy=True)

    @classmethod
    def create(cls, restaurant_id, name, price, description=None, is_available=True):
        new_item = cls(
            restaurant_id=restaurant_id, 
            name=name, 
            price=price, 
            description=description, 
            is_available=is_available
        )
        db.session.add(new_item)
        db.session.commit()
        return new_item

    @classmethod
    def get_by_id(cls, item_id):
        return cls.query.get(item_id)

    @classmethod
    def get_all_by_restaurant(cls, restaurant_id):
        return cls.query.filter_by(restaurant_id=restaurant_id).all()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
