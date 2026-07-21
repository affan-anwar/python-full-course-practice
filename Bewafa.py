import sys
import time


def print_lyrics():
    lyrics = [
        "Dil laga bhi liya",
        "Ishq bhi kar liya",
        "Chandni raat mein",
        "Humne taare gine",
        "",
        "Dil laga bhi liya",
        "Ishq bhi kar liya",
        "Chandni raat mein",
        "Humne taare gine",
        "",
        "Khwaab jaisa koyi",
        "Khwaab thi zindagi",
        "Neend tooti to",
        "Aaya samajh yeh humein",
        "",
        "Raah woh jispe main chal raha tha",
        "Uski koyi bhi manzil nahi hai",
        "",
        "Bewafa tera masoom chehra",
        "Bhool jaane ke kabil nahi hai",
        "Bewafa tera masoom chehra",
        "Bhool jaane ke kabil nahi hai",
        "Bewafa tera masoom chehra",
        "Bhool jaane ke kabil nahi hai",
        "",
        "Khoobsurat bohat hai tu lekin",
        "Dil lagane ke kabil nahi hai",
        "Bewafa tera masoom chehra",
        "Bhool jaane ke kabil nahi hai",
        "Bhool jaane ke kabil nahi hai"
    ]

    delays = [
        0.4, 0.4, 0.4, 1.0, 0.5,
        0.4, 0.4, 0.4, 1.0, 0.5,
        0.4, 0.4, 0.4, 1.2, 0.5,
        0.6, 1.2, 0.5,
        0.5, 0.8,
        0.5, 0.8,
        0.5, 1.2, 0.5,
        0.6, 0.9,
        0.5, 0.8, 1.5
    ]

    print("\n")
    print("          Bewafa Tera Masoom Chehra 💔")
    print("          ---------------------------")
    print()

    time.sleep(1)

    for index, line in enumerate(lyrics):

        if line == "":
            print()
            time.sleep(0.4)
            continue

        for character in line:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)

        print()

        if index < len(delays):
            time.sleep(delays[index])

    print("\n          💔 Song Finished 💔")


print_lyrics()