from response_validation import validate_ipwhois_response


def test_success_response():

    data = {
        "success": True,
        "ip": "8.8.8.8",
        "country": "United States",
        "city": "Mountain View"
    }

    result = validate_ipwhois_response(data)

    assert result["ip"] == "8.8.8.8"

    print("PASS: Successful response accepted.")


def test_failed_response():

    data = {
        "success": False,
        "message": "Invalid IP address"
    }

    try:
        validate_ipwhois_response(data)

    except ValueError:
        print("PASS: Failed API response rejected.")

    else:
        raise AssertionError("Failed response was accepted.")


def test_missing_field():

    data = {
        "success": True,
        "ip": "8.8.8.8",
        "country": "United States"
    }

    try:
        validate_ipwhois_response(data)

    except ValueError:
        print("PASS: Missing field detected.")

    else:
        raise AssertionError("Incomplete response was accepted.")


def test_invalid_format():

    data = ["8.8.8.8", "United States"]

    try:
        validate_ipwhois_response(data)

    except ValueError:
        print("PASS: Invalid response format rejected.")

    else:
        raise AssertionError("Invalid response format was accepted.")


if __name__ == "__main__":

    test_success_response()
    test_failed_response()
    test_missing_field()
    test_invalid_format()

    print("\nAll response validation tests completed.")
    