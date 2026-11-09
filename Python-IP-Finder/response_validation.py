import requests


def validate_ipwhois_response(data):
    """
    Validate the JSON response received from ipwho.is.
    """

    # Check whether the response is a dictionary
    if not isinstance(data, dict):
        raise ValueError("Invalid API response format.")

    # Check API-level success
    if data.get("success") is not True:
        message = data.get("message", "Unknown API error")
        raise ValueError(f"IP lookup failed: {message}")

    # Check required fields
    required_fields = ["ip", "country", "city"]

    for field in required_fields:
        if not data.get(field):
            raise ValueError(
                f"API response is missing required field: {field}"
            )

    return data

def test_failed_response():

    fake_response = {
        "success": False,
        "message": "Invalid IP address"
    }

    try:
        validate_ipwhois_response(fake_response)

    except ValueError as error:
        print("EXPECTED ERROR:", error)


if __name__ == "__main__":
    test_failed_response()

def test_missing_field():

    fake_response = {
        "success": True,
        "ip": "8.8.8.8",
        "country": "United States"
        # city is missing
    }

    try:
        validate_ipwhois_response(fake_response)

    except ValueError as error:
        print("EXPECTED ERROR:", error)


if __name__ == "__main__":
    test_missing_field()