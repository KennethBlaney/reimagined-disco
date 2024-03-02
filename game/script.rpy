# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label start:
    $ from utils import PlayerData, scene_chooser
    $ pd = PlayerData()
    $ pd.reset_qualities()

    # Set up premise
    scene black
    "You awaken!"
    scene space
    "You are an unknown, mysterious, alien entity on this world."
    "Your motives are understood only by yourself. They cannot be understood by mere mortal men."
    scene cultist
    "Not even the cultists who wish to pay you tribute can comprehend the vastness of your intellect."

    # Set the creature's name.
    $ pd.set_quality("name", renpy.input("So that your cult may worship you more effectively, what is your name?"))
    if not pd.qualities["name"]:
        $pd.set_quality("name", "The Beast that Hath No Name")
        "Bold move! By not choosing a name, you resist being pinned down by knowledge.""
        "But knowing that you defy naming is still knowledge about you."
    else:
        "[pd.get_quality('name')] is quite the fearsome name."
        "But unfortunately being named defines something about you and harms your mythos power."
    
    # Set up danger
    "[pd.get_quality('name')], guard your mythos power and don't let yourself be defined by anything."
    "Investigators will stop at nothing to learn your secrets, discover your weaknesses and remove you from this world."
    jump scene_choosing
    return

label scene_choosing:
    $ pd.compare_to_candidates()
    $ pd.set_qualities_from_elimination()
    $ pd.calculate_mythos()
    # TODO: Create display code
    $ temp_cand = ", ".join(pd.candidate_names)
    "Remaining mythos power: [pd.mythos]"
    # "Remaining Candidates: [temp_cand]"

    $ next_scene = scene_chooser(pd)
    scene dungeon
    jump expression next_scene
    return



label fins_selector:
    
    "You made it to the fins screen"
    menu:
        "Do you have fins?"

        "Yes":
            $pd.set_quality("fins", True)
            "Ooh... scary fins."

        "No":
            $pd.set_quality("fins", False)
            "Good to know. No fins."

    jump scene_choosing
    return

label gills_selector:
     
    "You made it to the gills screen"
    menu:
        "Do you have gills?"

        "Yes":
            $pd.set_quality("gills", True)
            "Ooh... scary gills."

        "No":
            $pd.set_quality("gills", False)
            "Good to know. No gills."

    jump scene_choosing
    return

label lungs_selector:
     
    "You made it to the lungs screen"
    menu:
        "Do you have lungs?"

        "Yes":
            $pd.set_quality("lungs", True)
            "Ooh... scary lungs."

        "No":
            $pd.set_quality("lungs", False)
            "Good to know. No lungs."

    jump scene_choosing
    return

label venom_selector:
     
    "You made it to the venom screen"
    menu:
        "Do you have venom?"

        "Yes":
            $pd.set_quality("venom", True)
            "Ooh... scary venom."

        "No":
            $pd.set_quality("venom", False)
            "Good to know. No venom."

    jump scene_choosing
    return

label shell_selector:
     
    "You made it to the shell screen"
    menu:
        "Do you have shell?"

        "Yes":
            $pd.set_quality("shell", True)
            "Ooh... scary shell."

        "No":
            $pd.set_quality("shell", False)
            "Good to know. No shell."

    jump scene_choosing
    return

label claws_selector:
     
    "You made it to the claws screen"
    menu:
        "Do you have claws?"

        "Yes":
            $pd.set_quality("claws", True)
            "Ooh... scary claws."

        "No":
            $pd.set_quality("claws", False)
            "Good to know. No claws."

    jump scene_choosing
    return

label elec_selector:
     
    "You made it to the elec screen"
    menu:
        "Do you have elec?"

        "Yes":
            $pd.set_quality("elec", True)
            "Ooh... scary elec."

        "No":
            $pd.set_quality("elec", False)
            "Good to know. No elec."

    jump scene_choosing
    return

label teeth_selector:
     
    "You made it to the teeth screen"
    menu:
        "Do you have teeth?"

        "Yes":
            $pd.set_quality("teeth", True)
            "Ooh... scary teeth."

        "No":
            $pd.set_quality("teeth", False)
            "Good to know. No teeth."

    jump scene_choosing
    return

label acid_selector:
     
    "You made it to the acid screen"
    menu:
        "Do you have acid?"

        "Yes":
            $pd.set_quality("acid", True)
            "Ooh... scary acid."

        "No":
            $pd.set_quality("acid", False)
            "Good to know. No acid."

    jump scene_choosing
    return

label tentacles_selector:
     
    "You made it to the tentacles screen"
    menu:
        "Do you have tentacles?"

        "Yes":
            $pd.set_quality("tentacles", True)
            "Ooh... scary tentacles."

        "No":
            $pd.set_quality("tentacles", False)
            "Good to know. No tentacles."

    jump scene_choosing
    return

label spines_selector:
     
    "You made it to the spines screen"
    menu:
        "Do you have spines?"

        "Yes":
            $pd.set_quality("spines", True)
            "Ooh... spines teeth."

        "No":
            $pd.set_quality("spines", False)
            "Good to know. No spines."

    jump scene_choosing
    return

label sonar_selector:
     
    "You made it to the sonar screen"
    menu:
        "Do you have sonar?"

        "Yes":
            $pd.set_quality("sonar", True)
            "Ooh... scary sonar."

        "No":
            $pd.set_quality("sonar", False)
            "Good to know. No sonar."

    jump scene_choosing
    return

label ending:
     
    "You are a [pd.animal]"
    return