

#Honestly, I have zero clue what to do here. The instructions are rather unclear to me/I dunno what to do. I can definitely tell you that this code does not work at all.

class starship:


    def __init__(self, final_fuel, base_ship_weight, cargo_weight):
        
        self.final_fuel=final_fuel
        self.base_ship_weight=base_ship_weight
        self.cargo_weight=cargo_weight

    def load_cargo(cargo_weight):

        cargo_weight=cargo_weight+1000
        


    def calculate_fuel(cargo_weight):

        base_ship_weight=50000
        total_weight=cargo_weight+base_ship_weight
        final_fuel=total_weight*3
        print(final_fuel)
        



starship.calculate_fuel()




