from flask import Blueprint, request, jsonify
from ..models.customer import Customer
from ..utils.database import db

customer_blueprint = Blueprint('customer_blueprint', __name__)

@customer_blueprint.route('/customers', methods=['POST'])
def create_customer():
    data = request.json
    new_customer = Customer(
        name=data['name'],
        latitude=data['latitude'],
        longitude=data['longitude']
    )
    db.session.add(new_customer)
    db.session.commit()
    return jsonify(new_customer.to_dict()), 201
