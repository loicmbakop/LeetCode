
def guess_your_number(n:int):

    left=1
    right=n

    middle = (left+right)//2
    while right > left:
        if middle > picked:
            left = middle +1
        
        if middle < picked:
            left = middle - 1

        if middle == picked:
            return middle






