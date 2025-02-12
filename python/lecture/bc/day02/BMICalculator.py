# 예외 처리를 통해 사용자가 숫자가 아닌 값을 입력했을 때 다시 입력하도록 하는 함수
def can_convert_to_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


print("Welcome to the BMI Calculator")

weight = input("\033[0;37mWhat is your weight in kg?\n\033[0m")
while not can_convert_to_float(weight):
    weight = input("\033[0;37mWhat is your weight in kg?\n\033[0m")
weight = float(weight)

height = input("\033[0;37mWhat is your height in cm?\n\033[0m")
while not can_convert_to_float(height):
    height = input("\033[0;37mWhat is your height in cm?\n\033[0m")
height = float(height)

height /= 100
BMI = weight / height**2

# NOTE: F-string을 사용하여 출력, f"문자열 {변수}"로 사용
# NOTE: round(<number>, <decimal places>) decimal places까지 반올림하여 출력
print(f"\033[0;37mYour BMI is {round(BMI, 1)}\033[0m")

if BMI < 18.5:
    print("\033[0;34mYou are underweight\033[0m")
elif BMI < 23:
    print("\033[0;32mYou are normal\033[0m")
elif BMI < 25:
    print("\033[0;33mYou are overweight\033[0m")
else:
    print("\033[0;31mYou are obese\033[0m")
