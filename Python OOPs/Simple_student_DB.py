class student:
    def __init__(self,name,age,mark):
        self.name=name
        self.age=age
        self.mark=mark

class course:
    def __init__(self,course_name,max_students):
        self.course_name=course_name
        self.max_students=max_students
        self.students=[]

    def add_student(self,student):
        if len(self.students)<self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_avg_mark(self):
        sum=0
        for stu in self.students:
            sum += stu.mark
        return sum/len(self.students)
    
    def total_students(self):
        return len(self.students)
    
s1=student("Tim",18,80)
s2=student("lee",18,75)
s3=student("bearn",18,85)

stu_details=course("Science",3)
stu_details.add_student(s1)
stu_details.add_student(s2)
stu_details.add_student(s3)
print(stu_details.get_avg_mark())
print(stu_details.total_students())
