import requests


def check_website(url):
    """
    Checks whether the website is reachable.
    Returns a dictionary containing the result.
    """

    try:
        response = requests.get(url, timeout=5)

        return {
            "reachable": True,
            "status_code": response.status_code
        }

    except requests.exceptions.RequestException:

        return {
            "reachable": False,
            "status_code": None
        }