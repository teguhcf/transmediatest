import pandas as pd
import datetime
from datetime import date
class DataEmployee:
    data = pd.read_excel(r'E:\employee.xlsx')
    df = pd.DataFrame(data, columns=['NAMA', 'tgl_lahir'])
    print(df)
    df2 = df
    nameEmployee = df['NAMA']
    listEmployee = []

    for index, row in df.iterrows():
        now = datetime.datetime.now()
        birthdate = row['tgl_lahir'];
        today = date.today()
        age = today.year - birthdate.year
        full_year_passed = (today.month, today.day) < (birthdate.month, birthdate.day)
        if not full_year_passed:
            age -= 1
        employee = {
            'name': row['NAMA'],
            'date': row['tgl_lahir'],
            'age': age

        }
        print(row['NAMA'], row['tgl_lahir'], age)
        listEmployee.append(employee)

    print("ini hasil")

    def getEmployee(self):
        data = pd.read_excel(r'E:\employee.xlsx')
        df = pd.DataFrame(data, columns=['NAMA', 'tgl_lahir'])
        print(df)
        df2 = df
        nameEmployee = df['NAMA']

        listEmployee = []
        no=1

        for index, row in df.iterrows():
            now = datetime.datetime.now()
            birthdate = row['tgl_lahir'];
            today = date.today()
            age = today.year - birthdate.year
            full_year_passed = (today.month, today.day) < (birthdate.month, birthdate.day)
            if not full_year_passed:
                age -= 1
            employee = {
                'name': row['NAMA'],
                'birthDate': row['tgl_lahir'],
                'age': age,
                'no':no

            }
            print(row['NAMA'], row['tgl_lahir'], age)
            listEmployee.append(employee)
            no+=1
        return listEmployee


    def getEmployeeClusteringAge(self):

        data = pd.read_excel(r'E:\employee.xlsx')
        df = pd.DataFrame(data, columns=['NAMA', 'tgl_lahir'])
        print(df)
        df2 = df
        nameEmployee = df['NAMA']

        listEmployee = []
        listEmployeeUnder26=0
        listEmployeeunder26to28 = 0
        listEmployeeUnder29to30 = 0
        listEmployeeUnder31to35 = 0
        listEmployeeUnder36to40 = 0
        listEmployeeUmpper40 = 0


        for index, row in df.iterrows():
            now = datetime.datetime.now()
            birthdate = row['tgl_lahir'];
            today = date.today()
            age = today.year - birthdate.year
            full_year_passed = (today.month, today.day) < (birthdate.month, birthdate.day)
            if not full_year_passed:
                age -= 1
            employee = {
                'name': row['NAMA'],
                'birthDate': row['tgl_lahir'],
                'age': age

            }
            if(age<26):
                listEmployeeUnder26+=1
            elif(age>=26 and age <=28):
                listEmployeeunder26to28+=1
            elif(age>=29 and age <=30):
                listEmployeeUnder29to30+=1
            elif(age>=31 and age <=35):
                listEmployeeUnder31to35+=1
            elif(age>=36 and age <=40):
                listEmployeeUnder36to40+=1
            elif(age>40):
                listEmployeeUmpper40+=1


        # clusterAge = {
        #     'ageUnder26': listEmployeeUnder26,
        #     'age26to28': listEmployeeunder26to28,
        #     'age29to30': listEmployeeUnder29to30,
        #     'age31to35': listEmployeeUnder31to35,
        #     'age36to40':listEmployeeUnder36to40,
        #     'ageOlder40':listEmployeeUmpper40,
        #     'total':len(df)
        #
        #     }

        listAge = []
        listAge.append("ageUnder26")
        listAge.append("age26to28")
        listAge.append("age29to30")
        listAge.append("age31to35")
        listAge.append("age36to40")
        listAge.append("ageOlder40")

        listAmount=[]
        listAmount.append(listEmployeeUnder26)
        listAmount.append(listEmployeeunder26to28)
        listAmount.append(listEmployeeUnder29to30)
        listAmount.append(listEmployeeUnder31to35)
        listAmount.append(listEmployeeUnder36to40)
        listAmount.append(listEmployeeUmpper40)

        clusterAge = {
            'age': listAge,
            'amount':listAmount,
            'total':len(df)

            }

        print(row['NAMA'], row['tgl_lahir'], age)
        listEmployee.append(employee)
        return clusterAge


    def getEmployeeClusteringAgeAll(self):
        data = pd.read_excel(r'E:\employee.xlsx')
        df = pd.DataFrame(data, columns=['NAMA', 'tgl_lahir'])
        print(df)
        df2 = df
        nameEmployee = df['NAMA']

        listEmployee = []
        listEmployeeUnder26 = 0
        listEmployeeunder26to28 = 0
        listEmployeeUnder29to30 = 0
        listEmployeeUnder31to35 = 0
        listEmployeeUnder36to40 = 0
        listEmployeeUmpper40 = 0

        for index, row in df.iterrows():
            now = datetime.datetime.now()
            birthdate = row['tgl_lahir'];
            today = date.today()
            age = today.year - birthdate.year
            full_year_passed = (today.month, today.day) < (birthdate.month, birthdate.day)
            if not full_year_passed:
                age -= 1
            employee = {
                'name': row['NAMA'],
                'birthDate': row['tgl_lahir'],
                'age': age

            }
            if (age < 26):
                listEmployeeUnder26 += 1
            elif (age >= 26 and age <= 28):
                listEmployeeunder26to28 += 1
            elif (age >= 29 and age <= 30):
                listEmployeeUnder29to30 += 1
            elif (age >= 31 and age <= 35):
                listEmployeeUnder31to35 += 1
            elif (age >= 36 and age <= 40):
                listEmployeeUnder36to40 += 1
            elif (age > 40):
                listEmployeeUmpper40 += 1

        clusterAge = {
            'ageUnder26': listEmployeeUnder26,
            'age26to28': listEmployeeunder26to28,
            'age29to30': listEmployeeUnder29to30,
            'age31to35': listEmployeeUnder31to35,
            'age36to40': listEmployeeUnder36to40,
            'ageOlder40': listEmployeeUmpper40,
            'total': len(df)

        }
        print(row['NAMA'], row['tgl_lahir'], age)
        listEmployee.append(employee)
        return clusterAge

    def getEmployeeClusteringAgePersen(self):

        data = pd.read_excel(r'E:\employee.xlsx')
        df = pd.DataFrame(data, columns=['NAMA', 'tgl_lahir'])
        print(df)
        df2 = df
        nameEmployee = df['NAMA']

        listEmployee = []
        listEmployeeUnder26=0
        listEmployeeunder26to28 = 0
        listEmployeeUnder29to30 = 0
        listEmployeeUnder31to35 = 0
        listEmployeeUnder36to40 = 0
        listEmployeeUmpper40 = 0

        for index, row in df.iterrows():
            now = datetime.datetime.now()
            birthdate = row['tgl_lahir'];
            today = date.today()
            age = today.year - birthdate.year
            full_year_passed = (today.month, today.day) < (birthdate.month, birthdate.day)
            if not full_year_passed:
                age -= 1
            employee = {
                'name': row['NAMA'],
                'birthDate': row['tgl_lahir'],
                'age': age

            }
            if(age<26):
                listEmployeeUnder26+=1
            elif(age>=26 and age <=28):
                listEmployeeunder26to28+=1
            elif(age>=29 and age <=30):
                listEmployeeUnder29to30+=1
            elif(age>=31 and age <=35):
                listEmployeeUnder31to35+=1
            elif(age>=36 and age <=40):
                listEmployeeUnder36to40+=1
            elif(age>40):
                listEmployeeUmpper40+=1


        clusterAge = {
            'under26': listEmployeeUnder26,
            'age26to28': listEmployeeunder26to28,
            'age29to30': listEmployeeUnder29to30,
            'age31to35': listEmployeeUnder31to35,
            'age36to40':listEmployeeUnder36to40,
            'ageOlder40':listEmployeeUmpper40,
            'total':df.size

            }
        print(row['NAMA'], row['tgl_lahir'], age)
        listEmployee.append(employee)
        return clusterAge