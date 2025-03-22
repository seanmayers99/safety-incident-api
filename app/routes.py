from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from . import db
from .models import Incident

main = Blueprint('main', __name__)

@main.route('/incidents', methods=['POST'])
@jwt_required()
def add_incident():
    data = request.get_json()
    new_incident = Incident(**data)
    db.session.add(new_incident)
    db.session.commit()
    return jsonify({"message": "Incident added"}), 201

@main.route('/incidents', methods=['GET'])
def get_incidents():
    incidents = Incident.query.all()
    return jsonify([{
        "id": i.id,
        "title": i.title,
        "description": i.description,
        "severity": i.severity,
        "reporter": i.reporter
    } for i in incidents])
