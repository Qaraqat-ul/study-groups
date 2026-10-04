class StudyGroup:
    def __init__(self, name, student_count):
        self.name = name
        self.student_count = student_count


class GroupManager:
    def __init__(self):
        self.groups = []

    def add_group(self, name, student_count):
        group = StudyGroup(name, student_count)
        self.groups.append(group)
        return group

    def get_all_groups(self):
        return self.groups

    def find_group(self, name):
        for group in self.groups:
            if group.name == name:
                return group
        return None
