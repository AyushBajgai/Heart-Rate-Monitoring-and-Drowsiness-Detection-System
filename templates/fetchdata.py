from google.oauth2 import service_account
import google.auth
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import json
import time

# Set up credentials
SCOPES = ['https://www.googleapis.com/auth/fitness.activity.read']
SERVICE_ACCOUNT_FILE = 'path/to/service-account-file.json'  # Update with your service account file path

# Function to authenticate and get Google Fit service
def get_google_fit_service():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    delegated_credentials = credentials.with_subject('user@example.com')  # Replace with your user email
    service = build('fitness', 'v1', credentials=delegated_credentials)
    return service

# Function to fetch heart rate data from Google Fit
def fetch_heart_rate(service):
    heart_rate_data = []
    now = int(time.time() * 1000000000)  # Convert current time to nanoseconds
    start_time = now - 3600 * 1000000000  # Fetch data for the last hour (adjust as needed)

    data_source_id = "derived:com.google.heart_rate.bpm:com.google.android.gms:merge_heart_rate_bpm"

    heart_rate_request = service.users().dataset().aggregate(
        userId='me',
        body={
            "aggregateBy": [{
                "dataTypeName": "com.google.heart_rate.bpm",
                "dataSourceId": data_source_id,
            }],
            "startTimeMillis": str(start_time // 1000000),  # Convert nanoseconds to milliseconds
            "endTimeMillis": str(now // 1000000),  # Convert nanoseconds to milliseconds
            "bucketByTime": {"durationMillis": 600000},  # Aggregate by 10 minutes
        }
    ).execute()

    if 'bucket' in heart_rate_request:
        for bucket in heart_rate_request['bucket']:
            for dataset in bucket['dataset']:
                for point in dataset['point']:
                    if 'value' in point:
                        heart_rate_data.append({
                            "heart_rate": point['value'][0]['fpVal'],
                            "timestamp": int(point['startTimeNanos']) // 1000000  # Convert nanoseconds to milliseconds
                        })

    return heart_rate_data

# Function to write heart rate data to a JSON file
def write_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    service = get_google_fit_service()
    heart_rate_data = fetch_heart_rate(service)
    write_to_json(heart_rate_data, 'heart_rate_data.json')

if __name__ == "__main__":
    main()
