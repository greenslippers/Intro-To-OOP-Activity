class Student:
    def __init__(self, name, level, classes):
        self.name = name
        self.level = level
        self.classes = classes

    def add_class(self, new_class):
        self.classes.append(new_class)

        return self.classes

    def get_num_classes(self):

        num_classes = len(self.classes)
        self.length = num_classes
        
        return num_classes
    
    def summary(self):

        print(f'{self.name} is a {self.level} enrolled in {len(self.classes)} classes')





