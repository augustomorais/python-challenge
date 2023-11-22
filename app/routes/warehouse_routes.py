from flask import Blueprint, request, jsonify
from ..models.warehouse import Warehouse
from ..utils.database import db

warehouse_blueprint = Blueprint('warehouse_blueprint', __name__)

@warehouse_blueprint.route('/warehouses', methods=['POST'])
def create_warehouse():
    data = request.json
    new_warehouse = Warehouse(
        name=data['name'],
        latitude=data['latitude'],
        longitude=data['longitude']
    )
    db.session.add(new_warehouse)
    db.session.commit()
    return jsonify(new_warehouse.to_dict()), 201

@warehouse_blueprint.route('/distance/<int:warehouse_id>/<int:customer_id>', methods=['GET'])
def calculate_distance_endpoint(warehouse_id, customer_id):
    warehouse = Warehouse.query.get_or_404(warehouse_id)
    customer = Customer.query.get_or_404(customer_id)
    distance = calculate_distance(warehouse.latitude, warehouse.longitude, customer.latitude, customer.longitude)
    return jsonify({'distance_km': distance})
