import time

#creates a txt file to view the status of the changes , while it moves, speed, and many more
status_file = "status.txt"

try:
    while True:
        with open(status_file, "r") as f:
            print("\n" + f.read())  # Display status
        time.sleep(1)  # Update every second

except KeyboardInterrupt:
    print("\nStatus monitoring stopped.")