class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model 

    def Next_generation_car_model(self):
        self.model += 1
        print(f"{self.brand} Brand New Model!The brand new model is {self.model}")


car1 = Car("BMW", 2026)
car1.Next_generation_car_model()
car1.Next_generation_car_model() 
        