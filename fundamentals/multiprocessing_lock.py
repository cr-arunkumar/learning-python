# lock - to prevent race conditions 
# when we trying to access and modify shared resources or multiple processes
# trying to modify the same resource at the same time then we will get the 
# inconsistent results

import multiprocessing
import threading
import time


def deposit(balance, amount,lock):
    for i in range(100):
        time.sleep(0.001)  # Simulating network delay
        lock.acquire()
        balance.value += amount
        lock.release ()


def withdraw(balance, amount,lock):
    for i in range(100):
        time.sleep(0.001)  # Simulating network delay
        lock.acquire()
        balance.value -= amount
        lock.release()


if __name__=="__main__":
    balance = multiprocessing.Value("d", 1000) 
    lock = multiprocessing.Lock()

    deposit_process = multiprocessing.Process(target=deposit, args=(balance, 0.01,lock))
    withdraw_process = multiprocessing.Process(target=withdraw, args=(balance, 0.01,lock))
    
    deposit_process.start()  
    withdraw_process.start()

    deposit_process.join()
    withdraw_process.join()

    print("Final balance:", balance.value)