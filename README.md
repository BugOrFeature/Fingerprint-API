# Fingerprint API

The Fingerprint API is a basic Flask-based web application that provides fingerprinting capabilities to extract OS and browser information from user agents. It allows you to gather information about clients accessing the API and store their fingerprint data in a SQLite database.

## Features

- Extracts OS and browser information from user agents.
- Stores fingerprint data in a SQLite database.
- Provides an API endpoint for recording fingerprints.
- The application uses the [Murmur3](https://github.com/hajimes/mmh3) mmh3.hash128() hashing algorithm to fingerprint the User-Agent.

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

Once the development server is running, you can access the API at `https://127.0.0.1:5000`.

### Record Fingerprint

To record a fingerprint, send a GET or POST request to the `/api/fingerprint` endpoint with the user agent data in the request headers. The API will extract the OS and browser information and save the fingerprint to the database.

Example using cURL:
We use the -k parameter because we are using a self-signed certificate. This option explicitly allows curl to perform “insecure” SSL connections and transfers.
```bash
curl -k -X POST https://127.0.0.1:5000/api/fingerprint -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3" 
```

Response:
```json
{
  "message": "Fingerprint recorded successfully.",
  "result": {
    "browser": "Chrome",
    "browser_version": "58.0.3029",
    "device": "Other",
    "device_brand": "None",
    "device_model": "None",
    "id": 1,
    "murmur_hash": "n89jiMmRHC5kFDGQdcN15w",
    "os": "Windows",
    "remote_addr": "127.0.0.1",
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
  }
}
```

Database:
Table - fingerprint
| id |                                                     user_agent                                                     | browser | browser_version | device | device_brand | device_model | os      | murmur_hash            | remote_addr |
|:--:|:------------------------------------------------------------------------------------------------------------------:|:-------:|:---------------:|--------|--------------|--------------|---------|------------------------|-------------|
| 1  | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3 | Chrome  | 58.0.3029       | Other  | None         | None         | Windows | n89jiMmRHC5kFDGQdcN15w | 127.0.0.1   |

## Additional browser information to fingerprint (todos)
* language
* color-depth
* hardware-concurrency
* screen-resolution
* time-zone
* storage-info
* cpuClass
* platform
* plugins
* canvas
* webGL
* touchSupport
* fonts

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
