from multiprocessing import Pool
import time

def complex_calculation(n):
    result = 0
    for i in range(10000):  
        result += sum(j * j for j in range(n))
    return result

if __name__=="__main__":
    n = 100

    t1 = time.time()
    serial_result = sum(complex_calculation(i) for i in range(n))
    print("Serial processing or utilizing one core", serial_result)
    print(f"Time taken: {time.time() - t1} seconds")

    t2 = time.time()
    pool = Pool(processes=7)
    pool_result = pool.map(complex_calculation, range(n))
    pool.close()
    pool.join()
    parallel_result = sum(pool_result)
    print("Parallel processing or utilizing multiple cores", parallel_result)
    print(f"Time taken for parallel processing: {time.time() - t2} seconds")