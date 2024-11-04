
# 1 - Small Ships, 2 - Medium Ships, 3 - Large Ships
# Structured by ship size, Time (military), occupied status, name of ship/bay
ship_bay_1 = [[1, (19, 22), 'Empty', 'Alpha'], 
              [1, (13, 15), 'Occupied', 'Beta'], 
              [3, (3, 6), 'Empty', 'Gamma'], 
              [2, (6, 12), 'Empty', 'Delta'],
              [3, (18, 24), 'Occupied', 'Epsilon'],
              [3, (11, 18), 'Empty', 'Eta'],
              [2, (7, 20), 'Empty', 'Theta'],
              [1, (10, 14), 'Occupied', 'Iota'],
              [2, (0, 9), 'Empty', 'Kappa'],
              [3, (14, 19), 'Empty', 'Lambda']]

ship_schedule_1 = [(1, (19, 20), 'Ship 1'), 
                   (3, (2, 3), 'Ship 2'), 
                   (2, (2, 5), 'Ship 3'),
                   (1, (13, 14), 'Ship 4'),
                   (2, (7, 10), 'Ship 5'),
                   (3, (15, 18), 'Ship 6')]


def bay_selection(ship_schedule, ship_bay):
    
    docking_options = []

    for ship in ship_schedule: #Tuple of ship details
        x = ''
        for bay in ship_bay:  #Bays
            ship_time = ship[1]
            bay_time = bay[1]

    #             Checks size                                                   Checks availability times                               Checks if occupied
            if (bay[0] == ship[0]) and (bay_time[0] <= ship_time[0] <= bay_time[1]) and (bay_time[0] <= ship_time[1] <= bay_time[1] and (bay[2] == 'Empty')): 
                x = f'Bay {bay[3]} is availble between times {ship_time[0]}-{ship_time[1]}'
                bay[2] = 'Occupied'
                break
            else:
                x = 'No bays are available'
           



        docking_options.append(f'{ship[2]}: {x}')

    
    return docking_options


availability = bay_selection(ship_schedule_1, ship_bay_1)

print("\n")
for ship in availability:
    print(f"{ship}\n ------------------------------------")

