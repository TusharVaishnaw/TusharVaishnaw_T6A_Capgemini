class Student:
    college='jecrc'
    def __init__(self,name='Not Provided',
    student_id='Not Provided',
    branch='Not Provided'):
        self.name=name
        self.student_id=student_id
        self.branch=branch
    @classmethod
    def chan(cls):
        cls.college='poornima'
        

s3=Student('Akshay','it190','cs')
print(s3.name,s3.student_id,s3.branch,s3.college)
#call method 1
s3.chan()
#call method 2
#Student.chan()
print(s3.name,s3.student_id,s3.branch,s3.college)
s1=Student()
print(s1.name,s1.student_id,s1.branch,s1.college)

