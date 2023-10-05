import threading


lock = threading.Lock()

def traitement_long_1():
    with lock:
        for i in range(5):
            print(threading.current_thread().getName(),i)

def traitement_long_2():
    with lock:      
        for i in range(5):
            print(threading.current_thread().getName(),i)

class TheThread(threading.Thread):

    def __init__(self) -> None:
        super().__init__()

    def run(self) -> None:
        with lock:
            for i in range(5):
                print(f"run {i} - {self.name}")

def main():
    th1 = threading.Thread(target=traitement_long_1)
    th2 = threading.Thread(target=traitement_long_2)
    th3 = TheThread()
    th4 = TheThread()
    th1.start()
    th2.start()
    th3.start()
    th4.start()


    th1.join()
    th2.join()
    th3.join()
    th4.join()
    print("terminé !")

if __name__=='__main__':
    main()
