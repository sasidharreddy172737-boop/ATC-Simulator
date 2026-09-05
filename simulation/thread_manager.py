import threading
class SimulationThreadManager:
    def __init__(self):

        self.threads=[]

    def create_threads(self,target,args=()):

        thread=threading.Thread(target=target,args=args)

        self.threads.append(thread)

        return thread
    def start_all(self):

        for thread  in self.threads:
            thread.start()

    def join_all(self):
        for thread in self.threads:
            thread.join()
            
    def clear(self):
        self.threads.clear()

    