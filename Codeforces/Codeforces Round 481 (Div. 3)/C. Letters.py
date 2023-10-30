def get_capacity(dormitory):
    capacity = []
    capacity.append(dormitory[0])
    for i in range(len(dormitory)-1):
        capacity.append(dormitory[i+1] + capacity[i])
        #dormitory[i+1] = dormitory[i+1] + capacity[i]
    return capacity


def get_dormitory(capacity, lettter):
    left = 0
    right = len(capacity) - 1
    while left < right:
        mid = (left + right) // 2
        if capacity[mid] < lettter:
            left = mid + 1
        else:
            right = mid
    return left + 1

def get_room(capacity, letter, dormitory):
    return capacity[dormitory - 1] - letter

if __name__ == "__main__":
    n, m = map(int, input().split())
    dormitories = list(map(int, input().split()))
    letters = list(map(int, input().split()))
    capacity = get_capacity(dormitories)
    for letter in letters:
        dormitory = get_dormitory(capacity, letter)
        room = dormitories[dormitory - 1] - get_room(capacity, letter, dormitory)
        print(dormitory, room)