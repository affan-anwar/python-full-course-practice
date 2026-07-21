import time
import sys


def print_lyrics():

    lyrics = [
        "Oh hum bade thhe masoom be-lihaz ban gaye",
        "Hum bade thhe masoom be-lihaz ban gaye",
        "",
        "Oh hum bade thhe masoom be-lihaz ban gaye",
        "Hum bade thhe masoom be-lihaz ban gaye",
        "",
        "Ho dhokhebaazon mein reh reh ke dhokebaaz ban gaye",
        "Ho dhokhebaazon mein reh reh ke dhokebaaz ban gaye",
        "Ho dhokhebaazon mein reh reh ke dhokebaaz ban gaye",
        "Ho hum bade thhe maasoom",
        "",
        "Are koi nahi is duniya mein",
        "Dil jisne apna toda nahi",
        "Humein gairon ne bhi loota hai",
        "Aur aapno ne bhi chhoda nahi",
        "",
        "Are koi nahi is duniya mein",
        "Dil jisne apna toda nahi",
        "Humein gairon ne bhi loota hai",
        "Aur aapno ne bhi chhoda nahi",
        "",
        "Hum logo ke liye toh sawad ban gaye",
        "Hum logo ke liye toh sawad ban gaye",
        "",
        "Ho dhokhebaazon mein reh reh ke dhokebaaz ban gaye",
        "Ho dhokhebaazon mein reh reh ke dhokebaaz ban gaye",
        "Ho dhokhebaazon mein reh reh ke dhokebaaz ban gaye",
        "Ho hum badde thhe masoom",
        "",
        "Ho jannat mein rehne walo ke",
        "Jahannum mein savere hai",
        "Ho maine rang badalne seekh liye",
        "Ab mere bhi laakhon chehre hai",
        "",
        "Ho jannat mein rehne walo ke",
        "Jahannum mein savere hai",
        "Ho maine rang badalne seekh liye",
        "Ab mere bhi laakhon chehre hai",
        "",
        "Hum kal nahi the jo aaj ban gaye",
        "Meri izzat pe jaani ji daag ban gaye",
        "",
        "Ho dhokhebaazon mein reh reh ke dhokebaaz ban gaye",
        "Ho dhokhebaazon mein reh reh ke dhokebaaz ban gaye",
        "Ho hum badde thhe masoom"
    ]

    delays = [
        0.4, 0.8, 0.4,
        0.4, 0.8, 0.4,
        0.3, 0.3, 0.4, 1.0, 0.4,
        0.4, 0.4, 0.4, 1.0, 0.4,
        0.4, 0.4, 0.4, 1.0, 0.4,
        0.5, 1.0, 0.4,
        0.3, 0.3, 0.4, 1.0, 0.4,
        0.4, 0.4, 0.4, 1.0, 0.4,
        0.4, 0.4, 0.4, 1.0, 0.4,
        0.5, 1.0, 0.4,
        0.3, 0.4, 1.0
    ]

    print("\nDhokebaaz 💔\n")
    time.sleep(1.2)

    for i, line in enumerate(lyrics):

        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.06)

        print()

        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(0.8)


print_lyrics()