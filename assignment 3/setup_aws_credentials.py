import os

def setup_aws_credentials(access_key_id, secret_access_key, region='us-east-1'):
    aws_dir = os.path.expanduser("~/.aws")
    credentials_path = os.path.join(aws_dir, "credentials")
    config_path = os.path.join(aws_dir, "config")

    if not os.path.exists(aws_dir):
        os.makedirs(aws_dir)
    
    credentials_content = f"""
[default]
aws_access_key_id = {access_key_id}
aws_secret_access_key = {secret_access_key}
"""
    with open(credentials_path, "w") as credentials_file:
        credentials_file.write(credentials_content.strip())
    
    config_content = f"""
[default]
region = {region}
"""
    with open(config_path, "w") as config_file:
        config_file.write(config_content.strip())
    
    print("AWS credentials and config setup complete.")

# Replace with your actual AWS credentials
setup_aws_credentials("YOUR_ACCESS_KEY_ID", "YOUR_SECRET_ACCESS_KEY", "us-east-1")
