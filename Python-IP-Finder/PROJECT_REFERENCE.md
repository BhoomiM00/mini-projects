# Python IP Finder – Project Reference Guide

This document explains the project architecture, Python imports, functions, APIs, error handling, testing, and important concepts for future revision.

---

## 1. Project Overview

Python IP Finder is a command-line application that:
- Accepts an IP address manually.
- Automatically detects the public IP address.
- Validates IPv4 and IPv6 addresses.
- Retrieves approximate IP geolocation information.
- Handles HTTP errors and invalid API responses.
- Displays results in a formatted terminal output.

## 2. Technologies and Libraries

| Library / Technology | Purpose |
|---|---|
| Python | Main programming language |
| requests | Sending HTTP requests to APIs |
| ipaddress | IP address validation and classification |
| ipify API | Detecting the public IP address |
| ipwho.is API | Retrieving IP geolocation information |

### Built-in vs External Libraries

- `ipaddress`: Python standard library; no installation required.
- `requests`: External library; installed using pip.

Installation:

```powershell
python -m pip install requests
```

## 3. Project Architecture

### ip_finder.py

Purpose: Main application file.

Responsibilities:
- Display the application menu.
- Accept user input.
- Perform manual IP lookup.
- Perform automatic public IP detection.
- Coordinate API requests and response validation.
- Display results.

Important functions:
- `manual_ip_lookup()` – Handles manual IP input and validation.
- `automatic_ip_lookup()` – Detects the public IP automatically.
- `lookup_ip_information(ip)` – Retrieves information about an IP address.
- `main()` – Controls the application workflow.

### api_request.py

Purpose: Centralized API request handling.

Important function:

`make_api_request(url)`

Responsibilities:
- Send HTTP GET requests.
- Set request timeout.
- Check HTTP status codes.
- Parse JSON responses.
- Handle timeout, connection, HTTP, JSON, and general request exceptions.
- Return API data or `None` when a request fails.

Important concepts:
- `requests.get()`
- `timeout`
- `response.status_code`
- `response.raise_for_status()`
- `response.json()`
- `try` and `except`

### response_validation.py

Purpose: Validate API responses before using their data.

Important function:

`validate_ipwhois_response(data)`

Responsibilities:
- Confirm that the response is a dictionary.
- Check the API success field.
- Check required fields.
- Raise a `ValueError` for invalid responses.
- Return validated data.

Important concepts:
- `isinstance()`
- `dict`
- `.get()`
- `raise ValueError`
- Exception handling

### output_formatter.py

Purpose: Keep terminal output organized and readable.

Functions:
- `print_header()` – Displays the application heading.
- `print_section(title)` – Displays section headings.
- `print_field(label, value)` – Displays formatted information.
- `print_success(message)` – Displays success messages.
- `print_error(message)` – Displays error messages.
- `print_footer()` – Displays the application footer.
- `display_ip_info(data)` – Displays IP geolocation information.

Nested API data examples:

```python
connection = data.get("connection") or {}
isp = connection.get("isp")

timezone = data.get("timezone") or {}
timezone_id = timezone.get("id")
```

## 4. API Reference

### API 1: ipify

Endpoint:

```text
https://api.ipify.org?format=json
```

Purpose: Detect the public IP address of the current internet connection.

Example JSON:

```json
{
    "ip": "203.0.113.10"
}
```

Note: The example IP is reserved for documentation and is not a real public IP.

### API 2: ipwho.is

Endpoint:

```text
https://ipwho.is/{ip}
```

Purpose: Retrieve approximate geographical and network information.

Information may include:
- IP address
- Country
- Region
- City
- ISP
- Timezone
- Connection information

Important: Geolocation is approximate and does not identify an exact physical location.

## 5. Important Python Concepts Used

| Concept | Explanation |
|---|---|
| Import | Makes modules and functions available |
| Function | Reusable block of code |
| Parameter | Input accepted by a function |
| Return | Sends a result back to the caller |
| Dictionary | Stores data as key-value pairs |
| `.get()` | Safely retrieves a dictionary value |
| Exception | An error detected during execution |
| `try-except` | Handles exceptions |
| `raise` | Manually raises an exception |
| `None` | Represents the absence of a value |
| Module | A Python file containing reusable code |

## 6. HTTP and API Concepts

- HTTP GET: Requests data from a server.
- HTTP 200: Successful request.
- HTTP 400: Bad request.
- HTTP 401: Unauthorized.
- HTTP 403: Forbidden.
- HTTP 404: Resource not found.
- HTTP 429: Too many requests.
- HTTP 500: Internal server error.
- HTTP 503: Service unavailable.

Remember: HTTP success does not always mean the API operation succeeded. An API can return HTTP 200 with `"success": false` in its JSON response.

## 7. IP Address Concepts

- IPv4: 32-bit IP address.
- IPv6: 128-bit IP address.
- Private IP: Used inside private networks.
- Public IP: Globally addressable IP space.
- `ipaddress.ip_address()`: Parses and validates an IP address.
- `is_global`: Indicates whether an address is globally scoped according to Python's IP classification rules.

Important: An IP being classified as global does not prove that it is reachable.

## 8. Testing

Test files:

```text
tests/
├── __init__.py
├── test_error_scenarios.py
└── test_response_validation.py
```

Run the tests:

```powershell
python -m tests.test_response_validation
python -m tests.test_error_scenarios
```

Testing areas:
- Valid IP addresses.
- Invalid IP addresses.
- IPv4 and IPv6.
- Private and global IP classification.
- API timeout.
- Connection errors.
- HTTP errors.
- Invalid JSON.
- API response validation.

## 9. Application Workflow

1. User starts the application.
2. Main menu is displayed.
3. User chooses manual lookup or automatic detection.
4. IP address is validated.
5. API request is performed.
6. API response is checked.
7. Information is formatted.
8. Results are displayed.
---

**Revision tip:** Update this document whenever you add a new function, import, module, API, or feature. Keep actual function signatures and test names synchronized with the source code.
