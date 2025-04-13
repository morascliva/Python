def main():
    time = input("What time is it? ").strip()
    hours = convert(time)
    
    if 7.0 <= hours <= 8.0:
        print("Breakfast time")
    elif 12.0 <= hours <= 13.0:
        print("Lunch time")
    elif 18.0 <= hours <= 19.0:
        print("Dinner time")


def convert(time):
    hours, minutes = map(int, time.split(":"))
    return hours + minutes / 60


    main()
