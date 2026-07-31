import requests


def check_security_headers(url):

    try:

        response = requests.get(url, timeout=5)

        headers = response.headers

        security_headers = {

            "Content-Security-Policy":
                "Content-Security-Policy" in headers,

            "Strict-Transport-Security":
                "Strict-Transport-Security" in headers,

            "X-Frame-Options":
                "X-Frame-Options" in headers,

            "X-Content-Type-Options":
                "X-Content-Type-Options" in headers,

            "Referrer-Policy":
                "Referrer-Policy" in headers
        }

        return security_headers

    except requests.exceptions.RequestException:

        return None