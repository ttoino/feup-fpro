current = "intro"
actions = {
    "intro": ("After a drunken night out with friends, you awaken in a thick, dank forest. A slobbering orc is running towards you.", {
        "a": ("A. Grab a nearby rock and throw it at the orc", "rock", None),
        "b": ("B. Lie down and wait to be mauled", None, "Welp, that was quick. You died!"),
        "c": ("C. Run", "run", None)
    }),
    "rock": ("The orc is stunned, but regains control. He begins running towards you again.", {
        "a": ("A. Run", "run", None),
        "b": ("B. Throw another rock", None, "The rock flew well over the orcs head. You missed. You died!"),
        "c": ("C. Run towards a nearby cave", "sword", None)
    }),
    "sword": ("Before you fully enter, you notice a shiny sword on the ground. Do you pick up a sword. Y/N?", {
        "y": (None, "cave_y", None),
        "n": (None, "cave_n", None)
    }),
    "cave_y": ("What do you do next?", {
        "a": ("A. Hide in silence", None, "I think orcs can see very well in the dark, right? You died!"),
        "b": ("B. Fight", None, "As the orc reached out to grab the sword, you pierced the blade into its chest. You survived!"),
        "c": ("C. Run", "run", "The orc turns around and sees you running.")
    }),
    "cave_n": ("What do you do next?", {
        "a": ("A. Hide in silence", None, "I think orcs can see very well in the dark, right? You died!"),
        "b": ("B. Fight", None, "You're defenseless. You died!"),
        "c": ("C. Run", "run", "The orc turns around and sees you running.")
    }),
    "run": ("You run as quickly as possible.", {
        "a": ("A. Hide behind boulder", None, "You're easily spotted. You died!"),
        "b": ("B. Trapped, so you fight", None, "You're no match for an orc. You died!"),
        "c": ("C. Run towards an abandoned town", "town", None)
    }),
    "town": ("You notice a purple flower near your foot. Do you pick it up? Y/N", {
        "y": (None, None, "You quickly hold out the purple flower. The orc was looking for love. This got weird, but you survived!"),
        "n": (None, None, "Maybe you should have picked up the flower. You died!")
    })
}

while current:
    t, d = actions[current]
    print(t)
    for t, _, _ in d.values():
        if t:
            print(t)
    _, current, t = d[input().lower()]
    if t:
        print(t)