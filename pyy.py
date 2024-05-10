import time
from threading import Thread


def countDown():
    for i in range(500000000):
        pass


t1 = Thread(target=countDown())
t2 = Thread(target=countDown())
t3 = Thread(target=countDown())

start = time.time()

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

end = time.time()


print("Time :", end - start)