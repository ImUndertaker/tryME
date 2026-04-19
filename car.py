import KMH_TO_MS, ACCELERATION_MS2, FUEL_CONSUMPTION_L_PER_100KM

class car():
    def __init__(self, speed, fuel):
        self.speed = speed
        self.fuel = fuel

    def acceleration(self):
        time_to_100 = (100*(KMH_TO_MS) - self.speed*(KMH_TO_MS))/ACCELERATION_MS2 # в среднем ускорение авто
        return f'Разгон до 100 за {time_to_100:.0f} секунд'

    def fuel_value(self) -> float:
        fuel_balance=self.fuel/FUEL_CONSUMPTION_L_PER_100KM
        distance = fuel_balance*100
        return f'запас хода: {distance:.0f} километров'



lexus=car(50, 20)
print(lexus.acceleration(),'|', lexus.fuel_value())
