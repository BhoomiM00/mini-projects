# Python IP Finder

A Python command-line application that detects your public IP address and retrieves approximate geolocation information using public APIs.

## Features

- Manual IPv4 and IPv6 address lookup
- Automatic public IP detection using ipify
- IP address validation using Python's `ipaddress` module
- Geolocation lookup using ipwho.is
- API response validation
- HTTP error and exception handling
- Professional command-line output
- Modular application structure

## Technologies Used

- Python
- Requests
- ipaddress
- ipify API
- ipwho.is API

## Project Structure

```text
Python-IP-Finder/
├── ip_finder.py
├── api_request.py
├── response_validation.py
├── output_formatter.py
├── tests/
│   ├── test_error_scenarios.py
│   └── test_response_validation.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Clone the repository and navigate to this project folder.

```bash
git clone YOUR_REPOSITORY_URL
cd mini-projects/Python-IP-Finder
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the Application

```bash
python ip_finder.py
```

Choose from the application menu:

1. Enter IP manually
2. Detect public IP automatically
3. Exit

## Run Tests

From the `Python-IP-Finder` folder:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## APIs Used

- [ipify](https://www.ipify.org/) – Public IP detection
- [ipwho.is](https://ipwho.is/) – IP geolocation information

## Important Notes

- IP geolocation is approximate and may not identify an exact physical location.
- Public API availability and rate limits may affect lookups.
- Never commit passwords, API secrets, or personal information.

## Learning Outcomes

This project helped me practise:

- Python functions and modules
- HTTP requests and REST APIs
- Exception handling
- JSON parsing
- IPv4 and IPv6 validation
- API response validation
- Unit testing and mocking
- Git and GitHub project management
