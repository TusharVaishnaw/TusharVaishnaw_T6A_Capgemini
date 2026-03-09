class Student:
    name='Not Provided'
    student_id='Not Provided'
    branch='Not Provided'


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
