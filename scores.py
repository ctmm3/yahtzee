#!/usr/bin/python3
#10/21/2019
#Noel & Carter



def usr_scores(lst):
    category = 0
    this_turn = 0
    print("1. One's")
    print("2. Two's")
    print("3. Three's")
    print("4. Four's")
    print("5. Five's")
    print("6. Six's")
    print("7. Three of a Kind")
    print("8. Four of a Kind")
    print("9. Full House")
    print("10. Small Straight")
    print("11. Large Straight")
    print("12. Chance")
    print("13. Yahtzee!")
    
    print(" ")
    print(" ")
    print("What is the number of the score you would like to take? ")
    input(category)
    
    
    if category == 1:
        ones(lst)
        
    elif category == 2: 
        twos(lst)
                 
    elif category == 3:
        threes(lst) 
                
                     
    elif category == 4:
        fours(lst)   
                
                     
    elif category == 5:
        fives(lst) 
                
    elif category == 6:
        sixs(lst) 
        
    elif category == 7:
        threeK(lst) 
         
    elif category == 8:
        fourK(lst) 
         
    elif category == 9:
        fh(lst) 
         
    elif category == 10:
        smst(lst) 
         
    elif category == 11:
        lgst(lst) 
         
    elif category == 12:
        chance(lst) 
         
    elif category == 13:
        yahtzee(lst) 
         


# ----------- Processing their score selection! ---------------------

def ones(lst):
    this_turn == 0 
    for items in lst:
        if item == 1:
            this_turn == this_turn + 1
        else:
            this_turn == 0
def twos(lst):
    this_turn == 0 
    for items in lst:
        if item == 2:
            this_turn == this_turn + 2
        else:
            this_turn == 0
            
def threes(lst):
    this_turn == 0 
    for items in lst:
        if item == 3:
            this_turn == this_turn + 3
        else:
            this_turn == 0
            
def fours(lst):
    this_turn == 0 
    for items in lst:
        if item == 4:
            this_turn == this_turn + 4
        else:
            this_turn == 0
            
def fives(lst):
    this_turn == 0 
    for items in lst:
        if item == 5:
            this_turn == this_turn + 5
        else:
            this_turn == 0
            
def sixs(lst):
    this_turn == 0 
    for items in lst:
        if item == 6:
            this_turn == this_turn + 6
        else:
            this_turn == 0    
            
def threeK(lst):
    if lst.count(1) == 3:
        this_turn == sum(lst)
    elif lst.count(2) == 3:
        this_turn == sum(lst)
    elif lst.count(3) == 3:
        this_turn == sum(lst)
    elif lst.count(4) == 3:
        this_turn == sum(lst)
    elif lst.count(5) == 3:
        this_turn == sum(lst)
    elif lst.count(6) == 3:
        this_turn == sum(lst)
    else:
        this_turn == 0    

def fourK(lst):
    if lst.count(1) == 4:
        this_turn == sum(lst)
    elif lst.count(2) == 4:
        this_turn == sum(lst)
    elif lst.count(3) == 4:
        this_turn == sum(lst)
    elif lst.count(4) == 4:
        this_turn == sum(lst)
    elif lst.count(5) == 4:
        this_turn == sum(lst)
    elif lst.count(6) == 4:
        this_turn == sum(lst)
    else:
        this_turn == 0     
    
def fh(lst):
    
    
    if lst.count(1) == 3:
        if lst.count(2) == 2:
            this_turn == 25       
        elif lst.count(3) == 2:
            this_turn == 25   
        elif lst.count(4) == 2:
            this_turn == 25   
        elif lst.count(5) == 2:
            this_turn == 25   
        elif lst.count(6) == 2:   
            this_turn == 25 
            
    elif lst.count(2) == 3:
        if lst.count(1) == 2:
            this_turn == 25       
        elif lst.count(3) == 2:
            this_turn == 25   
        elif lst.count(4) == 2:
            this_turn == 25   
        elif lst.count(5) == 2:
            this_turn == 25   
        elif lst.count(6) == 2:     
            this_turn == 25 
            
    elif lst.count(3) == 3:
        if lst.count(2) == 2:
            this_turn == 25       
        elif lst.count(1) == 2:
            this_turn == 25   
        elif lst.countt(4) == 2:
            this_turn == 25   
        elif lst.count(5) == 2:
            this_turn == 25   
        elif lst.count(6) == 2: 
            this_turn == 25 
            
    elif lst.count(4) == 3:
        if lst.count(2) == 2:
            this_turn == 25       
        elif lst.count(3) == 2:
            this_turn == 25   
        elif lst.count(1) == 2:
            this_turn == 25   
        elif lst.count(5) == 2:
            this_turn == 25   
        elif lst.count(6) == 2: 
            this_turn == 25 
            
    elif lst.count(5) == 3:
        if lst.count(2) == 2:
            this_turn == 25       
        elif lst.count(3) == 2:
            this_turn == 25   
        elif lst.count(4) == 2:
            this_turn == 25   
        elif lst.count(1) == 2:
            this_turn == 25   
        elif lst.count(6) == 2: 
            this_turn == 25 
            
    elif lst.count(6) == 3:
        if lst.count(2) == 2:
            this_turn == 25       
        elif lst.count(3) == 2:
            this_turn == 25   
        elif lst.count(4) == 2:
            this_turn == 25   
        elif lst.count(5) == 2:
            this_turn == 25   
        elif lst.count(1) == 2: 
            this_turn == 25 
    else:
        this_turn == 0   
        
def smst():
    
    counter1 = 1
    
    while count < 3:
        
        if ls.count(counter1) >= 1:
            
            if ls.count(counter1 + 1)>=1:
                
                if ls.count(counter1 + 2)>=1:
                    
                    if ls.count(counter1 + 3)>=1:
                        
                        this_turn == 30
                        
                    else:
                        counter1 += 1
                else:
                    counter1 += 1
            else:
                counter1 += 1
        else:
            counter1 += 1        
        
def lgst():
    if lst.count(1) == 1:
        if lst.count(2) == 1:
            if lst.count(3) == 1:
                if lst.count(4) == 1:
                    if lst.count(5) == 1:
                        this_turn == 40
    elif lst.count(2) == 1:
        if lst.count(3) == 1:
            if lst.count(4) == 1:
                if lst.count(5) == 1:
                    if lst.count(6) == 1:
                        this_turn == 40 
        
    else:
        this_turn == 0
        
def chance():
    this_turn == sum(lst)
    
def yahtzee():
    if lst.count(1) == 5:
        this_turn == 50
    elif lst.count(2) == 5:
        this_turn == 50
    elif lst.count(3) == 5:
        this_turn == 50
    elif lst.count(4) == 5:
        this_turn == 50
    elif lst.count(5) == 5:
        this_turn == 50
    elif lst.count(6) == 5:
        this_turn == 50
    else:
        this_turn == 0


    

   
    
    
    