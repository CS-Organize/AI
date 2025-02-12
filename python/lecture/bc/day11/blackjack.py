# TODO:
"""
1. 승패 카운팅 기능 없애고 베팅 기능 추가
2. 좀 더 예쁜 UI
3. 종료 조건 더 엄격하게
"""

import random
from replit import clear

# ANSI escape code를 사용하여 색상을 정의
BG_WHITE_FG_BLACK = "\033[107m\033[1;90m"
BG_WHITE_FG_RED = "\033[107m\033[1;91m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
WHITE = "\033[97m"
RESET = "\033[0m"

PLAYER = "player"
DEALER = "dealer"
CURRENT = "current"
FINAL = "final"
NUM_IDX = -5  # ranks가 있는 인덱스


# 카드 모양과 숫자를 정의
suits = [
    f"{BG_WHITE_FG_BLACK}♠️",
    f"{BG_WHITE_FG_RED}♥️",
    f"{BG_WHITE_FG_RED}♦️",
    f"{BG_WHITE_FG_BLACK}♣️",
]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


# List Comprehension을 사용하여 카드 생성
cards = [f"{suit} {rank}{RESET}" for suit in suits for rank in ranks]

used_cards = []
player_cards = []
dealer_cards = []
player_win_cnt = 0
dealer_win_cnt = 0


def deal_card_to(who):
    if len(cards) == 0:
        cards.extend(used_cards)
        random.shuffle(cards)
        used_cards.clear()
    if who == DEALER:
        dealer_cards.append(cards.pop())
    else:
        player_cards.append(cards.pop())


def calculate_hand_score(cards):
    score = 0
    a_cnt = 0
    for card in cards:
        if card[NUM_IDX] == "A":
            a_cnt += 1
        elif card[NUM_IDX] in ["J", "K", "Q", "0"]:
            score += 10
        else:
            score += int(card[NUM_IDX])
    for i in range(a_cnt):
        if score > 10:
            score += 1
        else:
            score += 11
    return score


def get_hand(cards):
    hand = ""
    for card in cards:
        hand += card + " "
    return hand


def display_score(who, when):
    if who == DEALER:
        print(f"dealer's card\n{get_hand(dealer_cards)}\n{when} score: {calculate_hand_score(dealer_cards)}")
    else:
        print(f"your card\n{get_hand(player_cards)}\n{when} score: {calculate_hand_score(player_cards)}")


def display_who_win(who = None):
    global dealer_win_cnt # 전역 변수를 사용하기 위해 global 키워드 사용
    global player_win_cnt
    if who == PLAYER:
        player_win_cnt += 1
        print(f"{GREEN}You win! {WHITE}{player_win_cnt}:{dealer_win_cnt}(W:L){RESET}")
    elif who == DEALER:
        dealer_win_cnt += 1
        print(f"{RED}You lose... {WHITE}{player_win_cnt}:{dealer_win_cnt}(W:L){RESET}")
    else:
        print(f"{YELLOW}It's a tie!{RESET}")


def blackjack():
    global dealer_win_cnt
    global player_win_cnt
    player_win_cnt += 1
    print("💸💸💸💸💰💰💰💰💸💸💸💸💰💰💰💰")
    print(f"{get_hand(player_cards)} {GREEN}Blackjack! {WHITE}{player_win_cnt}:{dealer_win_cnt}(W:L){RESET}")
    print("💸💸💸💸💰💰💰💰💸💸💸💸💰💰💰💰")
    print(f"{GREEN}You win! {WHITE}{player_win_cnt}:{dealer_win_cnt}(W:L){RESET}")


def reset_game():
    used_cards.extend(player_cards)
    used_cards.extend(dealer_cards)
    player_cards.clear()
    dealer_cards.clear()


def play_blackjack():
    # 초기 패 2장씩 받기
    for _ in range(2): # for문에서 _는 변수를 사용하지 않을 때 사용하는 관례적 표현
        deal_card_to(DEALER)
        deal_card_to(PLAYER)
    display_score(PLAYER, CURRENT)
    print(f"dealer's first card: {dealer_cards[0]}")

    # 유저 카드 추가 + 결과 출력
    while (
        calculate_hand_score(player_cards) < 21
        and input("Would you like another card? y or n\n") == "y"
    ):
        print("You take another card.")
        deal_card_to(PLAYER)
        display_score(PLAYER, CURRENT)
    if calculate_hand_score(player_cards) == 21 and len(player_cards) == 2:
        blackjack()
        reset_game()
        return
    elif calculate_hand_score(player_cards) > 21:
        print("You've exceeded 21 points.")
        display_who_win(DEALER)
        reset_game()
        return
    else:
        display_score(PLAYER, FINAL)

    # 딜러 카드 추가 + 결과 출력
    display_score(DEALER, CURRENT)
    while calculate_hand_score(dealer_cards) <= 16:
        print("dealer takes another card because dealer's score is less than 17.")
        deal_card_to(DEALER)
        display_score(DEALER, FINAL)
    if calculate_hand_score(dealer_cards) > 21:
        print("dealer have exceeded 21 points.")
        display_who_win(PLAYER)
        reset_game()
        return

    print(
        f"Your score is {calculate_hand_score(player_cards)}, dealer's score is {calculate_hand_score(dealer_cards)}"
    )
    if calculate_hand_score(player_cards) > calculate_hand_score(dealer_cards):
        display_who_win(PLAYER)
    elif calculate_hand_score(player_cards) < calculate_hand_score(dealer_cards):
        display_who_win(DEALER)
    else:
        display_who_win()

    reset_game()


clear()
random.shuffle(cards)
while input("Ready to start the play_blackjack game? y or n\n") == "y":
    play_blackjack()
