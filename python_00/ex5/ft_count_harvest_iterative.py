def ft_count_harvest_iterative():
    i = 1
    days_to_harvest = int(input("Days until harvest: "))
    while i <= days_to_harvest:
        print(f"Day {i}")
        i += 1
    if i > days_to_harvest:
        print("Harvest time!")
