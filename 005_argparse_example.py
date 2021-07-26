# This youtube link explain using argparse clearly and concisely:
# https://www.youtube.com/watch?v=cdblJqEUDNo

import argparse

parse = argparse.ArgumentParser(description='Calculate the area of a trapzoid.')
parse.add_argument('-s1', '--side1', metavar='', type=float, help='Side 1 of the trapezoid')
parse.add_argument('-s2', '--side2', metavar='', type=float, help='Side 2 of the trapezoid')
parse.add_argument('-H', '--height', metavar='', type=float, help='Height of the trapezoid')

group = parse.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='print quiet format')
group.add_argument('-v', '--verbose', action='store_true', help='print verbose format')

arg = parse.parse_args()

def calc_trapezoid_area(side1, side2, height):
    return(height * (side1 + side2) / 2.0)

# if we want to use call the function using fixed and hard-coded values
# we can proceed as follows:
#if __name__ == '__main__':
#    print(calc_trapezoid_area(2, 4, 5))

# but above format is of limited application.
# It is more practical if we be able to pass the arguments of the
# calc_trapezoid_area using the command line
# for this purpose we use argparse package

if __name__ == '__main__':
    area = calc_trapezoid_area(arg.side1, arg.side2, arg.height)
    
    if arg.quiet:
        print(area)
    elif arg.verbose:
        print('The area of the trapezoid with side 1 of %s, side 2 of %s and height of %s is %s' %(arg.side1, arg.side2, arg.height, area))
    else:
        print('The area of the trapezoid is %s' %area)
        

