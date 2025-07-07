def search_city(city_list, target_city):
    if target_city in city_list:
        return city_list.index(target_city)
    else:
        return -1
cities = ["Kathmandu", "Pokhara", "Lalitpur", "Biratnagar", "Butwal"]
user_city = input("Enter the city you want to search: ")
index = search_city(cities, user_city)
if index != -1:
    print("City found at index ", index,".")
else:
    print("City not found in the list.")