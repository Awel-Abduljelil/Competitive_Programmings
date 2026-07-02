def min_rotations(exhibit_name):
    current_position = 'a'
    total_rotations = 0
    for char in exhibit_name:
        clockwise_distance = abs(ord(char) - ord(current_position))
        counterclockwise_distance = 26 - clockwise_distance
        total_rotations += min(clockwise_distance, counterclockwise_distance)
        current_position = char
    
    return total_rotations
exhibit_name = input().strip()
result = min_rotations(exhibit_name)
print(result)
