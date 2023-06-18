import time
import requests


def read_example() -> None:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    print(response.status_code)


sync_start = time.time()
read_example()
read_example()
sync_end = time.time()

print(f"Running synchronously took {sync_end - sync_start:.4f} seconds.")
