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

COMSC_122 = Grade('A', 3, 'COMSC-132', 'Giambattista'),
RA_015 = Grade('A', 3, 'RA-015', ''),
RA_012 = Grade('B', 3, 'RA-012', ''),
RA_010 = Grade('A', 3, 'RA-010', ''),
MUSIC_093 = Grade('A', 2, 'MUSIC-093', ''),
MUSIC_015 = Grade('A', 3, 'MUSIC-015', ''),
RA_025 = Grade('A', 3, 'RA-025', ''),
RA_021 = Grade('A', 2, 'RA-021', ''),
RA_020 = Grade('A', 3, 'RA-020', ''),
ENGL_100 = Grade('A', 3, 'ENGL-100', ''),
MATH_040 = Grade('A', 4, 'MATH-040', 'Hubbard'),
SPCH_110 = Grade('A', 3, 'SPCH-110', 'Petersen'),
PSYCH_014 = Grade('B', 3, 'PSYCH-014', ''),
MATH_050 = Grade('B', 4, 'MATH-050', 'Horne'),
COMSC_044 = Grade('A', 3, 'COMSC-044', 'Giambattista'),
BIOSC_010 = Grade('A', 4, 'BIOSC-010', ''),
PHYS_040 = Grade('C', 4, 'PHYS-040', 'Stone'),
PHIL_041 = Grade('A', 3, 'PHIL-041', ''),
MATH_060 = Grade('B', 4, 'MATH-060', ''),
DRAMA_015 = Grade('A', 3, 'DRAMA-015', 'Norris'),
MATH_070 = Grade('A', 4, 'MATH-070', 'Stricker'),
COMSC_142 = Grade('A', 3, 'COMSC-142', 'Giambattista'),
COMSC_122 = Grade('A', 3, 'COMSC-122', 'Giambattista')

COURSES = [ COMSC122, RA_015, RA_012, RA_010, 
            MUSIC_093, MUSIC_015, RA_025, RA_021, 
            RA_020, ENGL_100, MATH_040, SPCH_110, 
            PSYCH_014, MATH_050, COMSC_044, BIOSC_010,
            PHYS_040, PHIL_041, MATH_060, DRAMA_015,
            MATH_070, COMSC_142, COMSC_122 ]

gbook = GradeBook([])
for course in courses:
    gbook.add(course)
