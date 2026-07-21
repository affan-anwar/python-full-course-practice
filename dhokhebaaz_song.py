import sys
import time


def print_lyrics():
    lyrics = [
        "Jis din tu aaine mein khud ko dekhegi",
        "Us din shayad sach samajh aayega",
        "Jo dhoka tune diya tha mujhe",
        "Waqt ban ke wapas tujhe dikhayega",
        "",
        "Jhooti muskaan, jhoothe vaade",
        "Sab kuch tha bas ek chaal teri",
        "Par yaad rakhna ye duniya gol hai",
        "Ek din palti hai kismat teri",
        "",
        "Jise tune tanha chhoda tha",
        "Woh aaj khada hai sar utha ke",
        "Aur tu dhoondhegi apna sukoon",
        "Us shaks mein jise diya tha dhokha ke",
        "",
        "Ehsaas hoga tab jab koi",
        "Tere saath wahi karega jo tune kiya",
        "Tab samajh aayega dard woh",
        "Jo kisi masoom dil ne sahaa tha",
        "",
        "Dhokhebaaz naam kamaya hai tune",
        "Ab uska bhaar bhi tu hi uthaana",
        "Kyunki jo bhi bijta hai duniya mein",
        "Waqt aane pe wahi hai use kaatna"
    ]

    delays = [
        0.4, 0.4, 0.4, 1.2, 0.5,
        0.4, 0.4, 0.4, 1.0, 0.5,
        0.4, 0.4, 0.4, 1.2, 0.5,
        0.4, 0.4, 0.4, 1.2, 0.5,
        0.4, 0.4, 0.4, 1.5
    ]

    print("\n")
    print("          Dhokhebaaz 💔 (Original)")
    print("          ------------------------")
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


if __name__ == "__main__":
    print_lyrics()