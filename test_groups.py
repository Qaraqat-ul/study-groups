import unittest
from groups import GroupManager


class TestGroupManager(unittest.TestCase):

    def test_add_group(self):
        manager = GroupManager()
        manager.add_group("ENG-1", 20)

        self.assertEqual(len(manager.get_all_groups()), 1)
        self.assertEqual(manager.get_all_groups()[0].name, "ENG-1")
        self.assertEqual(manager.get_all_groups()[0].student_count, 20)

    def test_find_group(self):
        manager = GroupManager()
        manager.add_group("KAZ-1", 22)

        group = manager.find_group("KAZ-1")

        self.assertIsNotNone(group)
        self.assertEqual(group.name, "KAZ-1")
        self.assertEqual(group.student_count, 22)


if __name__ == "__main__":
    unittest.main()  