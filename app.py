import csv
import random


def old_info():
    with open('old.csv', 'a') as f:
        fieldName = ['Name', 'Age', 'Sex']
        writer = csv.DictWriter(f, fieldnames=fieldName)
        while True:
            exit = input('Do you want to add input (y/n)? ')
            if exit.lower() == 'n':
                break
            else:
                name = input('Enter Your Name: ')
                age = int(input('Enter Your Age: '))
                sex = input('Enter Your Sex: ')
                writer.writerow({'Name': name, 'Age': age, 'Sex': sex})

def young_info():
    with open('young.csv', 'a') as f:
        fieldName = ['Name', 'Age', 'Sex','Occupation','Address']
        writer = csv.DictWriter(f, fieldnames=fieldName)
        while True:
            exit = input('Do you want to add input (y/n)? ')
            if exit.lower() == 'n':
                break
            else:
                name = input('Enter Your Name: ')
                age = int(input('Enter Your Age: '))
                sex = input('Enter Your Sex: ')
                occupation = input('Enter Your Occupation: ')
                address = input('Enter Your Address: ')
                writer.writerow({'Name': name, 'Age': age, 'Sex': sex,'Occupation':occupation,'Address':address})

def collect_fund():
    with open('fund.csv', 'a') as f:
        fieldName = ['Name', 'Fund']
        writer = csv.DictWriter(f, fieldnames=fieldName)
        while True:
            exit = input('Do you want to add input (y/n)? ')
            if exit.lower() == 'n':
                break
            else:
                name = input('Enter Your Name: ')
                fund = int(input('Enter Fund: '))
                writer.writerow({'Name': name, 'Fund': fund})


def choose_young():
    with open('fund.csv','r') as csv_file:
        reader = csv.DictReader(csv_file)
        fund=0
        for row in reader:
            fund= fund + int(row['Fund'])
    
    with open('old.csv','r') as read_old_csv, open('young.csv','r') as read_young_csv, open('choose_old.csv','w') as choose_csv:
        old_reader = csv.DictReader(read_old_csv)
        young_reader = csv.DictReader(read_young_csv)
        list_young = []
        for line in young_reader:
            list_young.append(line['Name'])
        fieldName = ['oldName', 'youngName','Salary','OldRating','YoungRating','Review']
        writer = csv.DictWriter(choose_csv,fieldnames=fieldName)
        writer.writeheader()
        for row in old_reader:
            oldName = row['Name']
            youngName = random.choice(list_young)
            salary = fund*(0.05)
            oldRating = float(input('Enter the rating for oldman: '))
            youngRating = float(input('Enter the rating for youngman: '))
            Review = input('Enter a Review: ')
            writer.writerow({'oldName': oldName, 'youngName': youngName,'Salary':salary,'OldRating':oldRating,'YoungRating':youngRating,'Review':Review})



if __name__=='__main__':
    totalFund=0
    print('ZEKELABS ASSIGNMENT (EDYODA)')
    while True:
            exit = input('\nDo you want any Choice (y/n)? ')
            if exit.lower() == 'n':
                break
            else:
                print('\nChoose 1, To Register an old man')
                print('Choose 2, To Register an Young man')
                print('Choose 3, To Register for the fund')
                print('Choose 4, To Choose the young man to care')
                print('Choose 5, To Exit\n')
                n = int(input('Enter Your Choice: '))
                if(n==1):
                    old_info()
                elif(n==2):
                    young_info()
                elif(n==3):
                    collect_fund()
                elif(n==4):
                    choose_young()
                else:
                    exit



