import argparse
import time


def countdown(seconds):
    """Counts down from a given number of seconds."""
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_display = "{:02d}:{:02d}".format(mins, secs)
        print(timer_display, end="\r")
        time.sleep(1)
        seconds -= 1
    print("00:00")
    print("Time's up!")


def main():
    parser = argparse.ArgumentParser(description="A simple countdown timer CLI.")
    parser.add_argument(
        "seconds", type=int, help="The number of seconds to count down from."
    )
    args = parser.parse_args()

    if args.seconds <= 0:
        print("Error: Please provide a positive number of seconds.")
        return

    countdown(args.seconds)


if __name__ == "__main__":
    main()
