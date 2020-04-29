class Instructor():
    
    def __init__(self, first_name, last_name, slack_handle, specialty, cohort):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.specialty = specialty
        self.cohort = cohort
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name} is with {self.cohort}"
    