"""
this task used to return a patients list which contains Patient class, run_simulation function and load_patient function
and we import task 1
"""

from a2_28049918_task1 import *
import random


class Patient(Person):

    def __init__(self, first_name, last_name, health):
        # this function call the Person's function and add new object call health_point
        Person.__init__(self, first_name, last_name)
        self.health_point = health

    def get_health(self):
        return self.health_point

    def set_health(self, new_health):
        self.health_point = new_health

    def is_contagious(self):
        # this function used to test whether the health point below 49 and whether it is contagious
        if 0 <= self.health_point <= 49:
            return True
        else:
            return False

    def infect(self, viral_load):
        # this function used to calculate health point after infection when viral load happened
        if self.health_point <= 29:
            self.health_point = self.health_point - (0.1 * viral_load)
        elif 29 < self.health_point < 50:
            self.health_point = self.health_point - (1.0 * viral_load)
        elif self.health_point >= 50:
            self.health_point = self.health_point - (2.0 * viral_load)
        self.health_point_checker()

    def sleep(self):
        # this function is health point increase by 5 after sleeping
        if 0 <= self.health_point <= 100:
            self.health_point += 5
        self.health_point_checker()

    def get_viral_load(self):
        # this function used to calculate viral load
        viral_load = 5 + (self.health_point - 25) ** 2 / 62
        return viral_load

    def health_point_checker(self):
        # this function to limit the health point between 0 and 100. if the health point over than 100, it will back to 100
        if self.health_point > 100:
            self.health_point = 100
        elif self.health_point < 0:
            self.health_point = 0


def run_simulation(days, meeting_probability, patient_zero_health):
    patients = load_patients()
    patients[0].set_health(patient_zero_health) # identify health point for zero patient, since patient is a list
    daily_cases = []
    for day in range(0, days):
        if random.random() < meeting_probability: # the meeting happens
            for patient in patients:
                friends = patient.get_friends() # get_friend is in Person class
                for friend in friends:
                    if patient.is_contagious() & (not friend.is_contagious()):
                        viral_load = patient.get_viral_load() # calculate patient viral load
                        friend.infect(viral_load) # using patient's viral load to calculate friend infection
                    elif friend.is_contagious() & (not patient.is_contagious()):
                        viral_load = friend.get_viral_load()
                        patient.infect(viral_load)
                    elif patient.is_contagious() & friend.is_contagious():
                        patient_viral_load = patient.get_viral_load()
                        friend_viral_load = friend.get_viral_load()
                        patient.infect(friend_viral_load)
                        friend.infect(patient_viral_load)
                patient.sleep() # each patient get 5 points after sleeping
        else:
            # meeting not happens
            for patient in patients:
                patient.sleep()

        # Calculate daily cases
        casesOfToday = 0
        for patient in patients:
            if patient.is_contagious():
                casesOfToday += 1
        daily_cases.append(casesOfToday)
    return daily_cases


def load_patients(initial_health=75):
    file = open("a2_sample_set.txt", "r")
    lines = file.readlines()
    patients = []
    for line in lines:
        name = line[:line.index(':')]
        first_name = name[:name.index(' ')]
        last_name = name[name.index(' '):]
        patient = Patient(first_name, last_name, initial_health) # invoke Patients class
        patients.append(patient)

    for patient in patients: # same as Task 1
        nameOfPatient = patient.get_name()
        for line in lines:
            if nameOfPatient == line[:line.index(':')]:  # Name of object matches one of names in text file
                patientsNameList = (line[line.index(': '):]).replace(': ', '').replace('\n', '').split(', ')

        # Find object by friends name and add to person
        for patientName in patientsNameList: # same as task 1
            patientObject = findObjectByName(patientName, patients)
            patient.add_friend(patientObject)

    file.close()

    return patients


def findObjectByName(name, people):
    for person in people:
        if name == person.get_name():
            return person


if __name__ == '__main__':
    test_result = run_simulation(15, 0.8, 49)
    print(test_result)
    # Sample output for the above test case (15 days of case numbers):
    # [8, 16, 35, 61, 93, 133, 153, 171, 179, 190, 196, 198, 199, 200, 200]
    #
    # Note: since this simulation is based on random probability, the
    # actual numbers may be different each time you run the simulation.

    # Another sample test case (high meeting probability means this will
    # spread to everyone very quickly; 40 days means will get 40 entries.)
    test_result = run_simulation(40, 1, 1)
    print(test_result)
    # sample output:
    # [19, 82, 146, 181, 196, 199, 200, 200, 200, 200, 200, 200, 200, 200, 
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200,
    # 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]

