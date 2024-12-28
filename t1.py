from threading import Thread

def SayHello(name):
    print(f"Hello, {name}!")
    
name1 = Thread(target=SayHello, args=("Rezvan",))
name2 = Thread(target=SayHello, args=("Sara",))

name1.start()
name2.start()
name1.join()
name2.join()