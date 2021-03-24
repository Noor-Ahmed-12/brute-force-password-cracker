                    #################################################################################################################
                    #           *************************Advanced Brute force password cracker tool****************************     #
                    #                                           Developer: @Noor-Ahmed-12(github)                                   #
                    #                               generator strong and secure password for your accounts                          #
                    #                                               Be secure and safe!                                             #
                    #################################################################################################################

import random
import string
import time

if __name__ == '__main__':

    # all letters(uppercase,lowercase),digits and punctuation is included in the password cracking list
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.punctuation
    s4=string.digits

    # password cracking list
    passwd_list=[]
    passwd_list.extend(list(s1))
    passwd_list.extend(list(s2))
    passwd_list.extend(list(s3))
    passwd_list.extend(list(s4))

    # for demo taking password from user
    user_passwd = input("enter password\n")
    guess_passwd = ''

    # calculating time 
    start = time.time()

    while guess_passwd!=user_passwd:
        guess_passwd = random.choices(passwd_list,k=len(user_passwd))
        print("-->      " + str(guess_passwd))

        if guess_passwd==list(user_passwd):
            print("\n\nPassword Crack successfully!\nPassword:")
            print("" .join(guess_passwd))
            break

    # total time in cracking the password
    end = time.time()
    total_elapse = end-start
    
    hours =total_elapse//3600
    total_elapse= total_elapse-3600*hours
    
    minutes = total_elapse//60
    sec = total_elapse - 60*minutes
    print("total time:" + '%d: %d: %d' %(hours,minutes,sec))