# 4. Provided is a list of tuples. Create another list called t_check that contains the third element of every tuple.
lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]

t_check = []
for tup in lst_tups:
    t_check.append(tup[2])
    
print(t_check)


# 5. Below, we have provided a list of tuples. Write a for loop that saves the second element of each tuple into a list called seconds.
tups = [('a', 'b', 'c'), (8, 7, 6, 5), ('blue', 'green', 'yellow', 'orange', 'red'), (5.6, 9.99, 2.5, 8.2), ('squirrel', 'chipmunk')]

seconds = []

for tup in tups:
    seconds.append(tup[1])
    
print(seconds)



# If you remember, the .items() dictionary method produces a sequence of tuples. Keeping this in mind, we have provided you a dictionary called pokemon. 
# For every key value pair, append the key to the list p_names, and append the value to the list p_number. Do not use the .keys() or .values() methods.
pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}

p_names = []
p_number = []
for names, number in pokemon.items():
    p_names.append(names)
    p_number.append(number)
    
print(p_names)
print(p_number)



# The .items() method produces a sequence of key-value pair tuples. 
# With this in mind, write code to create a list of keys from the dictionary track_medal_counts and assign the list to the variable name track_events. 
# Do NOT use the .keys() method.
track_medal_counts = {'shot put': 1, 'long jump': 3, '100 meters': 2, '400 meters': 2, '100 meter hurdles': 3, 'triple jump': 3, 'steeplechase': 2, '1500 meters': 1, '5K': 0, '10K': 0, 'marathon': 0, '200 meters': 0, '400 meter hurdles': 0, 'high jump': 1}

track_events = []
for k in track_medal_counts.items():
    track_events.append(k[0])
    
print(track_events)
