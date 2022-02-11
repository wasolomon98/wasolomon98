# Collection of functions for a small mock TTRPG game project
# Automates handling of updating lists and appending new items.
# Imported to separate (currently incomplete) character/nation handling module.

# Finds the location of upgraded tech in an imported list.
def tech_position(tech_list, tech_name):
    for i in tech_list:
        if i[:-2] == tech_name:
            return tech_list.index(i)

# Adds a newly acquired tech to the list.
def give_tech(tech_list, new_tech):
    new_list = tech_list[:]
    new_list.append(new_tech + " 1")
    return new_list

# Takes an input tech list and a chosen tech; increases chosen tech's 'level' by 1.
def upgrade_tech(tech_list, tech_name):
    for i in tech_list:
        if i[:-2] == tech_name:
            new_level = int(i[-1]) + 1
            tech_list[tech_position(tech_list, tech_name)] = i[:-1] + str(new_level)
            return tech_list
            
test_list = ["Plasma Rifles 1", "Plasteel Plating 3", "Energy Swords 1", "Heavy Ordinances 1"]
print(test_list)

test_list = give_tech(test_list, "Test Tech")
print(test_list)

test_list = upgrade_tech(test_list, "Test Tech")


print(test_list)
