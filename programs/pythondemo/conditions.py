# -*- coding: utf-8 -*-

age = int(input("Enter your age"))
if (age>=18):
    print('You are eligible to vote')
else:
    print('you are not eligible to vote')
    
amtpurchased = int(input("Enter amount purchased"))
if(amtpurchased > 30000):
    print('Discount is 30 %')
elif (amtpurchased >20000 and amtpurchased <=30000):
    print('discount is 20 %')
else:
    print('discount is 10 %')
print('your age is {} and {} '.format(10,30))
        
    
