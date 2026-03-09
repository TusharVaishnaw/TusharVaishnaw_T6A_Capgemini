class Student:
    def __init__(self,name='Not Provided',
    student_id='Not Provided',
    branch='Not Provided'):
        self.name=name
        self.student_id=student_id
        self.branch=branch

s3=Student('Akshay','it190','cs')
print(s3.name,s3.student_id,s3.branch)

s1=Student()
s2=Student()
print(s1.name,s1.student_id,s1.branch)
print(s2.name,s2.student_id,s2.branch)

s1.name='Tushar'
s1.student_id='it176'
s1.branch='it'

s2.name='Akshat'
s2.student_id='cs177'
s2.branch='cs'

print(s1.name,s1.student_id,s1.branch)
print(s2.name,s2.student_id,s2.branch)
