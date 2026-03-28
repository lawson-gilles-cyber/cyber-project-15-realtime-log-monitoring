# Real-time detection logic

def analyze_log(log):

    # Detect brute force attempt
    if "LOGIN FAILED" in log:
        return "[ALERT] Failed login attempt detected"

    # Detect suspicious login
    if "LOGIN SUCCESS - admin" in log:
        return "[ALERT] Admin login detected"

    # Detect sensitive file access
    if "confidential" in log:
        return "[ALERT] Sensitive file accessed"

    return None
