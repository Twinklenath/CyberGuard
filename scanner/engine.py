from scanner.website_checker import check_website
from scanner.https_checker import check_https
from scanner.header_checker import check_security_headers
from scanner.ssl_checker import check_ssl
from scanner.cookie_checker import check_cookies
from scanner.score_calculator import calculate_score


def scan_website(url):

    website_result = check_website(url)

    https_result = check_https(url)

    headers_result = check_security_headers(url)

    ssl_result = check_ssl(url)

    cookie_result = check_cookies(url)

    score = calculate_score(
        website_result["reachable"],
        https_result if isinstance(https_result, bool) else https_result["https"],
        headers_result
    )

    return {
        "website": website_result,
        "https": https_result,
        "headers": headers_result,
        "ssl": ssl_result,
        "cookies": cookie_result,
        "score": score
    }