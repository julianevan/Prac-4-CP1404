import random
def main():
    quick_picks = int(input("How many quick picks?"))
    CONSTANTS = (1,46)
    numbers = []
    for a in range (1,quick_picks+1):
        for i in range (1,7):
            num = random.randint(CONSTANTS[0],CONSTANTS[1])
            while num in numbers:
                num = random.randint(CONSTANTS[0],CONSTANTS[1])
            else:
                pass
            numbers.append(num)
            numbers.sort()
        print(numbers[0],numbers[1],numbers[2],numbers[3],numbers[4],numbers[5])
        numbers = []
main()



