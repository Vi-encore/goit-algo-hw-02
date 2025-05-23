from queue import Queue
import random
import time

queue = Queue()


def generate_request() -> None:
    new_request = {
        "id": random.randint(1, 1000),
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    queue.put(new_request)
    print(f'Request {new_request["id"]} was created at {new_request["time"]}')


def process_request() -> None:
    if not queue.empty():
        request = queue.get()
        print(f"Request {request['id']} is processing.")
    else:
        print("There are no requests to process")


while True:
    generate_request()
    process_request()

    exit_command = input('If you want to exit press "y": ')
    if exit_command.lower() == "y":
        print("Good bye!")
        break
