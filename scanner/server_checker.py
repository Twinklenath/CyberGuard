import requests


def check_server(url):

    try:

        response = requests.get(url, timeout=5)

        server = response.headers.get("Server", "Unknown")

        return {
            "server": server
        }

    except requests.exceptions.RequestException:

        return {
            "server": "Unknown"
        }