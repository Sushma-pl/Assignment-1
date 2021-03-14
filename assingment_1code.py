# -*- coding: utf-8 -*-
"""Assingment-1code

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kgwt1ArcrBa17IsygvTElioV5U1PIOv7
"""

import random 

#Function for roll the dice.
def roll_the_dice(Event):
    n_simulation=100000
    count=0
    #do this experiment 100000 times 
    for i in range(n_simulation):

        #Roll dice three times 
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        die3=random.randint(1,6)


        #event E = getting 4 on third throw of die
        if Event=='E':
            if die3==4:
                count+=1

        #event F = getting 6 and 5 on first and second throw of die resp.       
        elif Event=='F':
            if die1==6 and die2==5 :
                count+=1
        
        #to calculate E and F i.e (6,5,4)
        else :
            if die1==6 and die2==5 and die3==4:
                count+=1

    return count/n_simulation

a = round(roll_the_dice('E and F'),5)  #P(E and F)
b = round(roll_the_dice('F'),5)        #P(F)

print("Probability of getting 4 at third roll, Pr(E) = ",round(roll_the_dice('E'),5))
print("Probability of getting 6 and 5 on first and second roll resp., Pr(F) = ",round(roll_the_dice('F'),5))
print("Probability of (6,5,4), Pr(E and F) = ",round(roll_the_dice('E and F'),5))
print('probability P(E|F) = ',round(a/b,5))