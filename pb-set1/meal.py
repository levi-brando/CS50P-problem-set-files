def main():
    time = input("What time is it? ").strip()
    float_time = convert(time)

    if 7 <= float_time <= 8:
        print("breakfast time")
    elif 12 <= float_time <= 13:
        print("lunch time")
    elif 18 <= float_time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    new_hour = ((hours * 60) + minutes)/60
    return new_hour


if __name__ == "__main__":
    main()
