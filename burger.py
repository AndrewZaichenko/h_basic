burgers = [
    {
        "id": 0,
        "name": "Tribute Burger",
        "description": "A mouth-watering honest beef burger",
        "type": "beef",
        "ingredients": {
            "beef": 11,
            "american cheese": 2,
            "burger sauce": 5,
            "french mustard": 1,
            "pickes": 4,
            "coleslaw": 6,
            "lettuce": 4
        },
        "addresses": [
            {
                "addressId": 0,
                "number": "75",
                "line1": "Venn Street",
                "line2": "Clapham",
                "postcode": "SW4 0BD",
                "country": "United Kingdom"
            }
        ]
    },
    {
        "id": 1,
        "name": "Pulled Mooshie",
        "type": "vegan",
        "description": "Spicy vegan burger with jackfruit",
        "ingredients": {
            "jackfruit": 2,
            "cucumber": 4,
            "tomatoes": 5,
            "gluten free bun": 0,
            "burger sauce": 11
        },
        "addresses": [
            {
                "addressId": 0,
                "number": "104",
                "line1": "Brick Lane",
                "line2": "Shoreditch",
                "postcode": "E1 6RL",
                "country": "United Kingdom"
            }
        ]
    }
]

burgers_in_ua = [
    {
        "addressId": 0,
        "name": "'ODESA-BRGRS'",
        "street": "Derybasivska St.",
        "house_num": 12,
        "postcode": 65000,
        "city": "Odesa"
    },
    {
        "addressId": 1,
        "name": "'KYIV-BRGRS'",
        "street": "Lesi Ukrainky Blvd.",
        "house_num": 24,
        "postcode": 11330,
        "city": "Kyiv"
    },
    {
        "addressId": 2,
        "name": "'LVIV-BRGRS'",
        "street": "Svobody Ave.",
        "house_num": 23,
        "postcode": 79000,
        "city": "Lviv"
    },
    {
        "addressId": 3,
        "name": "'KHARKIV-BRGRS'",
        "street": "Sumska St.",
        "house_num": 2,
        "postcode": 61000,
        "city": "Kharkiv"
    },
    {
        "addressId": 4,
        "name": "'DNIPRO-BRGRS'",
        "street": "Dmytra Yavornytskoho Ave.",
        "house_num": 67,
        "postcode": 49000,
        "city": "Dnipro"
    }
]

# print((burgers_in_ua[0]["street"]))
# print(burgers[0]["addresses"], burgers[1]["addresses"])

burgers[0]["addresses"] = burgers_in_ua[:3]
burgers[1]["addresses"] = burgers_in_ua[3:5]

# print(burgers[0]["addresses"], burgers[1]["addresses"])

client_burger = input("Which burger do you want: Vegan or Beef? >>> ").strip().lower()
print(f"The client orders {client_burger} burger.")

# if client_burger == burgers[]

if client_burger == burgers[0]["type"]:
  order = burgers[0]
  print("The client wants a", burgers[0]["name"], "-", burgers[0]["description"])
elif client_burger == burgers[1]["type"]:
  order = burgers[1]
  print("The client wants a", burgers[1]["name"], "-", burgers[1]["description"])

ingr_dict = order["ingredients"]
if all(ingr_dict.values()):
    print("You can buy", order["name"], "by the following addresses:")
    for addr in order["addresses"]:
        print("In", addr["city"], ">>>", addr["name"], addr["street"], addr["house_num"])
else:
    print("Sorry, we have run out of ingredients for", order["name"])