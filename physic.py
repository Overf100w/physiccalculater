sub_params = {'gold': [130, None, 67000], 'quicksilver': [138, None, 12000, 300000], 'plumbum': [140, None, 25000], 
 'tin': [230, None, 59000], 'silver': [250, None, 87000], 'copper': [400, None, 210000], 'zinc': [400], 
 'brass': [400], 'iron': [460, None, 270000], 'steel': [500, None, 84000], 'graphite': [750], 
 'brick': [880], 'ice': [2100, None, 340000],'ether': [2350, None, None, 400000], 
 'water': [4200, None, None, 2300000], 'powder': [None, 3800], 'wood': [2400, 10000000], 
 'peat': [None, 14000000], 'coal': [None, 27000000], 'anthracite': [None, 30000000], 
 'charcoal': [None, 34000000],'alcohole': [2500, 27000000, 110000, 900000], 'natural gas': [None, 44000000], 
 'oil': [None, 44000000],'kerosine': [2100, 46000000], 'hydrogen': [None, 120000000, 59000], 
 'gasoline': [None, 46000000], 'aluminium': [None, None, 390000],'wax':[None, None, 150000], 
 'oxygen':[None, None, 14000], 'ammonia':[None, None, None, 1400000], 'air':[None, None, None, 200000]}

#Welcome function
def welcome():  
    global a
    global subst
    global m

    print(""" 
 |##########==========#####/////////////////////////////////////#####==========##########|
 |#######################==========It\'s J0ulE C@lCul@Ter==========######################|
 |##########==========#####/////////////////////////////////////#####==========##########|

     If you want to calculate heating energy use \'h\';
     If you want to calculate burning energy use \'b\';
     If you want to calculate melting energy use \'m\';
     If you want to calculate steam energy use   \'s\';
     """)

    a = input('Fill operation:')
    while a == '':
        a = input('You fill the empty Operation! Operation:')

welcome()

#Heating energy
if a == 'h':
    subst = input("Substance:")     #Substance input
    while subst == '':
        subst = input('You fill the empty substation! Substance:')

    if subst in sub_params:
        c = sub_params[subst][0]
    else:
        c = input('')
        while c == '':
            c = input('Idk this substance, fill \'c\' by hand: ')

    t = input('Temperature(difference):')    #Temperature input
    while t == '':
        t = input('You fill the empty temperature! Temperature(difference):')

    m = input('Mass(kg):')                   #Mass input
    while m == '':
        m = input('You fill the empty mass! Mass(kg):')

#Output
    input("\nFormula: Q = cm(t)\nResult: {} Joules".format(float(m) * float(c) * float(t)))                                   
    print('\n' * 50)
    welcome()
#----------------------------------------

#Burning energy
elif a == 'b':
    subst = input("Substance:") #Substance input
    while subst == '':
        subst = input('You fill the empty substation! Substance:')

    if subst in sub_params:
        q = sub_params[subst][1]
    else:
        q = input('Uncnown substance, fill \'q\' by hand:')
        while q == '':
            print('You fill the empty \'q\'. Q:')
    
    m = input('Mass(kg):')                   #Mass input
    while m == '':
        m = input('You fill the empty mass! Mass(kg):')

#Output
    input("\nFormula: Q = qm\nResult: {} Joules".format(float(m) * float(q)))
    print('\n' * 50)
    welcome()
#----------------------------------------

#Melitng energy
elif a == 'm':
    subst = input("Substance:") #Substance input
    while subst == '':
        subst = input('You fill the empty substation! Substance:')

    if subst in sub_params:
        la = sub_params[subst][2]
    else:
        la = input('Uncnown substance, fill \'lambda\' by hand:')
        while la == '':
            print('You fill the empty \'lambda\'. Lambda:')

    m = input('Mass(kg):')                   #Mass input
    while m == '':
        m = input('You fill the empty mass! Mass(kg):')

#Output
    input("\nFormula: Q = \'lambda\'*m\nResult: " + str(float(m) * float(la)) + ' Joules')
    print('\n' * 50)
    welcome()
#----------------------------------------

#Steam energy
elif a == 's':
    subst = input("Substance:")
    while subst == '':
        subst = input('You fill the empty substation! Substance:')
    
    if subst in sub_params:
        L = sub_params[subst][3]
    else:
        L = input('Uncnown substance, fill \'L\' by hand:')
        while L == '':
            print('You fill the empty \'L\'. L:')

    m = input('Mass(kg):')                   #Mass input
    while m == '':
        m = input('You fill the empty mass! Mass(kg):')

#Output
    input("\nFormula: Q = Lm\nResult: " + str(float(m) * float(L)) + ' Joules')
    print('\n' * 50)
    welcome()
#----------------------------------------
    
else:
    input('Unknown operation! Press any key to restart programm and try again.')