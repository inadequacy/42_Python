def ft_count_harvest_recursive():
    days_to_harvest = int(input("Days until harvest: "))
    days_go_down(days_to_harvest)
    print("Harvest time!")


def days_go_down(days):
    if days > 0:
        days_go_down(days - 1)
        print(f"Day {days}")
