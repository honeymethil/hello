class Flight():

    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seats():     #equivalent to saying   if self.open_seats == 0 or no open seats
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        #print(self.capacity - len(self.passengers))
        return self.capacity - len(self.passengers)

Indigo = Flight(4)
passengerList = ["Honey", "Anushri", "Seena", "Aarush", "Amma"]

#Indigo.add_passenger("Honey")
#Indigo.add_passenger("Seena")
#Indigo.add_passenger("Anushri")
#Indigo.add_passenger("Aarush")

for person in passengerList:
    success = Indigo.add_passenger(person)
    if success:        #success==True
        print(f"Added {person} successfully!")
    else:
        print(f"No available seats for {person}")

print(Indigo.passengers)