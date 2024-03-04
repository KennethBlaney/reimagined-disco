# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

label start:
    $ from utils import PlayerData, scene_chooser, generate_runes
    $ pd = PlayerData()
    $ pd.reset_qualities()

    # Set up premise
    scene black
    "You awaken!"
    scene stars
    "You are an unknown, mysterious, alien entity on this world."
    "Your motives are understood only by yourself. They cannot be understood by mere mortal men."
    scene cult_ritual
    "Not even the cultists who wish to pay you tribute can comprehend the vastness of your intellect."

    # Set the creature's name.
    $ pd.set_quality("name", renpy.input("So that your cult may worship you more effectively, what is your name?"))
    if not pd.qualities["name"]:
        $pd.set_quality("name", "Beast that Hath No Name")
        "Bold move! By not choosing a name, you resist being pinned down by knowledge."
        "But knowing that you defy naming is still knowledge about you."
    elif pd.name_hash == '713a751b48086a13fe637a6056fc784b6467a960':
        $pd.rocket_launcher = True
        "[pd.get_quality('name')] is quite the fearsome name."
        "With a name like that you are probably equipped with a talking rocket launcher and ready to fight Fishsanto."
    elif pd.name_hash == '4d890e8107fca409871daba22fa1cae97f618791':
        $pd.the_hidden_name = True
        "[pd.get_quality('name')] is quite the fearsome name."
        "Truly it chills me to very core."
        "You are surely an unknowable entity."
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
    "As your mythos power leaves you from the choices you've made, you begin to feel weak."
    "Tired, you start to drift off to slumber again. Perhaps for another thousand years."
    "However, just before you drift off to sleep, the investigators enter the room."
    "You feel powerless to stop them for the first time, but they simply take notice of you and move on."
    "As you look down at your form, you realize the decisions you've made about yourself have transformed you into an ordinary [ps.animal]."
    scene expression pd.animal
    $killed = 4-pd.investigators_remaining
    "However, all it not lost."
    "You killed [killed] investigators and so have earned [killed] runes of the true name of the Great Old One."
    $runes = generate_runes(killed)

    return

label game_over:
    scene stars
    "Banished from Earth, you float aimlessly in the black space between the stars."
    "Try as you might, you are unable to push or pull yourself in any direction."
    "Perhaps one day, your orbit will bring you close enough to Earth so you may have your revenge."
    return

label win:
    "You destroy the Earth"
    return

label mixed_ending:
    "The investigators are dead or run off, but you are just a [pd.animal], so the world survives."
    return