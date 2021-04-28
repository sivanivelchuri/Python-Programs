number_of_stations=int(input("number_of_gas_stations: "))
distances=list(map(int,input("distance_between_gas_stations:").split()))
gasoline_stations=number_of_stations
gas_amount=list(map(int,input("amount_of_gas_in_each_station: ").split()))
destination_dist=int(input("destination_dist: "))
initial_gas=int(input("initial_gas: "))
c=0
if initial_gas>destination_dist:
    print("NO STATIONS VISITED")
elif initial_gas<distances[0]:
    print("CAN'T POSSIBLE")
else:
    for i in range(len(distances)):
        gas=initial_gas-distances[i]
        if gas==0 or gas<(distances[i+1]-distances[i]):
            initial_gas+=gas_amount[i]
            c+=1
        elif gas>(distances[i+1]-distances[i]):
            continue
print(c)

            
