import threading
import time

import requests

"""
Duas vezes mais rápido

Isso o corre por que o GIL é liberado para as operações de I/O-bound (E/S), mas não para
operações vinculadas a CPU. 

No caso da E/S, as chamadas de sistema de baixo nível estão fora do tempo de execução do Python.
Isso permite que o GIL seja liberado porqie não esta interagindo diretamente com objetos Python, no
nível do sistema operacional, as operações de E/S são executadas simultaneamente. 
"""


def read_example() -> None:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    print(response.status_code)


thread_1 = threading.Thread(target=read_example)
thread_2 = threading.Thread(target=read_example)

sync_start = time.time()
thread_1.start()
thread_2.start()

print("All threads running!")
thread_1.join()
thread_2.join()
sync_end = time.time()

print(f"Running with threads took {sync_end - sync_start:.4f} seconds.")
