from datetime import datetime, timedelta
import time
last_push_time = None

start_time = datetime.now()
isPrinted = False


try:
    while datetime.now() - start_time < timedelta(minutes=5):
        now = datetime.now()
        
        if last_push_time is None:
            print("Push Data successfully")
            last_push_time = now
        else:
            time_diff = now - last_push_time
            if time_diff >=  timedelta(seconds=5):
                print("Push Data Successfully")
                last_push_time = now
                
            else:
                print(f"Skipping push — only {time_diff.total_seconds()/60:.2f} minutes elapsed since last push.")
            
        time.sleep(1)
except Exception as e:
        print(str(e))