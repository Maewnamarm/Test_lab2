def calculate_total(room,last_water,current_water,last_elect,current_elect):
    water_rate = 5
    electric_rate = 6
    roomtype = {'a':1500,'b':2000}

    if room not in roomtype:
        raise ValueError("a or b")
    

    calwater = (current_water-last_water)*water_rate
    calelect = (current_elect-last_elect)*electric_rate
    roomtype = roomtype[room]

    price = roomtype + calelect + calwater
    
    return{
        "roomtype":roomtype,
        "calwater":calwater,
        "calelect":calelect,
        "price":price,
    }
