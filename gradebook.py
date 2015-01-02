# Grade Manager

class Grade():

    
    def __init__(self, mark, units, course, teacher):
        self.mark = mark
        self.units = units
        self.course = course
        self.teacher = teacher

class GradeBook():

    def __init__(self, grade_list):
        self.grade_list = grade_list
        self.gpa = 0
        self.units = 
        self.values = { 'A' : 4,
                        'B' : 3,
                        'C' : 2,
                        'D' : 1,
                        'F' : 0 }
    def add(self, grade):
        self.grade_list.append(grade)

    def print_gpa(self):
        totalp = 0
        totalu = 0
        for g in self.grade_list:
            totalp += self.values[g.mark] * g.units
            totalu += g.units
        self.gpa = totalp / totalu
        self.units = totalu 
        print (self.gpa)

    def print_grades(self):
        for g in self.grade_list:
            print (g.mark, g.units, g.course, g.teacher)
    
                  
comsc_122 = Grade('A', 3, 'COMSC-132', 'Giambattista')

gbook = GradeBook([])
gbook.add(comsc_122)


gbook.print_grades()
gbook.print_gpa()
print (gbook.gpa)
