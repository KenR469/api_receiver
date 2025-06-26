from datetime import datetime, timedelta,timezone
import time
last_push_time = None

start_time = datetime.now(timezone.utc)
isPrinted = False

last_push_done = False
next_push_time = None

try:
    while datetime.now(timezone.utc) - start_time < timedelta(minutes=5):
        now = datetime.now(timezone.utc)
        
        if not last_push_done:
            print("Push Data successfully")
            last_push_done = True
            next_push_time = now + timedelta(seconds=5)
        else:
            if now >= next_push_time:
                print("Push 2nd Data successfully")
                next_push_time = now + timedelta(seconds=5)
                
            else:
                 print("Waiting for 5 seconds interval after first push.")
            
        time.sleep(1)
except Exception as e:
        print(str(e))