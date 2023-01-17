def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
        
    """
    f=open(data).read()
    l=[]
    data=f.split('\n')
    for i in data:
        l.append(len(i))
# Read data from file
    return l
print(main('txt_file/data06.txt'))