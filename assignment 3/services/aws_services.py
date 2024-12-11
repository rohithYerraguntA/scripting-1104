import boto3

def fetch_cloudtrail_logs():
    client = boto3.client('cloudtrail')
    response = client.lookup_events(MaxResults=50)  # Adjust as needed
    return response.get('Events', [])
