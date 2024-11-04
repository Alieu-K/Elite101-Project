
# Structured by ship size, Time (military), occupied status, name of ship/bay
ship_bay_1 = [['Small', (19, 22), 'Empty', 'Alpha'], 
              ['Small', (13, 15), 'Occupied', 'Beta'], 
              ['Big', (3, 6), 'Empty', 'Gamma'], 
              ['Medium', (6, 12), 'Empty', 'Delta'],
              ['Big', (18, 24), 'Occupied', 'Epsilon'],
              ['Big', (11, 18), 'Empty', 'Eta'],
              ['Medium', (7, 20), 'Empty', 'Theta'],
              ['Small', (10, 14), 'Occupied', 'Iota'],
              ['Medium', (0, 9), 'Empty', 'Kappa'],
              ['Big', (14, 19), 'Empty', 'Lambda']]

ship_schedule_1 = [('Small', (19, 20), 'Ship 1'), 
                   ('Big', (2, 3), 'Ship 2'), 
                   ('Medium', (2, 5), 'Ship 3'),
                   ('Small', (13, 14), 'Ship 4'),
                   ('Medium', (7, 10), 'Ship 5'),
                   ('Big', (15, 18), 'Ship 6')]


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

