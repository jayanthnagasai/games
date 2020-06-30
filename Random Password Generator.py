import random

password_length = int(input("How many characters do you want for your password(Minimum 8 characters):  "))
possible_characters_1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#$%&*!"
possible_characters_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#$%&*!"
possible_characters_3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#$%&*!"
possible_characters_4 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#$%&*!"
possible_characters_5 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#$%&*!"


if password_length >= 8:
    random_character_list_1 = [random.choice(possible_characters_1) for i in range(password_length)]
    random_character_list_2 = [random.choice(possible_characters_2) for i in range(password_length)]
    random_character_list_3 = [random.choice(possible_characters_3) for i in range(password_length)]
    random_character_list_4 = [random.choice(possible_characters_4) for i in range(password_length)]
    random_character_list_5 = [random.choice(possible_characters_5) for i in range(password_length)]
    random_password_1 = "".join(random_character_list_1)
    random_password_2 = "".join(random_character_list_2)
    random_password_3 = "".join(random_character_list_3)
    random_password_4 = "".join(random_character_list_4)
    random_password_5 = "".join(random_character_list_5)
    print("Your random passsword generated is  " + random_password_1)
    print("Your second random passsword generated is  " + random_password_2)
    print("Your third random passsword generated is  " + random_password_3)
    print("Your fourth random passsword generated is  " + random_password_4)
    print("Your fifth random passsword generated is  " + random_password_5)
else:
    print("Your password would be too weak")
