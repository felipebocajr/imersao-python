print("You get in your new car.")
print('''
                              _.-="_-         _
                         _.-="   _-          | ||"""""""---._______     __..
             ___.===""""-.______-,,,,,,,,,,,,`-''----" """""       """""  __'
      __.--""     __        ,'                   o \           __        [__|
 __-""=======.--""  ""--.=================================.--""  ""--.=======:
]       [w] : /        \ : |========================|    : /        \ :  [w] :
V___________:|          |: |========================|    :|          |:   _-"
 V__________: \        / :_|=======================/_____: \        / :__-"
 -----------'  "-____-"  `-------------------------------'  "-____-"

''')
digit_error = "You typed something wrong..."
wrong = "Wrong. This are not the correct way to do."
print("Your mission is to go for a drive with it.") 


choose1 = input("Now that you are inside the car, what will you do first?\nType 1 to turn on the car.\nType 2 to put on your seat belt.\nType 3 to pull the manual brake.\nType 4 for adjust the mirrors.\n")
if choose1 == "1" or choose1 == "3":
  print(wrong)
elif choose1 == "2":
    choose2_1 = input("Nice, now you are safe due to your seat belt.\nOkay, now that you put your seat belt, what will you do?\nType 1 to turn on the car.\nType 2 to pull the manual brake.\nType 3 for adjust the mirrors.\n")
    if choose2_1 == "1" or choose2_1 == "2":
      print(wrong)
    elif choose2_1 == "3":
      choose3_1 = input("Nice, your mirrors are adjusted now.\nNow that you can see the cars around and in the back, what will you do?\nType 1 to turn on the car.\nType 2 to pull the manual brake.\n")
      if choose3_1 == "2":
        print(wrong)
      elif choose3_1 == "1":
        final_choose_1 = input('\nNice, the car is ready to go now!\nWait... there is one more thing...\nType "pull" to pull the manual brake.\n').lower()
        if final_choose_1 == "pull":
          print('''
           ___
    _-_-  _/\______\\__
 _-_-__  / ,-. -|-  ,-.`-.
    _-_- `( o )----( o )-'
           `-'      `-'
           NICE BRO YOU FUCKING GOT IT GO DRIVE NOW B) 
          ''')
        else:
          print(digit_error)
      else:
        print(digit_error)
    else:
      print(digit_error)


elif choose1 == "4":
  choose2_2 = input("Nice, your mirrors are adjusted now.\nNow that you can see the cars around and in the back, what will you do?\nType 1 to turn on the car.\nType 2 to put on your seat belt\nType 3 to pull the manual brake.\n")
  if choose2_2 == "1" or choose2_2 == "3":
    print(wrong)
  elif choose2_2 == "2":
    choose3_2 = input("Nice, now you are safe due to your seat belt.\nOkay, now that you put your seat belt, what will you do?\nType 1 to turn on the car.\nType 2 to pull the manual brake.\n")
    if choose3_2 == "2":
      print(wrong)
    elif choose3_2 == "1":
      choose4_2 = input('\nNice, the car is ready to go now!\nWait... there is one more thing...\nType "pull" to pull the manual brake.\n').lower()
      if choose4_2 == "pull":
        print('''
           ___
    _-_-  _/\______\\__
 _-_-__  / ,-. -|-  ,-.`-.
    _-_- `( o )----( o )-'
           `-'      `-'
           NICE BRO, YOU GOT IT! GO DRIVE NOW B) 
          ''')
      else:
        print(digit_error)     
    else:
      print(digit_error)
  else:
    print(digit_error)
else:
  print(digit_error)
