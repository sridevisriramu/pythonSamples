def plane_ride_cost(city):
 if city == "Charlotte":
  return 183
 elif city =="Tampa":
    #print city
    return 220
 elif city=="Pittsburgh":
  return 222
 elif city=="Los Angeles":
  return 475
 else:
  return "city name not matched"

#plane_ride_cost("Tampa")

def rental_car_cost(days):
  if days >= 7:
    return days*40-50   
  elif days >= 3 and days<7:
    # days*40-20
    return days*40-20
  else:
    return days*40

#rental_car_cost(2)

def hotel_cost(nights):
 return 140 * nights

def trip_cost(city, days):
  print rental_car_cost(days)+ hotel_cost(days - 1) + plane_ride_cost(city)
  return rental_car_cost(days)+ hotel_cost(days - 1) + plane_ride_cost(city)


trip_cost("Tampa", 3)