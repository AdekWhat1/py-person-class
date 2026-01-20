class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self

def create_person_list(people: list) -> list:
    people_objs = [Person(d["name"], d["age"]) for d in people]
    for d in people:
        if d.get("wife") is not None:
            person = Person.people[d["name"]]
            spouse = Person.people[d["wife"]]
            person.wife = spouse
        if d.get("husband") is not None:
            person = Person.people[d["name"]]
            spouse = Person.people[d["husband"]]
            person.husband = spouse
    return people_objs
