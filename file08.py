def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    answer=[]

    for i in data.split('\n'):
        for j in i.split(' ')[1]:
                answer.append(j)
    return max(answer)
# Read data from file
print(main('txt_file/data08.txt'))
