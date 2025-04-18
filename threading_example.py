import threading
from time import sleep


# def worker(num):
#     print(f"Worker: {num} is working")
#
#
# threads = []
#
# for proc_number in range(10):
#     t = threading.Thread(target=worker, args=(proc_number,))
#     threads.append(t)
#     t.start()


def do_job(number, second_arg=None):
    for i in range(50):
        print(f"From child thread: {i=}, {number=}, {second_arg=}")
        sleep(1)


def do_job2(number, second_arg=None):
    for i in range(50):
        print(f"From child thread: {i=}, {number=}, {second_arg=}")
        sleep(1)


thread = threading.Thread(
    target=do_job, args=(2,), kwargs={"second_arg": 25}, daemon=True
)
thread2 = threading.Thread(
    target=do_job, args=(26,), kwargs={"second_arg": 100}, daemon=True
)
thread.start()
thread2.start()
thread.join()
thread2.join()

for i in range(10, 20):
    print(f"From main thread: {i=}")

print("Finish")
