import ssl
import socket
from datetime import datetime


def check_ssl(hostname):

    try:
        # Remove http:// or https:// if present
        hostname = hostname.replace("https://", "").replace("http://", "")
        hostname = hostname.split("/")[0]

        context = ssl.create_default_context()

        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:

                certificate = ssock.getpeercert()

        issuer = dict(x[0] for x in certificate["issuer"])

        expiry = certificate["notAfter"]

        expiry_date = datetime.strptime(
            expiry,
            "%b %d %H:%M:%S %Y %Z"
        )

        days_left = (expiry_date - datetime.utcnow()).days

        return {
            "valid": True,
            "issuer": issuer.get("organizationName", "Unknown"),
            "expiry": expiry_date.strftime("%d %B %Y"),
            "days_left": days_left
        }

    except Exception:

        return {
            "valid": False,
            "issuer": None,
            "expiry": None,
            "days_left": None
        }