import csv
from myapp.models import Student
from datetime import datetime

def import_students():
    with open('yunword/data/raw/students.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            student = Student(
                student_id=row['学生编号'],
                province=row['省份'],
                city=row['城市'],
                grade=row['年级'],
                textbook_version=row['教材版本'],
                registration_date=datetime.strptime(row['注册日期'], '%Y/%m/%d').date()
            )
            student.save()

if __name__ == "__main__":
    import_students()
