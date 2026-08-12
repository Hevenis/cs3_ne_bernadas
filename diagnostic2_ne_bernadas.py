cargo_weight=50000

def calculate_fuel(cargo_weight):
    optionA="no"

    satellite=1000
    rover=2500
    supplies=500

    equipment={
        "satellite": satellite, 
        "rover": rover, 
        "supplies": supplies}
    
    while optionA == "no":
        
        optionB=input("What equipment would you like to edit? ")

        if optionB in equipment:
            add=int(input("The heavier, the better the tech. But you need more fuel (and vice versa) "))
            equipment[optionB]+=add

        else: 

            print("you sure that's an actual thing?")


        optionA=input("Launch now? choose *launch* or *no* ")


    total_cargo_weight=satellite+rover+supplies+cargo_weight

    fuel=total_cargo_weight*3

    print(f"The weight of your spaceship now is {total_cargo_weight} kg and the fuel needed is {fuel} gallons")


    if total_cargo_weight<60000:

        print("your good:]")

    else:

        print("WARNING MAX WEIGHT REACHED. OH NO")
    

        
    
    


print ("Hi there, I'm your assistant to help you with your rocketeering-stuff-thingy")

print ("The spaceship already weighs 50,000 kg, so don't go over 60,000 kg!")

calculate_fuel(cargo_weight)
