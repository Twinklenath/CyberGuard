def generate_summary(
    reachable,
    https,
    headers,
    ssl
):

    summary = []

    if reachable:
        summary.append("✔ Website Reachable")
    else:
        summary.append("❌ Website Unreachable")

    if https:
        summary.append("✔ HTTPS Enabled")
    else:
        summary.append("❌ HTTPS Disabled")

    if ssl["valid"]:
        summary.append("✔ Valid SSL Certificate")
    else:
        summary.append("❌ Invalid SSL Certificate")

    for header, status in headers.items():

        if status:

            summary.append(f"✔ {header}")

        else:

            summary.append(f"⚠ Missing {header}")

    return summary