class Car:
    @staticmethod
    def start():
        print("Car started")
    
    @staticmethod
    def stop():
        print("Car stopped")
    

class ToyotoCar(Car):
        def __init__(self,name):
                self.name=name


car1=ToyotoCar("Fortuner")
car2=ToyotoCar("prius")

print(car1.name)
car1.start()
car1.stop()
