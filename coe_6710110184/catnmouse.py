def catnmouse(x: int, y: int, z: int) -> str:
    if abs(x - z) < abs(y - z):
        return "Cat A"
    elif abs(x - z) > abs(y - z):
        return "Cat B"
    else:
        return "Mouse C"
    
if __name__ == '__main__':
    line_str = input("Enter A B C:")
    line = map(int, line_str.split())

    result = catnmouse(*line)
    print(result)