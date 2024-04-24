# workers = [['Ivan', 'Ivanov', 100000, 1], ['Petr', 'Petrov', 150000, 2], ['Sidor', 'Sidorov', 200000, 10]]
#
#
#
#
# for worker in workers:
#     if worker[3] < 2:
#         position = 'junior'
#         status = worker[0]+ ' '+worker[1] + ' is ' + position
#         print(status)
#     elif 5 >= worker[3] >= 2:
#         position = 'middle'
#         status = worker[0]+ ' '+worker[1] + ' is ' + position
#         print(status)
#
#     elif worker[3] > 5:
#         position = 'senior'
#         status = worker[0]+ ' '+worker[1] + ' is ' + position
#         print(status)
# ______________________________________________________________________
# N = 10
# n= 0
# dn = 2
# lst = []
#
# while (n<=N):
#     lst.append(n)
#     n+=dn
# ______________________________________________________________________
salaries_dict = {'name' : 'Masha','surname' : 'Volkova', 'age': 25, 'salary': 60000,'position': 'junior' }


users_dict = {
    'mvolkova' : {'name' : 'Masha','surname' : 'Volkova', 'age': 25, 'salary': 60000,'position': 'junior' },
    'pvoronov' : {'name' : 'Peter','surname' : 'Voronov', 'age': 27, 'salary': 100000,'position': 'junior' },
    'pparker' : {'name' : 'Peter','surname' : 'Parker', 'age': 35, 'salary': 150000,'position': 'middle' },
    'akarpov' : {'name' : 'Anatoly','surname' : 'Karpov', 'age': 30, 'salary': 250000,'position': 'senior' }

}

# _________________________________________________________________________
# задача: перевести фарингейт в цельсия
def temp_to_celcius(tempFar):
    cel = (tempFar - 32)*5.0/9.0
    return cel

taxi['temp_C'] = temp_to_celcius(taxi['temp'])