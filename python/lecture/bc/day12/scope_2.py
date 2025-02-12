"""enemies = 1

def increase_enemies():
    global enemies # 전역 변수를 사용하겠다고 선언, 선언하지 않으면 함수 내에서 enemies 변수를 찾지 못함
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")"""

# 실제로는 전역 변수를 사용하는 것은 좋지 않다. 함수 내에서만 사용하는 지역 변수를 사용하는 것이 좋다.

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")
