def skill_position(skill_list, skill_name):
    for i in skill_list:
        if i[:-2] == skill_name:
            return skill_lis.index(i)
