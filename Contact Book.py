print()
print("Welcome to Jay's Contact Book")
print()

contactsavaiable = ["Mom", "Dad", "Home", "Sai Bro", "Sumanth Bro", "Kumar Bro"]

for contact in contactsavaiable:
    print(contact)

print()
mycontacts= {
    "Mom": "+1 (412)-403-1456" ,
    "Dad": "+1 (412)-403-1536" ,
    "Home": "+1 (412)-423-9068",
    "Sai Bro": "+1 (603)-777-6439",
    "Sumanth Bro": "+1 (510)-358-5265",
    "Kumar Bro": "+1 (469)-367-8246",
}

print()
find_contact = input("Enter Contact:  ")
print(mycontacts.get(find_contact))
