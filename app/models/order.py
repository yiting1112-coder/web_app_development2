from datetime import datetime
from app.models import db

class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    status = db.Column(db.String(20), default='pending', nullable=False)
    total_price = db.Column(db.Integer, nullable=False)
    pickup_time = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    items = db.relationship('OrderItem', backref='order', lazy=True, cascade="all, delete-orphan")

    @classmethod
    def create(cls, user_id, restaurant_id, total_price, pickup_time, status='pending'):
        new_order = cls(
            user_id=user_id,
            restaurant_id=restaurant_id,
            total_price=total_price,
            pickup_time=pickup_time,
            status=status
        )
        db.session.add(new_order)
        db.session.commit()
        return new_order

    @classmethod
    def get_by_id(cls, order_id):
        return cls.query.get(order_id)

    @classmethod
    def get_by_user(cls, user_id):
        return cls.query.filter_by(user_id=user_id).order_by(cls.created_at.desc()).all()
        
    @classmethod
    def get_by_restaurant(cls, restaurant_id):
        return cls.query.filter_by(restaurant_id=restaurant_id).order_by(cls.created_at.desc()).all()

    def update_status(self, new_status):
        self.status = new_status
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
