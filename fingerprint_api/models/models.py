from fingerprint_api import db

class Fingerprint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_agent = db.Column(db.String(512), nullable=False)
    browser = db.Column(db.String(50), nullable=False)
    os = db.Column(db.String(50), nullable=False)
    murmur_hash = db.Column(db.String(512), nullable=False)

    def __init__(self, user_agent, browser, os, murmur_hash):
        self.user_agent = str(user_agent)
        self.browser = str(browser)
        self.os = str(os)
        self. murmur_hash = str(murmur_hash)

    def __repr__(self):
        return f"Fingerprint('{self.user_agent_string}', '{self.browser}', '{self.os}', {self.murmur_hash})"

