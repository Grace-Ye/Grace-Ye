"""
this task used to return a people list which contains the name for each person and their friends'name
"""


import logging


class Person:
    """
    this class defined four functions, which includes init objects, add friend, get name and get friend
    """

    def __init__(self, first_name, last_name):
        """
        this function used to define global objects firstname,lastname and friend_person( a list)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.friend_person = []

    def add_friend(self, friend_person):
        """
        this function used to add friend_person to friend_person list
        """
        self.friend_person.append(friend_person)

    def get_name(self):
        """
        this function used to combine firstname and lastname
        """
        return self.first_name + self.last_name

    def get_friends(self):
        return self.friend_person


def load_people():
    file = open("a2_sample_set.txt", "r")
    lines = file.readlines()
    people = []
    for line in lines:
        name = line[:line.index(':')]  # get all characteristics before colon
        first_name = name[:name.index(' ')]  # the part before blank space from name object
        last_name = name[name.index(' '):]  # the part after blank space
        person = Person(first_name, last_name)  # invoke Person class init function and return object list but no name
        people.append(person)  # add person into people list

    for person in people:
        nameOfPerson = person.get_name()  # invoke Person class get_name function
        for line in lines:
            if nameOfPerson == line[:line.index(':')]:  # Name of object matches one of names in text file
                friendsNameList = (line[line.index(': '):]).replace(': ', '').replace('\n', '').split(', ')
                # list friends name for each object

        # Find object by friends name and add to person
        for friendName in friendsNameList:
            friendObject = findObjectByName(friendName, people)
            person.add_friend(friendObject)

    file.close()
    return people


def findObjectByName(name, people):
    # this function used to match name and person name to return object list
    for person in people:
        if name == person.get_name():
            return person


if __name__ == '__main__':
    load_people()
