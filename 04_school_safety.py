
name = input("what is your name: ")


pass_1 = input("do you have a pass:")


if pass_1 == "yes":

    time_pass = int(input("what time was the pass issued:"))

    what_time_is_it = int(input("what time is it now:"))

    were_are_going = input("where are we going:")
    
    print(time_pass)
    print(what_time_is_it) 
    if what_time_is_it - time_pass <= 2:
        print("you can go")
    else:
        print("your pass has expired")
    if were_are_going == "nurse" or were_are_going == "bathroom" or were_are_going =="nurse":
        print("you can go")



        





else:
    print("no you dont have a pass")




