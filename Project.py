def bay_selection(ship_schedule, ship_bay):
    
    docking_options = []

    for ship in ship_schedule: #Tuple of ship details
        x = ''
        for bay in ship_bay:  #Bays
            ship_time = ship[1]
            bay_time = bay[1]

    #             Checks size                                                   Checks availability times                               Checks if occupied
            if (bay[0] == ship[0]) and (bay_time[0] <= ship_time[0] <= bay_time[1]) and (bay_time[0] <= ship_time[1] <= bay_time[1] and (bay[2] == 'Empty')): 
                x = f'Bay {bay[3]} is availble between {ship_time[0]}-{ship_time[1]}'
                bay[2] = 'Occupied'
                break
            else:
                x = 'No bays are available'
           



        docking_options.append(f'{x} for {ship[2]}')

    
    return docking_options





# 1 - Small Ships, 2 - Medium Ships, 3 - Large Ships
# Structured by ship size, Time (military), occupied status, name of ship/bay
ship_bay_1 = [[1, (19, 22), 'Empty', 'Alpha'], 
              [1, (13, 15), 'Occupied', 'Beta'], 
              [3, (0, 5), 'Empty', 'Gamma'], 
              [2, (6, 12), 'Empty', 'Delta'],
              [3, (18, 24), 'Occupied', 'Epsilon'],
              [1, (17, 23), 'Empty', 'Zeta']]

ship_schedule_1 = [(1, (19, 20), 'Ship 1'), 
                   (3, (2, 3), 'Ship 2'), 
                   (2, (2, 5), 'Ship 3')]




ship_bay_2 = [[1, 0, 0, 2, 0],
              [0, 0, 0, 2, 2],
              [2, 1, 0, 0, 2],
              [0, 1, 0, 0, 0],
              [0, 0, 2, 2, 1]]

ship_schedule_2 = [3, 3, 2, 3, 1]

availability = bay_selection(ship_schedule_1, ship_bay_1)

print("\n")
for ship in availability:
    print(f"{ship}\n ------------------------------------")

