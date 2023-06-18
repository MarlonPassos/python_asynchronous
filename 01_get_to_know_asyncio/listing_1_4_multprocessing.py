import multiprocessing
import os

"""
Criamos um processo filho que imprime seu ID de processo e também imprime o ID do processo pai. 
"""


def hello_from_process():
    print(f"Hello from child process {os.getpid()}")


if __name__ == "__main__":
    hello_process = multiprocessing.Process(target=hello_from_process)
    hello_process.start()

    print(f"Hello from parent process {os.getpid()}")
    hello_process.join()
