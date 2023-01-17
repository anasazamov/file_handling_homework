def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """

# Read data from file
    answer=[]
    answer2=[]
    f=open(data,mode='r').read()
    for i in f.split('\n'):
        for j in i.split(' ')[1]:
                answer.append(j)
    for i in answer:
        if i .isdigit():
            answer2.append(i)
    return min(answer2)
# Read data from file
print(main('txt_file/data09.txt'))