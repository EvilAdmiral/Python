class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age

class Student(Person):
    def __init__(self, sid, name, age, course, marks):
        super().__init__(name, age)
        self.sid, self.course, self.marks = sid, course, marks

    def __str__(self):
        return f"ID: {self.sid}, Name: {self.name}, Age: {self.age}, Course: {self.course}, Marks: {self.marks}"

class StudentManager:
    def __init__(self):
        self.students = []

    def add(self, s):
        self.students.append(s)

    def remove(self, sid):
        self.students = [s for s in self.students if s.sid != sid]

    def search(self, sid):
        return next((s for s in self.students if s.sid == sid), None)

    def display_all(self):
        [print(s) for s in self.students]

    def top_scorer(self, course):
        return max((s for s in self.students if s.course == course), key=lambda s: s.marks, default=None)

    def avg_marks(self, course):
        c = [s.marks for s in self.students if s.course == course]
        return sum(c)/len(c) if c else 0

    def list_by_course(self, course):
        return [s for s in self.students if s.course == course]

    @staticmethod
    def valid(s):
        return all([s.sid, s.name, s.age, s.course, s.marks])

# --- Sample Data ---
data = [
    {"id": 101, "name": "Amit", "age": 20, "course": "Python", "marks": 7},
    {"id": 300, "name": "Riya", "age": 23, "course": "Java", "marks": 851},
    {"id": 203, "name": "Samefer", "age": 21, "course": "Python", "marks": 923},
    {"id": 204, "name": "Pooja", "age": 20, "course": "C++", "marks": 69},
    {"id": 205, "name": "Nikhil", "age": 23, "course": "Python", "marks": 881}
]

m = StudentManager()
for d in data:
    s = Student(d["id"], d["name"], d["age"], d["course"], d["marks"])
    if StudentManager.valid(s):
        m.add(s)

# --- Example Usage ---
print("\nAll Students:"); m.display_all()
print("\nSearch ID 203:", m.search(203) or "Not found")
print("\nTop in Python:", m.top_scorer("Python") or "None")
print("\nAvg Marks in Python:", round(m.avg_marks("Python"), 2))
print("\nStudents in Java:", *m.list_by_course("Java"), sep="\n")
print("\nRemoving ID 101..."); m.remove(101)
print("\nStudents after removal:"); m.display_all()
