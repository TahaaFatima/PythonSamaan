import datetime

def log_errors(msg):
    dt = datetime.datetime.now()
    with open("log_error.txt",'a') as file:
        file.write(f"Error occurred at {dt} - {msg}\n")