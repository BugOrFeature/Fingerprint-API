from flask import Blueprint, request, jsonify
from user_agents import parse
from fingerprint_api.models import Fingerprint
from fingerprint_api import db

fingerprint_blueprint = Blueprint('fingerprint', __name__)


@fingerprint_blueprint.route('/api/fingerprint', methods=['POST', 'GET'])
def fingerprint():
    user_agent = request.headers.get('User-Agent')
    # Implement fingerprinting logic here to extract OS and browser from the user_agent
    ua = parse(user_agent)

    # Store the fingerprint in the database
    fingerprint = Fingerprint(ua=ua, user_agent=user_agent, remote_addr=request.remote_addr)

    db.session.add(fingerprint)
    db.session.commit()

    return jsonify({'message': 'Fingerprint recorded successfully.',
    'result': fingerprint.as_dict()
    })
