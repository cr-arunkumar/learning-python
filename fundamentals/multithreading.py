# Multithreading: Uses multiple threads within a single process (shared memory)
# multiprocessing: Uses multiple processes (separate memory)
# GIL (Global Interpreter Lock): Python's memory management limitation that allows
#  only one thread to execute Python bytecode at a time

'''
multithreading
 - IO-bound tasks (like network I/O, disk I/O)
 - overhead is low 
 - it is limited by GI(Global Interpreter Lock -
   Python's memory management limitation which allows only one thread
   to execute Python bytecode at a time)
- used - Web scraping, API calls

multiprocessing
   - CPU-bound tasks (like CPU-intensive tasks like calculations)
   - overhead is high
   - it uses multiple processes, which can utilize multiple cores
   - it is not limited by GIL
   - used when we need to do data processing 
   '''

import threading
import time

def calculate_square(numbers, taskType="io-bound", task_complexity=4, final_result=None,queue=None):
    print(f"Calculating squares for numbers: {numbers} - task type: {taskType} - task complexity: {task_complexity} %")
    if taskType=="io-bound":
        simulate_io_bound_task()
    else:
        do_cpu_bound_tasks(task_complexity)
    result=[num**2 for num in numbers]
    print("Result for Squared:", result)
    if queue is not None:
            for i in numbers:
                queue.put(i)
    if final_result is not None:
        final_result.value = sum(result)  # Update the shared memory variable
    return result

def simulate_io_bound_task(n=1):
    print(f"Simulating IO-bound task for number: {n}")
    time.sleep(1)  # Simulating delay
    print(f"Finished IO-bound task for number: {n}")

def do_cpu_bound_tasks(n=4):
    print(f"Simulating CPU-bound tasks for number: {n}")
    fibo_sum(n)
    print(f"Finished CPU-bound task for number: {n}")

def calculate_cube(numbers, taskType="io-bound", task_complexity=4, final_result=None,queue=None):
    print(f"Calculating cubes for numbers: {numbers} - task type: {taskType} - task complexity: {task_complexity} %")
    if taskType=="io-bound":
        simulate_io_bound_task()
    else:
        do_cpu_bound_tasks(task_complexity)
    result=[num**3 for num in numbers]
    if queue is not None:
        for i in numbers:
            queue.put(i)  # Add the result to the queue
    if final_result is not None:
        final_result.value = sum(result)  # Update the shared memory variable
    return result

# cpu intesive tasks 
def fibo_sum(n):
    a, b = 0, 1
    sum=0
    for _ in range(n):
        a, b = b, a + b
        sum+=a
    print("Sum of Fibonacci numbers:", sum)
    return sum

numbers = [1, 2, 3, 4, 5]

start_time = time.time()
calculate_square(numbers)
calculate_cube(numbers)
print("Time taken:", time.time() - start_time)

# let use the multithreading to utilize the cpu ideal time 
print("------------------------------Using the threading----------------------------------")
def example_function(args):
       print("Thread is running",args)

start_time=time.time()
thread_for_square = threading.Thread(target=calculate_square, args=(numbers,))
thread_for_cube = threading.Thread(target=calculate_cube, args=(numbers,))
thread_for_square.start()
thread_for_cube.start()
# Wait for both threads to finish
thread_for_square.join()
thread_for_cube.join()

print("Time taken:", time.time()-start_time)

# Note : when we do use threading module it is bound by GIL,
#  so we may not get the ideal speedup as compared to multiprocessing
# in above example , we have added the delay to simulate IO bound tasks
# incase if we have CPU bound tasks then threading will not be more efficient
print("\n\n------------------------------Using the multiprocessing----------------------------------\n\n")
import multiprocessing
if __name__ == "__main__":
    
 start_time = time.time()
 squred_result_in_main=multiprocessing.Value("d",0.0)
 cube_result_in_main=multiprocessing.Value("d",0.0)
#  we can multiprocessing queue to share the data between processes
 square_queue=multiprocessing.Queue()
 cube_queue=multiprocessing.Queue()
 process_for_square = multiprocessing.Process(target=calculate_square, args=(numbers,"cpu-bound",14,squred_result_in_main,square_queue)) 
 process_for_cube = multiprocessing.Process(target=calculate_cube, args=(numbers,"cpu-bound",14,cube_result_in_main,cube_queue))

 process_for_square.start()
 process_for_cube.start()

 # Wait for both processes to finish
 process_for_square.join()
 process_for_cube.join()
 print("Squred Result:", squred_result_in_main.value)
 print("Cube Result:", cube_result_in_main.value)

 while not square_queue.empty():
        print("Squred Result from Queue:", square_queue.get())
 while not cube_queue.empty():
        print("Cube Result from Queue:", cube_queue.get())


 print("Time taken:", time.time()-start_time)

# multiprocessing will utilize multiple cores, so it will be more efficient