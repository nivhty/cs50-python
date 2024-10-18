def main():
    time = convert(input("What time is it? "))
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <=13:
        print("lunch time")
    elif 18 <= time <=19:
        print("dinner time")



def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes_to_hours = float(minutes) / 60
    time_in_float = hours + minutes_to_hours
    return time_in_float


if __name__ == "__main__":
    main()
