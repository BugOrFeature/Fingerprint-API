# Fingerprint API

The Fingerprint API is a basic Flask-based web application that provides fingerprinting capabilities to extract OS and browser information from user agents. It allows you to gather information about clients accessing the API and store their fingerprint data in a SQLite database.

## Features

- Extracts OS and browser information from user agents.
- Stores fingerprint data in a SQLite database.
- Provides an API endpoint for recording fingerprints.
- The application uses the [Murmur3](https://github.com/hajimes/mmh3) mmh3.hash64() hashing algorithm to fingerprint the User-Agent.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your_username/fingerprint-api.git
cd fingerprint-api
```

2. Download poetry:
```bash
curl -sSL https://install.python-poetry.org | python -
```

3. Install the required dependencies using Poetry:

```bash
poetry install
```

4. Create a `.env` file in the root directory of the project and set the `SECRET_KEY`:

```
SECRET_KEY=your_secret_key_here
```

5. Run the development server:

```bash
poetry run python3 app.py
```

## Usage

Once the development server is running, you can access the API at `http://127.0.0.1:5000`.

### Record Fingerprint

To record a fingerprint, send a GET or POST request to the `/api/fingerprint` endpoint with the user agent data in the request headers. The API will extract the OS and browser information and save the fingerprint to the database.

Example using cURL:

```bash
curl -X POST http://127.0.0.1:5000/fingerprint -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
