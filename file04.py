def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=[]
    f=open(data,mode="r").read()
    for i in f:
        if not i.isdigit():
            a.append(i)
    return a
# Read data from file
print(main('txt_file/data04.txt'))