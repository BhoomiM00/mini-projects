import ipaddress

from api_request import make_api_request
from response_validation import validate_ipwhois_response

from output_formatter import (
    print_header,
    print_section,
    print_field,
    print_success,
    print_error,
    display_ip_info
)


# --------------------------------------------------
# MANUAL IP LOOKUP
# --------------------------------------------------

def manual_ip_lookup():

    ip = input("\nEnter an IP address: ").strip()

    try:
        ip_obj = ipaddress.ip_address(ip)

    except ValueError:
        print_error("Invalid IP address.")
        return

    if not ip_obj.is_global:
        print_error("This is not a globally routable IP address.")
        return

    lookup_ip_information(ip)


# --------------------------------------------------
# AUTOMATIC PUBLIC IP DETECTION
# --------------------------------------------------

def automatic_ip_lookup():

    print_section("AUTOMATIC PUBLIC IP DETECTION")

    url = "https://api.ipify.org?format=json"

    data = make_api_request(url)

    if data is None:
        print_error("Could not detect your public IP.")
        return

    public_ip = data.get("ip")

    if not public_ip:
        print_error("Public IP missing from API response.")
        return

    try:
        ip_obj = ipaddress.ip_address(public_ip)

    except ValueError:
        print_error("The public IP API returned an invalid IP.")
        return

    if not ip_obj.is_global:
        print_error("Detected IP is not globally routable.")
        return

    print_success("Public IP detected successfully.")

    print_field("Your Public IP", public_ip)

    lookup_ip_information(public_ip)


# --------------------------------------------------
# IP GEOLOCATION LOOKUP
# --------------------------------------------------

def lookup_ip_information(ip):

    url = f"https://ipwho.is/{ip}"

    data = make_api_request(url)

    if data is None:
        print_error("Could not retrieve IP information.")
        return

    try:
        validated_data = validate_ipwhois_response(data)

    except ValueError as error:
        print_error(str(error))
        return

    display_ip_info(validated_data)


# --------------------------------------------------
# MAIN APPLICATION
# --------------------------------------------------

def main():

    while True:

        print_header()

        print("\n1. Enter IP manually")
        print("2. Detect my public IP automatically")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":

            manual_ip_lookup()

        elif choice == "2":

            automatic_ip_lookup()

        elif choice == "3":

            print_success("Thank you for using Python IP Finder!")
            break

        else:

            print_error("Invalid choice. Please select 1, 2, or 3.")


# --------------------------------------------------
# PROGRAM ENTRY POINT
# --------------------------------------------------

if __name__ == "__main__":
    main()