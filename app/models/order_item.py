from app.models import db

class OrderItem(db.Model):
    __tablename__ = 'order_item'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu_item.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    @classmethod
    def create(cls, order_id, menu_item_id, quantity, price):
        new_item = cls(
            order_id=order_id,
            menu_item_id=menu_item_id,
            quantity=quantity,
            price=price
        )
        db.session.add(new_item)
        db.session.commit()
        return new_item

    @classmethod
    def get_by_id(cls, item_id):
        return cls.query.get(item_id)
        
    @classmethod
    def get_by_order(cls, order_id):
        return cls.query.filter_by(order_id=order_id).all()
