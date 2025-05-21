import time
from multiprocessing import Process

def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter += 1
    end = time.time()
    print(f"Counted to {count_to} in {end - start} seconds")
    return counter

if __name__ == "__main__":
    start = time.time()
    
    to_one_hundred_million = Process(target=count, args=(100000000,))
    to_two_hundred_million = Process(target=count, args=(200000000,))
    
    to_one_hundred_million.start()
    to_two_hundred_million.start()
    
    to_one_hundred_million.join()
    to_two_hundred_million.join()
    
    end = time.time()
    print(f"Total time taken: {end - start} seconds")