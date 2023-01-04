import getpass

username = input('what is your username?\n')
password = getpass.getpass(prompt = 'what is your password\n')

#p = getpass.getpass(prompt='Your favorite flower? ')

pass_length = len(password)
hidden_pass = '*' * pass_length 

print(f'hello {username}, your password {hidden_pass} is {pass_length} digits long.')