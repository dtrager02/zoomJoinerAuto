from datetime import datetime
import time
start = datetime.now()
print(start)
time.sleep(5)
print(datetime.now()<start)