import time


def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    print(f"fib({number}) is {fib(number)}")


def fibs_no_threading():
    print_fib(40)
    print_fib(41)


start_with_threads = time.time()
fibs_no_threading()
end_threads = time.time()

print(f"Completed in  {end_threads - start_with_threads:.4f} seconds")