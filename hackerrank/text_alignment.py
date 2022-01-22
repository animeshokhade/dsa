# question --> https://www.hackerrank.com/challenges/text-alignment/problem?h_r=profile
# default_format
#Replace all ______ with rjust, ljust or center.

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))  # my_code_replacement

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)) # my_code_replacement

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))  # my_code_replacement

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))  # my_code_replacement

#Bottom Cone
for i in range(thickness):  # my_code_replacement
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# end