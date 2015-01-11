from eve import Eve
from eve.auth import BasicAuth

class Authenticate(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource,
                   method):
        print resource
        print method
        if resource == 'user' and method == 'GET':
            user = app.data.driver.db['user']
            user = user.find_one({'username': username,'password':password})
            if user:
                return True
            else:
                return False
        else:
            return True
            

if __name__ == '__main__':
    app = Eve(auth=Authenticate)
    app.run()
