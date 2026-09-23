def solution(args):
    ans=f"{args[0]}"
    prevVal=args[0]
    rangeCheck=1
    tmpRange=""
    for val in args[1:]:
        if (prevVal + 1) == val:
            prevVal=val
            rangeCheck += 1
            if rangeCheck <= 2:
                tmpRange = tmpRange + "," + f"{val}"
            else:
                tmpRange=""
        else:
            if rangeCheck >= 3 and len(tmpRange) == 0:
                ans = ans + "-" + f"{prevVal}" + "," + f"{val}"
                rangeCheck = 1
                prevVal=val
            elif len(tmpRange) > 0:
                ans = ans + tmpRange + "," + f"{val}"
                tmpRange=""
                rangeCheck = 1
                prevVal=val
            else:
                ans = ans + "," + f"{val}"
                rangeCheck = 1
                prevVal=val
    if rangeCheck >= 3 and len(tmpRange) == 0:
        ans = ans + "-" + f"{prevVal}"
    elif len(tmpRange) > 0:
        ans = ans + tmpRange
    return ans


"""

Description:
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
"""
