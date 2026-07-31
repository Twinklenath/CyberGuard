import requests


def check_cookies(url):
    try:
        response = requests.get(url, timeout=5)

        cookies = response.cookies

        cookie_results = []

        for cookie in cookies:

            cookie_results.append({
                "name": cookie.name,
                "secure": cookie.secure,
                "httponly": "HttpOnly" in str(cookie),
            })

        return cookie_results

    except Exception:
        return []