class BasePasswordManager:
    old_passwords = list()
    def get_password(self):
        try:
            return self.old_passwords[-1]
        except:
            print("Empty! No Old Passwords")
            exit()

    def is_correct(self,string):
        try:
            if string==self.old_passwords[-1]:
                return True
            return False
        except:
            print("No Current Password Set")
            exit()


class passwordmanager(BasePasswordManager):
    def __init__(self):
        pass
    def set_password(self,new_password):
        if len(new_password)<6:
            print("minimum 6 characters is required for password")
            exit()
        else:
            if len(self.old_passwords) > 0:
                newpasswprd_level = self.get_level(new_password)
                curpassword_level = self.get_level(self.old_passwords[-1])
                if newpasswprd_level > curpassword_level or newpasswprd_level == 2:
                    self.old_passwords.append(new_password)
                    print("Password Change Successful!")
                else:
                    print("Old Password Has Greater Level Of Security")
            else:
                self.old_passwords.append(new_password)
                print("New Password Added")

    def get_level(self,string):
        st = str(string)
        if st.isdigit() or st.isnumeric() or st.isalpha():
            return 0
        elif st.isalnum():
            return 1
        else:
            return 2
 
print("Enter A Password To Store")
password = input().strip()
obj = passwordmanager()
obj.set_password(password)
print(" ' "+obj.get_password()+" ' ")
print()
print("Enter Another Password For Demonstartion!")
password2 = input().strip()
obj.set_password(password2)
print(" ' "+obj.get_password()+" ' ")
