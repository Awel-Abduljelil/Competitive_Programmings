def game_score(n, cards):
    left, right = 0, n - 1
    sereja_points, dima_points = 0, 0
    turn = 0  
    while left <= right:
        if cards[left] > cards[right]:
            chosen_card = cards[left]
            left += 1
        else:
            chosen_card = cards[right]
            right -= 1
        
        if turn == 0:
            sereja_points += chosen_card
        else:
            dima_points += chosen_card
        turn = 1 - turn 
    return sereja_points, dima_points
n = int(input())
cards = list(map(int, input().split()))
sereja_points, dima_points = game_score(n, cards)
print(sereja_points, dima_points)
