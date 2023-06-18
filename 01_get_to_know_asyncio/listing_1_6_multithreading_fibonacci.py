import threading
import time

"""
Essa versão com threads levou quase a mesma quantidade de tempo do exemplo 1_5_no_threading_fibonacci
Isso se deve quase inteiramente ao GIL e á sobrecarga de criação e gerenciamento de threads. Embora seja
verdade que as threads são executadas simultaneamente, apenas uma delas pode executar o código Python por
vez devido ao bloqueio.
"""

def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    print(f"fib({number}) is {fib(number)}")


def fibs_with_threading():
    fortieth_thread = threading.Thread(target=print_fib, args=(40,))
    forty_first_thread = threading.Thread(target=print_fib, args=(41,))

    fortieth_thread.start()
    forty_first_thread.start()

    fortieth_thread.join()
    forty_first_thread.join()


start_with_threads = time.time()
fibs_with_threading()
end_threads = time.time()

print(f"Threads took {end_threads - start_with_threads:.4f} seconds")
