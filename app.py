from fingerprint_api import create_app

app = create_app()

if __name__ == "__main__":
    # For development purposes, use a self-signed SSL certificate
    app.run(ssl_context='adhoc', debug=True)
