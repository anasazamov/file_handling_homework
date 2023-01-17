def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    arr=[]
    txt=open(data,mode="r").read()
    arr2=txt.split(",")
    for i in arr2:
        arr.append(int(i))
    return arr
print(main('txt_file/data01.txt'))