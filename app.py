from flask import Flask, render_template, request

from scanner.website_checker import check_website
from scanner.https_checker import check_https
from scanner.header_checker import check_security_headers
from scanner.score_calculator import calculate_score
from scanner.ssl_checker import check_ssl
from scanner.cookie_checker import check_cookies
from scanner.server_checker import check_server
from scanner.summary_generator import generate_summary
from scanner.database import create_database
from scanner.database import save_scan
from scanner.database import get_history

app = Flask(__name__)
create_database()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/scan", methods=["POST"])
def scan():

    website = request.form["url"]

    website_result = check_website(website)

    https_result = check_https(website)

    headers_result = check_security_headers(website)

    ssl_result = check_ssl(website)

    cookie_result = check_cookies(website)

    server_result = check_server(website)

    score = calculate_score(
        website_result["reachable"],
        https_result if isinstance(https_result, bool) else https_result["https"],
        headers_result
    )

    save_scan(website, score)

    summary = generate_summary(
        website_result["reachable"],
        https_result if isinstance(https_result, bool) else https_result["https"],
        headers_result,
        ssl_result
    )

    return render_template(
        "result.html",
        website=website,
        result=website_result,
        https_result=https_result if isinstance(https_result, bool) else https_result["https"],
        headers=headers_result,
        score=score,
        ssl=ssl_result,
        cookies=cookie_result,
        server=server_result,
        summary=summary
    )
@app.route("/history")

def history():

    scans = get_history()

    return render_template(
        "history.html",
        scans=scans
    )

if __name__ == "__main__":
    app.run(debug=True)