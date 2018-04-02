def stats(numbers):
    numbers.sort()
    print ('Numbers sorted lowest to highest:', numbers)
    return (numbers[0], numbers[-1])

list = [5, 45, 12, 1, 78]
min, max = stats(list)
print ('Lowest number is', min)
print ('Highest number is', max)
