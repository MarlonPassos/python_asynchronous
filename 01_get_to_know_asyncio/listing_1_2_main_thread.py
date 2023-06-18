import os
import threading

"""
Um processo com uma thread pricipal

Primeiro, pegamos o ID do processo e o imprimimos para mostrarum processo dedicado
em execução. Em seguida, obtemos a contagem ativa de threads em execução.
"""

print(f"Python process running with process id: {os.getpid()}")
total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f"Python is currently running {total_threads} thread`s")
print(f"The current thread is {thread_name}")
