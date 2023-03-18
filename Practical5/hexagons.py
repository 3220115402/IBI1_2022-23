#we are given the formula h=2n(2n-1)/2,n is the ordinal of the hexagon
#we want to use loop to put in n=1,2,3,4,5 separately to get the total 
#mumber of the dots for each hexagon.
n=1
for n in range(1,6):
    h=2*n*(2*n-1)/2
    print(h)
#Below shows the five values for dot numbers of the five hexagons
#1.0
#6.0
#15.0
#28.0
#45.0
