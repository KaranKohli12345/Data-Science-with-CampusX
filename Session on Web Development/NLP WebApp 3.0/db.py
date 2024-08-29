# We are using json file to store data of users as we haven't studied databases.

# Input data from user will flow in three steps:

# HTML(client side) --> app.py/Flask(server side) --> users.json file (database) 

import json

class Database:

    def insert_data(self, name, email, password):
        with open('users.json', 'r') as rf:
            users = json.load(rf)

        if email in users:
            return 0
        else:
            users[email] = [name, password]
            with open('users.json', 'w') as wf:
                json.dump(users, wf, indent=4)
            return 1


    def verify_login(self, email, password):
        with open('users.json', 'r') as rf:
            users = json.load(rf)

        if email in users:
            if users[email][1] == password:
                return 1
            else:
                return 0
        else:
            return 0

