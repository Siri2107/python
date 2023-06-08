# leap year


def is_leap(year):

     if(year%100==0 and year%4==0 or year%400==0):
          print(year,"True")
     else:
          print(year,"Flase")

year=int(input())
print(is_leap(year))
    
