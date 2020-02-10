from operator import attrgetter, methodcaller, itemgetter
import vehicle

vehicle_list = [
    vehicle.Bike(1656612),
    vehicle.Car(105000),
    vehicle.Bike(51542120),
    vehicle.Bike(454254255),
    vehicle.Car(505000)
    ]

print("Descending Order - Price : ")
veh_list = sorted(vehicle_list, key = attrgetter('price'), reverse = True)
print(veh_list)
print("Ascending Order - Discount Price : ")
print(sorted(veh_list, key = methodcaller('discount_price')))