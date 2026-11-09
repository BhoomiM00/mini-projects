import requests
from unittest.mock import Mock, patch

from api_request import make_api_request


def test_timeout():

    with patch(
        "requests.get",
        side_effect=requests.exceptions.Timeout
    ):
        print("\nTEST: TIMEOUT")

        result = make_api_request("https://example.com")

        assert result is None
        print("PASS: Timeout handled correctly.")


def test_connection_error():

    with patch(
        "requests.get",
        side_effect=requests.exceptions.ConnectionError
    ):
        print("\nTEST: CONNECTION ERROR")

        result = make_api_request("https://example.com")

        assert result is None
        print("PASS: Connection error handled correctly.")


def test_http_429():

    fake_response = Mock()
    fake_response.status_code = 429

    fake_response.raise_for_status.side_effect = (
        requests.exceptions.HTTPError(
            "429 Too Many Requests",
            response=fake_response
        )
    )

    with patch("requests.get", return_value=fake_response):

        print("\nTEST: HTTP 429")

        result = make_api_request("https://example.com")

        assert result is None
        print("PASS: HTTP 429 handled correctly.")


def test_http_500():

    fake_response = Mock()
    fake_response.status_code = 500

    fake_response.raise_for_status.side_effect = (
        requests.exceptions.HTTPError(
            "500 Internal Server Error",
            response=fake_response
        )
    )

    with patch("requests.get", return_value=fake_response):

        print("\nTEST: HTTP 500")

        result = make_api_request("https://example.com")

        assert result is None
        print("PASS: HTTP 500 handled correctly.")


if __name__ == "__main__":

    test_timeout()
    test_connection_error()
    test_http_429()
    test_http_500()

    print("\nAll API failure tests completed.")

def test_invalid_json():
  if __name__ == "__main__":

    fake_response = Mock()
    fake_response.status_code = 200
    fake_response.raise_for_status.return_value = None

    fake_response.json.side_effect = (
        requests.exceptions.JSONDecodeError(
            "Invalid JSON",
            "not-json",
            0
        )
    )

    with patch("requests.get", return_value=fake_response):

        print("\nTEST: INVALID JSON")

        result = make_api_request("https://example.com")

        assert result is None
        print("PASS: Invalid JSON handled correctly.")