'''
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345


In general, (n r) = n!/r!(n-r)!

It is not until n=23 that a value exceeds one-million:
(23 10)=1144066

How many, not necessarily distinct, values of (n r)
for 1<n<100 are greater than one-million?
'''

#This problem is just generating Pascal's triangle with 101 rows
#and count how many elements are over 1000000

#Generate Pascal's triangle
def generate_pascals_triangle(num_rows):
    # Create an empty list to hold the triangle
    triangle = []
    #Count elements over 1000000
    count=0
    # Loop over each row
    for row_num in range(num_rows):
        # Create an empty list to hold the row values
        row = []
        # Loop over each column in the row
        for col_num in range(row_num + 1):
            # If the column is the first or last, the value is 1
            if col_num == 0 or col_num == row_num:
                row.append(1)
            # Otherwise, the value is the sum of the two values above it
            else:
                value = triangle[row_num - 1][col_num - 1] + triangle[row_num - 1][col_num]
                row.append(value)
                if value>1000000:
                    count+=1
        # Add the row to the triangle
        triangle.append(row)
    return count

print(generate_pascals_triangle(101))
