lst = [14, 20,100,33,44,55,12,13,14]
N = int(input("which largest number:"))
if N <= 0 or N > len(lst):
    print("Invalid input for N.")
else:
    sorted_list = sorted(lst, reverse=True)
    nth_largest = sorted_list[N-1]
    print(f"{N}th Largest number: {nth_largest}")
1
