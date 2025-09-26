h = 10
t = 7
steps = 0
l = 0
while l <= h:
    mid = l + (h - l) // 2
    if l == t:
        print("Found! It is", t, "steps are: ", steps)
        break
    elif mid > t:
        h = mid -1
        steps += 1
        print(f"Trying in the range of {l} to {h}")
    else:
        l = mid + 1
        print(f"Trying in the range of {l} to {h}")
        steps += 1