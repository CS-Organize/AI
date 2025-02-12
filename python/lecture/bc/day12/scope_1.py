enemies = 1

def increase_enemies():
    enemies = 2 # increase_enemies 함수 내에서만 사용 가능한 지역 변수
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")



game_level = 3
def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0] # 파이썬은 블록 스코프가 없다.
    print(new_enemy)
    """
    if (game_level < 5)
    {
        int new_enemy = enemies[0];
    }
    std::cout << new_enemy << std::endl;
    다른 언어에서는 블록 스코프가 있어서 new_enemy 변수는 if문 내에서만 사용 가능하다.
    파이썬은 인터프리터 언어라서 블록 스코프가 없는 것 같다.
    """
