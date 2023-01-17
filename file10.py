def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """

# Read data from file
    f=open(data).read()
    l=[]
    data=f.split('\n')
    for i in data:
        l.append(len(i))
# Read data from file
    return max(l)
print(main('txt_file/data10.txt'))