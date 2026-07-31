def calculate_score(reachable, https_enabled, headers):

    score = 100

    if not reachable:
        return 0

    if not https_enabled:
        score -= 25

    if not headers.get("Content-Security-Policy"):
        score -= 15

    if not headers.get("Strict-Transport-Security"):
        score -= 15

    if not headers.get("X-Frame-Options"):
        score -= 10

    if not headers.get("X-Content-Type-Options"):
        score -= 10

    if not headers.get("Referrer-Policy"):
        score -= 5

    if score < 0:
        score = 0

    return score