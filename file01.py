def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    arr=[]
    arr2=data.split(",")
    for i in arr2:
        arr.append(int(i))
    return arr
