def feed_animals(animals: list[int], food: list[int]) -> int:
    if len(animals) == 0 or len(food) == 0:
        return 0
    animals.sort()
    food.sort()
    count = 0
    for f in food:
        if f >= animals[count]:
            count += 1
        if count == len(animals):
            break
    return count


if __name__ == '__main__':
    assert feed_animals([], []) == 0
    assert feed_animals([2, 3, 4], [1, 2]) == 1 
    assert feed_animals([8, 1], [1, 8]) == 2
    assert feed_animals([2, 3], [1, 2, 3, 4]) == 2
    assert feed_animals([5, 5, 5], [4, 5, 6]) == 2
