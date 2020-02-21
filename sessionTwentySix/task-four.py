def show_stars(rows):
    for row in range(1,rows+1):
        print()
        for column in range(1,row+1):
            print('*' , end="")

show_stars(5)