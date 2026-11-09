def print_header():
    print("=" * 50)
    print("              PYTHON IP FINDER")
    print("=" * 50)


def print_section(title):
    print(f"\n{title.center(50)}")
    print("-" * 50)


def print_field(label, value):
    if value is None or value == "":
        value = "Not Available"

    print(f"{label:<16}: {value}")


def print_success(message):
    print(f"\n[SUCCESS] {message}")


def print_error(message):
    print(f"\n[ERROR] {message}")


def print_footer():
    print("=" * 50)

def display_ip_info(data):
    import ipaddress

    print_header()

    print_section("IP INFORMATION")

    print_field("IP Address", data.get("ip"))

    ip_version = "Not Available"

    if data.get("ip"):
        try:
            ip_version = ipaddress.ip_address(data["ip"]).version
            ip_version = f"IPv{ip_version}"
        except ValueError:
            ip_version = "Unknown"

    print_field("IP Version", ip_version)
    print_field("Country", data.get("country"))
    print_field("Region", data.get("region"))
    print_field("City", data.get("city"))

    # ISP information is inside the connection object
    connection = data.get("connection") or {}
    print_field("ISP", connection.get("isp"))

    # Timezone information is inside the timezone object
    timezone = data.get("timezone") or {}
    print_field("Timezone", timezone.get("id"))

    print_section("LOCATION DETAILS")

    print_field("Latitude", data.get("latitude"))
    print_field("Longitude", data.get("longitude"))

    print_footer()
    print_success("IP lookup completed.")

    if __name__ == "__main__":

     sample_data = {
        "ip": "8.8.8.8",
        "country": "United States",
        "region": "California",
        "city": "Mountain View",
        "latitude": 37.386,
        "longitude": -122.0838,
        "connection": {
            "isp": "Google LLC"
        },
        "timezone": {
            "id": "America/Los_Angeles"
        }
    }