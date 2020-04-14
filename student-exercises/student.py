import json
class Student:
    def __init__(self, first_name, last_name, slack_handle, cohort):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.cohort = cohort
        self.exercises_list = list()
    
    def print_details(self):
        new_dict = self.__dict__
        new_list = list()
        for exercise in new_dict["exercises_list"]:
            ex_dict = exercise.__dict__
            new_list.append(ex_dict)
        new_dict["exercises_list"] = new_list
        print(json.dumps(new_dict, indent=2))
    