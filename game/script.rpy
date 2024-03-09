# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# TODO: define background images
image stars = im.Scale("stars.webp", 2560, 1440)

define slow_fade = Fade(2,0,2)

# The game starts here.

label start:
    $ config.rollback_enabled = False
    $ from utils import PlayerData, scene_chooser, generate_runes
    $ pd = PlayerData()
    $ pd.reset_qualities()

    # Set up premise
    $ preferences.text_cps = 15
    scene black
    "You awaken!"
    $ preferences.text_cps = 150
    show stars with slow_fade
    "You are an unknown, mysterious, alien entity on this world."
    "Your motives are understood only by yourself. They cannot be understood by mere mortal men."
    hide stars with slow_fade

    scene cult_ritual with slow_fade
    "Not even the cultists who wish to pay you tribute can comprehend the vastness of your intellect."

    # Set the creature's name.
    $ pd.set_quality("name", renpy.input("So that your cult may worship you more effectively, what is your name?"))
    if not pd.qualities["name"]:
        $pd.set_quality("name", "Beast that Hath No Name")
        "Bold move! By not choosing a name, you resist being pinned down by knowledge."
        "But knowing that you defy naming is still knowledge about you."
    elif pd.name_hash == '8eeda85ec33732f2e43952f95fef42b8b7180923':
        $pd.rocket_launcher = True
        "[pd.get_quality('name')] is quite the fearsome name."
        "With a name like that you are probably equipped with a talking rocket launcher and ready to fight Fishsanto."
    elif pd.name_hash == '4d890e8107fca409871daba22fa1cae97f618791':
        $pd.the_hidden_name = True
        "[pd.get_quality('name')]?"
        "It is YOU! You are the Great Old One."
        $pd.set_quality("name", "Great Old One")
        "Truly, your name chills me to very core."
        "You are surely an unknowable entity."
    elif pd.name_hash == 'da02c82aa690956281ead291a46f53b34c7e3e4d':
        $pd.is_an_evil_clown = True
        "Wow... bunch of stuff to unpack here."
    elif pd.name_hash == '957a3b6762ba76e2f5898de288c889b30dfa085b':
        $pd.is_an_evil_clown = True
        "Wow... bunch of stuff to unpack here."
    else:
        "[pd.get_quality('name')] is quite the fearsome name."
        "But unfortunately being named defines something about you and harms your mythos power."
    
    # Set up danger
    "[pd.get_quality('name')], guard your mythos power and don't let yourself be defined by anything."
    scene investigators
    "Unfortunately, there is a group of investigators who will stop at nothing to learn your secrets, discover your weaknesses and remove you from this world."
    "Protect yourself from them so that you may rise from your palace under the waves and dominate the Earth."
    jump scene_choosing
    return




label scene_choosing:
    $ pd.compare_to_candidates()
    $ pd.set_qualities_from_elimination()
    $ pd.calculate_mythos()
    scene temple_interior

    $ temp_cand = ", ".join(pd.candidate_names)
    "Remaining mythos power: [pd.mythos]"
    # "Remaining Candidates: [temp_cand]"
    "Remaining investigators: [pd.investigators_remaining]"

    $ next_scene = scene_chooser(pd)
    jump expression next_scene
    return






label non_mythos_ending:
    if pd.animal == "horror":
        $ temp_path = ", ".join(pd.path)
        "Please take a screen shot of the next line and send it to the developer."
        "The path that caused an error was: [temp_path]"
        return
    if pd.is_an_evil_clown:
        $pd.animal = "clown fish"
    "As your mythos power leaves you from the choices you've made, you begin to feel weak."
    "Tired, you start to drift off to slumber again. Perhaps for another thousand years."
    "However, just before you drift off to sleep, the investigators enter the room."
    "You feel powerless to stop them for the first time, but they simply take notice of you and move on."
    "As you look down at your form, you realize the decisions you've made about yourself have transformed you into an ordinary [pd.animal]."
    scene expression pd.animal
    $killed = 4-pd.investigators_remaining
    if killed == 0:
        return
    "However, all it not lost."
    $runes = generate_runes(killed)
    if killed == 1:
        "You killed [killed] investigators and so have earned [killed] rune of the true name of the Great Old One."
        "The Great Old One's name includes the rune: [runes]"
    else:
        "You killed [killed] investigators and so have earned [killed] runes of the true name of the Great Old One."
        "The Great Old One's name includes the runes: [runes]"


    return

label game_over:
    scene stars
    "Banished from Earth, you float aimlessly in the black space between the stars."
    "Try as you might, you are unable to push or pull yourself in any direction."
    "Perhaps one day, your orbit will bring you close enough to Earth so you may have your revenge."
    return

label win:
    if pd.is_an_evil_clown:
        "You laugh manically"
    "You destroy the Earth"
    return

label mixed_ending:
    "As the last investigator dies at your hands, you feel tired."
    "Your mythos power is gone."
    "As you look at your form, you realize you are merely an ordinary [pd.animal], and no longer the eldritch monster you used to be."
    "However, all it not lost."
    "For killing all of the investigators you have earned 5 runes in the true name of the Great Old One."
    $runes = generate_runes(5)
    "The Great Old One's name includes the runes: [runes]"
    return