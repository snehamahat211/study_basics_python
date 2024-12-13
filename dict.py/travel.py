travel_log =[
    {
        "country":"France",
        "total":12,
        "Cities":["paris","lille","dijon"],
    },
    {
        "country":"Germany",
        "total":7,
        "Cities":["berlin","hamburg","Stuttgart"],
    },
    ]
def add_new(country_visited,total_visited,Cities_visited):
    new_country={}
    new_country["country"]=country_visited
    new_country["total"]=total_visited
    new_country["Cities"]=Cities_visited
    travel_log.append(new_country)
add_new("Russia",2,["moscow","Saint-peterburg","Novosibirsk"])
print(travel_log)
