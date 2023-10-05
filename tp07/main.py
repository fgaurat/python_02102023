from UserDao import UserDao
from User import User
import csv

def main_insert():
    dao = UserDao("users_db.db")
    with open('MOCK_DATA.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            u = User(**row)
            # print(u)
            dao.save(u)    

def get_from_domain(domain,users):
    for data in users:
        if domain in data.email:
            yield data



def main():
    dao = UserDao("users_db.db")
    # users = dao.findAll()
    # filtered_users = dao.findAll() | get_from_domain('msu.edu')
    # l = list(users)
    # print(users[12])
    # print(type(users))
    # for u in users:
    #     print(u)    

    filtered_users = get_from_domain('msu.edu',dao.findAll())
    for f in filtered_users:
        print(f)

if __name__=='__main__':
    main()
