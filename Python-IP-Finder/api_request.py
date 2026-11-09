import requests


def make_api_request(url):
    try:
        print("\nConnecting to API...")

        response = requests.get(url, timeout=10)
        print("HTTP Status Code:", response.status_code)

        response.raise_for_status()

        data = response.json()
        return data

    except requests.exceptions.Timeout:
        print("[ERROR] Request timed out.")

    except requests.exceptions.ConnectionError:
        print("[ERROR] Connection failed. Check your internet.")

    except requests.exceptions.HTTPError as error:
        status = error.response.status_code

        if status == 429:
            print("[ERROR] API rate limit reached. Try again later.")
        elif status >= 500:
            print("[ERROR] API server temporarily unavailable.")
        else:
            print("[ERROR] HTTP Error:", status)

    except requests.exceptions.JSONDecodeError:
        print("[ERROR] API returned invalid JSON.")

    except requests.exceptions.RequestException as error:
        print("[ERROR] Request failed:", error)

    return None

if __name__ == "__main__":

    print("\nTEST 1: Invalid domain")

    result = make_api_request(
        "https://this-domain-should-not-exist-123456.example/"
    )

    print("Returned:", result)

    print("\nTEST 2: Invalid URL")

    result = make_api_request("not-a-valid-url")

    print("Returned:", result)