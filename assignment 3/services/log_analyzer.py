import json

def parse_logs(raw_logs):
    parsed_logs = []
    for log in raw_logs:
        parsed_logs.append({
            "event_time": log.get("EventTime"),
            "event_name": log.get("EventName"),
            "username": log.get("Username"),
            "source_ip": log.get("SourceIPAddress")
        })
    return parsed_logs

def analyze_logs(logs):
    # Example: Identify suspicious IP addresses or actions
    suspicious_ips = set(log['source_ip'] for log in logs if log['event_name'] == "UnauthorizedAccess")
    return {"suspicious_ips": suspicious_ips}
