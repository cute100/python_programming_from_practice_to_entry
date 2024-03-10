from city_country import get_city_country
print("Enter 'q' at any time to quit")
while True:
    city=input("\nPlese give me a city name:")
    if city=='q':
        break
    country=input("\nPlese give me a country name:")
    if country=='q':
        break
    formatted_name=get_city_country(city,country)
    print(f"\tNeatly formatted name:{formatted_name}")