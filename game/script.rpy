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
        "Bold move! By not choosing a name, you resist being pinned down by knowledge."
        "But knowing that you defy naming is still knowledge about you."
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
    # TODO: Create display code
    $ temp_cand = ", ".join(pd.candidate_names)
    "Remaining mythos power: [pd.mythos]"
    " "
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
     
    "Something triggers in your vast brain which makes you believe that an investigator is entering your domain."
    menu:
        "How do you avoid the investigator and prevent them from learning about you?"

        "I use my echolocation to keep tabs on them and always move to another room.":
            $pd.set_quality("sonar", True)
            "Using your powerful echolocation, you manage to avoid the investigation."
            "The investigators complete their search and seems to find no trace of you."

        "I use changes in the current of the water to figure out where the investigator is":
            $pd.set_quality("sonar", False)
            "As the investigator moves around your temple, you are able to sense when they get close so you can avoid them."
            "The investigators complete their search and seems to find no trace of you."

        "I lie in wait to ambush the investigators":
            "You hide in the shadows and take your opportunity"
            jump fight_the_investigators

    jump scene_choosing
    return

label fight_the_investigators:
    menu:

        "Lunge out and bite down on an investigator using my ferocious teeth" if pd.get_quality("teeth") is not False:
            if pd.get_revealed("teeth"):
                "You lunge at the investigator, but they are ready for your attack having fallen for it once before."
                "Before you can change tactics, the investigators are on you, casting an exorcism ritual which banishes you from the Earth."
                jump game_over
            else:
                "You lunge at the investigator crunching into them with your deadly teeth."
                $pd.investigators_remaining -= 1
                "The investigator quickly bleeds out and dies as the rest scatter to escape you."
                $pd.set_quality("teeth", True)
                $pd.set_revealed("teeth", True)
                jump scene_choosing
        "Dunno":
            "Well die then"
            jump game_over

label ending:
    "You are a [pd.animal]"
    return

label game_over:
    "You died"
    return
