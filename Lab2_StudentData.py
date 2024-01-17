""" Part 3: Student dataclass
Type in the dataclass code from the slides/video. You would have done this before class.
Add one more field: gpa, a float.
Write a main function to create some example Student objects with some example names, college_id and GPA values.
Verify you can read the name, college ID and GPA for an example student.
Verify when you print an example student, the GPA is included. """

from dataclasses import dataclass


@dataclass
class Student:
    name: str
    college_id: int
    gpa: float

    # this writes clear way we can read the database information
    def __str__(self):
        return f'Name {self.name}, college_ID {self.college_id}, GPA: {self.gpa}'


def main():

    # this is student dataclass information
    susan = Student('Susan', 12334, 3.9)
    ahmed = Student('Ahmed', 13455, 3.0)

    print(susan)
    print(ahmed)

main()