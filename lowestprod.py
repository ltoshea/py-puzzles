"""Create a function that returns the lowest product of 4 consecutive numbers in a given string of numbers
This should only work is the number has 4 digits of more. If not, return "Number is too small".
lowest_product("123456789")--> 24 (1x2x3x4)
lowest_product("35") --> "Number is too small"
lowest_product("1234111")--> 4 (4x1x1x1)"""

def lowest_product(input):
    if len(input) < 4:
        return 'Number is too small'
    else:
        smallest = int(input[0])*int(input[1])*int(input[2])*int(input[3])
        for i in range(0,len(input)-3):
            total = 1
            for j in range(i,i+4):
                total = total * int(input[j])
            if total < smallest:
                    smallest = total
        return smallest

if __name__ == "__main__":
	print lowest_product("1234")