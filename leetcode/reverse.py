def reversevwl(strtxt) -> str:
    listin = []
    for i, x in enumerate(strtxt):
        if x in "aeiouAEIOU":
            print(f"vowel found {x} at index {i}")
            listin.append([i, x])

    indexed_list = list(enumerate(strtxt))
    # Get reversed vowels
    numbers = []
    for sublist in listin:
        numbers.append(sublist[0])
    numbers.reverse()
    for i in range(len(listin)):
        listin[i][0] = numbers[i]

    # Replace vowels in indexed_list
    for pos in listin:
        index = pos[0]
        vowel = pos[1]
        indexed_list[index] = (index, vowel)

    return ''.join(char for _, char in indexed_list)

if __name__ == "__main__":
    strinput = str(input("Enter string to reverse: "))
    print(f"The entered strings are: {strinput}")
    revstr = reversevwl(strinput)
    print(revstr)


    