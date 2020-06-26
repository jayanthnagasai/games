email = input("What is your email address:  ").strip()
print()
username = email[:email.index("@")]
domainame = email[email.index("@")+1:]
output1 = "Your user name is '{}' ".format(username)
output2 = "Your domain name is '{}' ".format(domainame)
print(output1)
print()
print(output2)
