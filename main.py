# добавлю константы 
KMH_TO_MS = 10 / 36      # перевод км/ч в м/с
ACCELERATION_MS2 = 5.0   # среднее ускорение, м/с²
FUEL_CONSUMPTION_L_PER_100KM = 6.0  # л/100 км
def car_discription(car_model, color):
    return f"Описание авто: {car_model}, цвет: {color}"
