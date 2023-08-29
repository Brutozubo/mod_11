from peewee import *
import unittest

conn = SqliteDatabase('db1.sqlite')

class Students(Model):
	id = PrimaryKeyField(column_name = 'id')
	name = CharField(column_name = 'name')
	lastname = CharField(column_name = 'lastname')
	age = IntegerField(column_name = 'age')
	city = CharField(column_name = 'city')

	class Meta:
		database = conn

class Courses(Model):
	id = PrimaryKeyField(column_name = 'id')
	name = CharField(column_name = 'name')
	time_start =CharField(column_name = 'time_start')
	time_end =CharField(column_name = 'time_end')

	class Meta:
		database = conn

class Student_Courses(Model):
    student_id = ForeignKeyField(Students)
    courses_id = ForeignKeyField(Courses)

    class Meta:
        database = conn

Students.create_table()
Courses.create_table()
Student_Courses.create_table()

conn.commit()
conn.close

def add_student(id, name, lastname, age, city):
	try:
		Students.insert(id = id, name = name, lastname = lastname, age = age, city = city).execute()
		return True
	except:
		return False

def add_course(id, name, time_start, time_end):
	try:
		Courses.insert(id = id, name = name, time_start = time_start, time_end = time_end).execute()
		return True
	except:
		return False

def delete_student(id):
	try:
		Student_Courses.delete().where(Student_Courses.student_id == id).execute()
		Students.delete().where(Students.id == id).execute()
		return True
	except:
		return False

def add_student_course(student_id, courses_id):
	try:
		Student_Courses.insert(student_id = student_id, courses_id = courses_id).execute()
		return True
	except:
		return False


unittest.main()