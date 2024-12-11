from flask import Flask, render_template, request, redirect, url_for, flash
from models.database import init_db, save_log, get_logs
from services.aws_service import fetch_cloudtrail_logs
from services.log_analyzer import parse_logs, analyze_logs

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize the database
init_db()

@app.route('/')
def dashboard():
    logs = get_logs()
    return render_template('dashboard.html', logs=logs)

@app.route('/fetch-logs', methods=['GET', 'POST'])
def fetch_logs():
    if request.method == 'POST':
        logs = fetch_cloudtrail_logs()  # Fetch logs from AWS
        parsed_logs = parse_logs(logs)
        save_log(parsed_logs)          # Save logs to the database
        flash("Logs fetched and saved successfully!", "success")
        return redirect(url_for('dashboard'))
    return render_template('fetch_logs.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_logs():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            logs = file.read().decode('utf-8')
            parsed_logs = parse_logs(logs)
            save_log(parsed_logs)
            flash("Logs uploaded and analyzed successfully!", "success")
            return redirect(url_for('dashboard'))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
