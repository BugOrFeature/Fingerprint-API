from fingerprint_api import db
import mmh3
import base64

class Fingerprint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_agent = db.Column(db.String(512), nullable=False)
    browser = db.Column(db.String(50), nullable=False)
    browser_version = db.Column(db.String(50), nullable=False)
    device = db.Column(db.String(50), nullable=False)
    device_brand = db.Column(db.String(50), nullable=False)
    device_model = db.Column(db.String(50), nullable=False)
    os = db.Column(db.String(50), nullable=False)
    murmur_hash = db.Column(db.String(512), nullable=False)
    remote_addr = db.Column(db.String(50), nullable=False)

    def __init__(self,ua, user_agent, remote_addr):
        self.user_agent = str(user_agent)
        self.browser = str(ua.browser.family)
        self.browser_version = str(ua.browser.version_string)
        self.device = str(ua.device.family)
        self.device_brand = str(ua.device.brand)
        self.device_model = str(ua.device.model)
        self.os = str(ua.os.family)
        self.murmur_hash = self.hash(user_agent)
        self.remote_addr = str(remote_addr)

    @staticmethod
    def hash(input_string):
        mm_hash = mmh3.hash128(input_string.encode('utf-8'), signed=False).to_bytes(16, byteorder='big', signed=False)
        # hash128, return two values each of 8 bytes, we just flip the order here to make it consistent.
        hash = mm_hash[8:] + mm_hash[:8]
        return base64.urlsafe_b64encode(hash).decode('utf-8').strip("=")
        

    def __repr__(self):
        return f'''Fingerprint(
        User-Agent: {self.user_agent},
        Browser: {self.browser},
        Browser-version: {self.browser_version},
        Device: {self.device},
        Device-brand: {self.device_brand},
        Device-model: {self.device_model},
        OS: {self.os},
        Murmur-hash: {self.murmur_hash},
        Remote-addr: {self.remote_addr}
        )'''

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}



