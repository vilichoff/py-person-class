class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    person_list = []

    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        person_list.append(person)

    for person_data in people:
        name = person_data["name"]
        person = Person.people[name]

        if "wife" in person_data:
            wife_name = person_data["wife"]
            if wife_name and wife_name in Person.people:
                person.wife = Person.people[wife_name]

        if "husband" in person_data:
            husband_name = person_data["husband"]
            if husband_name and husband_name in Person.people:
                person.husband = Person.people[husband_name]

    return person_list
