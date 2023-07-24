from flask import Blueprint, request, jsonify
from user_agents import parse
from fingerprint_api.models import Fingerprint
from fingerprint_api import db
import mmh3

fingerprint_blueprint = Blueprint('fingerprint', __name__)


@fingerprint_blueprint.route('/api/fingerprint', methods=['POST', 'GET'])
def fingerprint():
    user_agent = request.headers.get('User-Agent')
    # Implement fingerprinting logic here to extract OS and browser from the user_agent
    ua = parse(user_agent)
    os = ua.os.family
    browser = ua.browser.family

    murmur_hash = mmh3.hash64(f"{user_agent}")

    # Store the fingerprint in the database
    fingerprint = Fingerprint(user_agent=user_agent, murmur_hash=murmur_hash, os=os, browser=browser)
    db.session.add(fingerprint)
    db.session.commit()

    return jsonify({'message': 'Fingerprint recorded successfully.'})
