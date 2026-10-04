from groups import GroupManager

manager = GroupManager()

manager.add_group("ENG-1", 20)
manager.add_group("ENG-2", 18)
manager.add_group("KAZ-1", 22)

print("Оқу топтарының тізімі:")
print("----------------------")

for group in manager.get_all_groups():
    print(f"{group.name}: {group.student_count} студент")

found_group = manager.find_group("ENG-2")

if found_group:
    print("\nІздеу нәтижесі:")
    print(f"{found_group.name}: {found_group.student_count} студент")