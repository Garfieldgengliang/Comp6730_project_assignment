"""COMP6730 question 8.

This should be completed individually.

Author: <u6799959>
Date: <10/21/2018>
"""


def plot_fire_spread(vegetation_type, vegetation_density, wind_speed):
    '''plot the numbers of various vegetation type on fire after 100 steps
    in a map by using bar chart'''
    import matplotlib.pyplot as plt
    steps = 100
    from assignment import load_bushfire
    initial_bushfire = load_bushfire('south_initial_2003_bushfire.csv')
    from assignment import simulate_bushfire_stochastic
    newmap =  simulate_bushfire_stochastic(initial_bushfire, steps, vegetation_type, vegetation_density, wind_speed)
    count_Open_Woodland = 0
    count_Woodland = 0
    count_Grassland = 0
    count_Forest = 0
    count_Open_Forest = 0
    count_Urban_Vegetation = 0
    count_Golf_Course = 0
    count_Pine_Forest = 0
    count_Shrubland = 0
    count_Arboretum = 0
    for rowindex in range (0, len(newmap)):
        for colindex in range (0, len(newmap[0])):
            if vegetation_type[rowindex][colindex] == 'Open Woodland' and newmap[rowindex][colindex] == True:
                count_Open_Woodland = count_Open_Woodland + 1
            elif vegetation_type[rowindex][colindex] == 'Woodland' and newmap[rowindex][colindex] == True:
                count_Woodland = count_Woodland + 1
            elif vegetation_type[rowindex][colindex] == 'Grassland' and newmap[rowindex][colindex] == True:
                count_Grassland = count_Grassland  + 1
            elif vegetation_type[rowindex][colindex] == 'Forest' and newmap[rowindex][colindex] == True:
                count_Forest = count_Forest + 1
            elif vegetation_type[rowindex][colindex] == 'Open Forest' and newmap[rowindex][colindex] == True:
                count_Open_Forest = count_Open_Forest + 1
            elif vegetation_type[rowindex][colindex] == 'Urban Vegetation' and newmap[rowindex][colindex] == True:
                count_Urban_Vegetation = count_Urban_Vegetation + 1
            elif vegetation_type[rowindex][colindex] == 'Golf Course' and newmap[rowindex][colindex] == True:
                count_Golf_Course = count_Golf_Course + 1
            elif vegetation_type[rowindex][colindex] == 'Pine Forest' and newmap[rowindex][colindex] == True:
                count_Pine_Forest = count_Pine_Forest + 1
            elif vegetation_type[rowindex][colindex] == 'Shrubland' and newmap[rowindex][colindex] == True:
                count_Shrubland = count_Shrubland  + 1
            elif vegetation_type[rowindex][colindex] == 'Arboretum' and newmap[rowindex][colindex] == True:
                count_Arboretum = count_Arboretum + 1
    objects = ['Open Woodland','Woodland','Grassland','Forest','Open Forest','Urban Vegetation','Golf Course', 'Pine Forest','Shrubland','Arboretum']
    object_value = [count_Open_Woodland,  count_Woodland,count_Grassland, count_Forest, count_Open_Forest, count_Urban_Vegetation, count_Golf_Course, count_Pine_Forest, count_Shrubland, count_Arboretum  ]
    plt.bar(objects, object_value, align='center', alpha=0.5)
    plt.xlabel('vegetation types')
    plt.ylabel('numbers')
    plt.title('numbers of various vegetation type on fire after 100 steps')
    plt.show



if __name__ == '__main__':
    # If you want something to happen when you run this file,
    # put the code in this `if` block.
    pass
