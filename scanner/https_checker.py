import requests


def check_https(url):
    """
    Checks whether the website finally uses HTTPS
    after redirects.
    """

    try:
        response = requests.get(url, timeout=5)

        final_url = response.url

        return {
            "https": final_url.startswith("https://"),
            "final_url": final_url
        }

    except requests.exceptions.RequestException:

        return {
            "https": False,
            "final_url": None
        }