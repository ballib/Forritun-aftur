

flight_altitude = int(input("Input flight altitude (ft): "))
airspace_class = input("Input airspace class: ")
visibility = int(input("Input visibility (km): "))
horizontal = int(input("Input horizontal cloud separation (ft): "))
vertical = int(input("Input vertical cloud separation (ft): "))


if flight_altitude >= 10000:
    if airspace_class == "A":
        print("Instrument Flight Rules")
    elif airspace_class == "B" or airspace_class == "C" or airspace_class == "D" or airspace_class == "E" or airspace_class == "F" or airspace_class == "G":
        if visibility >= 8:
            if horizontal >= 1500:
                if vertical >= 1000:
                    print("Visual Flight Rules")
                else:
                    print("Instrument Flight Rules")
            else:
                print("Instrument Flight Rules")
        else:
            print("Instrument Flight Rules")
    else:
        print("Invalid input")



elif flight_altitude < 10000 and flight_altitude > 3000:
    if airspace_class == "A":
        print("Instrument Flight Rules")
    elif airspace_class == "B" or airspace_class == "C" or airspace_class == "D" or airspace_class == "E" or airspace_class == "F" or airspace_class == "G":
        if visibility >= 5:
            if horizontal >= 1500:
                if vertical >= 1000:
                    print("Visual Flight Rules")
                else:
                    print("Instrument Flight Rules")
            else:
                print("Instrument Flight Rules")
        else:
            print("Instrument Flight Rules")
    else:
        print("Invalid input")


elif flight_altitude <= 3000 and flight_altitude >= 0:
    if airspace_class == "A":
        print("Instrument Flight Rules")
    elif airspace_class == "B" or airspace_class == "C" or airspace_class == "D" or airspace_class == "E":
        if visibility >= 5:
            if horizontal >= 1500:
                if vertical >= 1000:
                    print("Visual Flight Rules")
                else:
                    print("Instrument Flight Rules")
            else:
                print("Instrument Flight Rules")
        else:
            print("Instrument Flight Rules")
    elif airspace_class == "F" or airspace_class == "G":
        if visibility >= 5:
            if horizontal >= 0:
                if vertical >= 0:
                    print("Visual Flight Rules")
                else:
                    print("Instrument Flight Rules")
            else:
                print("Instrument Flight Rules")
        else:
            print("Instrument Flight Rules")


    else:
        print("Invalid input")
else:
    print("Invalid input")


