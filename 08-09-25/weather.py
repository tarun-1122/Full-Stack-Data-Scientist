import random

weather_opt=['sunny','cloudy','rainy','windy','snowy']
temp=random.randint(-10,50)
weather=random.choice(weather_opt)

print("weather=",weather,"temp=",temp)
