# Group c-d
# import random
# import array
# class  Password:
#
#     DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     LOWER_CHAR = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
#                              'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
#                              'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
#                              'z']
#     UPPPER_CHAR = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
#                              'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
#                              'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
#                              'Z']
#
    # SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
    #                '*', '(', ')', '<']
#     def create_password(self, length):
#         ALL_CHAR = self.DIGITS + self.LOWER_CHAR + self.UPPPER_CHAR + self.SYMBOLS
#         password= ''
#         for i in range(0 , length):
#             password=password+random.choice(ALL_CHAR)
#         return password
# password = Password()
# my_password = password.create_password(8)
# print('Before shuffle')
# print(my_password)
# print('After shuffle')
# sh = array.array('u' , my_password)
# random.shuffle(sh)
# for i in sh :
#     print(f'{i}', end= '')





# Group B - Arabic
# import random as r
# import  array
# class Password:
#     DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     LOWER_CHAR = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
#                                  'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
#                                  'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
#                                  'z']
#     UPPPER_CHAR = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
#                                  'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
#                                  'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
#                                  'Z']
#     SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
#                    '*', '(', ')', '<']
#
#     ALL_CHAR = DIGITS + LOWER_CHAR + UPPPER_CHAR + SYMBOLS
#
#
#     def create_password(self , length):
#         password = ''
#         for i in range(0,length):
#             password =password + r.choice(self.ALL_CHAR)
#         return password
# password = Password()
# my_password = password.create_password(12)
# print('Before Shuffle')
# print(my_password)
# x=array.array('u' , my_password)
# r.shuffle(x)
# print('After Shuffle')
# for i in x:
#     print(i, end='')







import random as r
auto_selected = ['rock', 'paper' , 'scissors']
while True:
    your_choice = input('Enter Your Choice (rock , paper , scissors) ')
    if your_choice in auto_selected:
        auto_select =r.choice(auto_selected)
        print(f'You choose {your_choice}')
        print(f'Computer choose {auto_select}')
    else:
        print('You Entered incorrect Word')
        break

    if your_choice == auto_select:
        print('You Both Choose Same One!!!!')
    elif your_choice == 'rock':
        if auto_select == 'scissors':
            print('You Win !!!!!')
        else:
            print('You Lose !!!!!!')
    elif your_choice == 'scissors':
        if auto_select == 'paper':
            print('You Win !!!!!')
        else:
            print('You Lose !!!!!!')
    elif your_choice == 'paper':
        if auto_select == 'rock':
            print('You Win !!!!!')
        else:
            pass
        print('You Lose !!!!!!')
    your_round = 0
    your_round += 1
    print(f'================={your_round}=================')