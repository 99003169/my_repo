# Importing libraries

import random
import string as st

# To generate password


class password_generator:
    # Constructor

    def __init__(self):
        self.pwd_len = 0
        self.pwd_stren = "weak"
        self.gen_pwd = ""

    # To accept length

    def get_length(self, length):
        self.pwd_len = length
        print("Password Length: ", self.pwd_len)

    # To calculate password strength

    def calc_strength(self):
        if (self.pwd_len >= 4 and self.pwd_len <= 7):
            self.pwd_stren = "Weak"
        elif (self.pwd_len >= 8 and self.pwd_len <= 11):
            self.pwd_stren = "Moderate"
        else:
            self.pwd_stren = "Strong"
        print("Password Strength: ", self.pwd_stren, '\n')

    # To generate random password

    def generate_password(self):
        self.gen_pwd = random.choice(st.ascii_uppercase) + \
            random.choice(st.ascii_lowercase) + \
            random.choice(st.digits) + random.choice(st.punctuation)
        for a in range(self.pwd_len - 4):
            self.gen_pwd = self.gen_pwd + random.choice(st.ascii_uppercase +
                                                        st.ascii_lowercase +
                                                        st.digits +
                                                        st.punctuation)
        password_list = list(self.gen_pwd)
        random.shuffle(password_list)
        self.gen_pwd = ''.join(password_list)
        print("Generated password: ", self.gen_pwd)

# To handle input and output files


class input_output_file_handling:
    def read_write_file(self):
        object1 = password_generator()
        fr = open("input.txt", "r")
        fw = open("output.txt", "a")
        for each_line in fr:
            length = int(each_line)
            object1.get_length(length)
            object1.generate_password()
            object1.calc_strength()
            fw.write("Password Length: " + each_line +
                     "Generated Password: " + object1.gen_pwd + '\n' +
                     "Password Strength: " + object1.pwd_stren + '\n\n')
        fr.close()
        fw.close()

# To display password criteria


print("Welcome to Random Password Generator!")
print("\nThe password strength is as follows:")
print("\nWeak\t\t:\t4 - 7 Characters")
print("Moderate\t:\t8 - 11 Characters")
print("Strong\t\t:\t12+ Characters")
print("\nNote : Minimum password length should be 4\n")
in_out_obj = input_output_file_handling()
in_out_obj.read_write_file()
