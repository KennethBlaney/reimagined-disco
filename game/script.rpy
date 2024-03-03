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
    scene stars
    "You are an unknown, mysterious, alien entity on this world."
    "Your motives are understood only by yourself. They cannot be understood by mere mortal men."
    scene cult_ritual
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
    scene temple_interior
    # TODO: Create display code
    $ temp_cand = ", ".join(pd.candidate_names)
    "Remaining mythos power: [pd.mythos]"
    "Remaining Candidates: [temp_cand]"

    $ next_scene = scene_chooser(pd)
    jump expression next_scene
    return



label fins_selector:
    
    "The investigators have you surrounded, but they don't know it yet. Your only hope is to escape or to hide."
    menu:
        "What do you do to survive?"

        "Use my powerful fins to escape.":
            $pd.set_quality("fins", True)
            "You flip your fins and manage to swim past one of the investigators. The puny human is stunned by your appearance and you easily escape."
            jump scene_choosing

        "Hide in the shadows and hope they pass you by.":
            $pd.set_quality("fins", False)
            "Good to know. No fins."
            jump scene_choosing

        "Hide in the shadows and ambush them.":
            "You hide in the shadows and take your opportunity"
            jump fight_the_investigators

    return

label gills_selector:
     
    "The investigators believe that you might succumb to poisonous gas released into your lair."
    menu:
        "What do you do to survive the poison?"

        "Take a deep breath. I have impressive lung capacity":
            $pd.set_quality("gills", False)
            $pd.set_quality("lungs", True)
            "Ooh... scary gills."

        "Jump into a pool of water. The poison gas can't get me there.":
            $pd.set_quality("gills", True)
            $pd.set_quality("lungs", False)
            "Good to know. No gills."

        "I actually don't need to breathe, so the gas won't affect me.":
            $pd.set_quality("gills", False)
            $pd.set_quality("lungs", False)
            "Good to know. No gills."

    jump scene_choosing
    return

label lungs_selector:
    jump gills_selector
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
     
    "Look out! The investigators have ambushed you and they've brought automatic weapons."
    menu:
        "They try to spray you with bullets. What do you do?"

        "Nothing. I have a thick shell and their bullets don't scare me.":
            $pd.set_quality("shell", True)
            "Ooh... scary shell."

        "I'm nimble and flexible enough to avoid their bullets.":
            $pd.set_quality("shell", False)
            "Good to know. No shell."

    menu:
        "The investigators are stunned their attack doesn't work. Do you seize the opportunity to attack?"

        "Yes. Make them regret attacking you.":
            jump fight_the_investigators
        "No. Staying alive is more important.":
            "They say 'Discretion is the better part of valor' and you know now is not the time to attack."
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
    scene monster_attack

    menu:
        "How will you attack the investigators?"

        "My ferocious teeth" if pd.get_quality("teeth") is not False:
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

        "My potent venom" if pd.get_quality("venom") is not False:
            if pd.get_revealed("venom"):
                "You manage to inject your venom into the investigator's veins."
                "The investigator, prepared for this, takes out a syringe and injects it into their neck."
                "With your venom neutralized the investigators are on you quickly. They cast an exorcism ritual which banishes you from the Earth"
                jump game_over
            else:
                "You manage to inject your venom into the investigator's veins."
                $pd.investigators_remaining -= 1
                "They start convulsing and foaming from the mouth. The rest first make motions to save their friend, but retreat to avoid meeting a similar fate."
                $pd.set_quality("venom", True)
                $pd.set_revealed("venom", True)
                jump scene_choosing

        "My massive pincer claws" if pd.get_quality("claws") is not False:
            if pd.get_revealed("claws"):
                "You attempt to grab an investigator between your claws."
                "The investigator is too quick and leaps out of the way, closing back in and holding your pincers closed."
                "The investigators attack, attaching thick belts around your claws."
                "With your claws stuck closed the investigators are on you quickly. They cast an exorcism ritual which banishes you from the Earth."
                jump game_over
            else:
                "You attempt to grab an investigator between your claws."
                $pd.investigators_remaining -= 1
                "Frozen with fear, the investigator stands no chance. You clamp around their neck and crush their windpipe."
                "Others make motions to help, but are quickly demoralized as your clamp harder and decapitate their friend."
                $pd.set_quality("claws", True)
                $pd.set_revealed("claws", True)
                jump scene_choosing

        "My electricity powers" if pd.get_quality("elec") is not False:
            if pd.get_revealed("elec"):
                "Using your naturally generated electricity, you send a charge through the floor."
                "The investigators are unharmed. Stunned you realize they have prepared themselves with rubber soled shoes."
                "In your ironic state of shock, the investigators are on you quickly. They cast an exorcism ritual which banishes you from the Earth."
                jump game_over
            else:
                "Using your naturally generated electricity, you send a charge through the floor."
                $pd.investigators_remaining -= 1
                "The lead investigator convulses in place as the others quickly back away."
                "Smoke rises from the investigator as their flesh burns. The others, repulsed by the smell, scatter."
                $pd.set_quality("elec", True)
                $pd.set_revealed("elec", True)
                jump scene_choosing

        "My corrosive acid" if pd.get_quality("acid") is not False:
            if pd.get_revealed("acid"):
                "You spray your acid on the unsuspecting investigator."
                "The investigator quickly reaches into their bag and spreads baking soda on the wound, neutralizing the acid."
                "With your acid unable to digest your prey, the investigators are on you quickly. They cast an exorcism ritual which banishes you from the Earth."
                jump game_over
            else:
                "You spray your acid on the unsuspecting investigator."
                $pd.investigators_remaining -= 1
                "The rest react in horror as their friend is dissolved into a pile of protein rich goo and quickly run away."
                $pd.set_quality("acid", True)
                $pd.set_revealed("acid", True)
                jump scene_choosing

        "My constricting tentacles" if pd.get_quality("tentacles") is not False:
            if pd.get_revealed("tentacles"):
                "You attack."
                "They kill you."
                jump game_over
            else:
                "You attack."
                $pd.investigators_remaining -= 1
                "he dies."
                $pd.set_quality("tentacles", True)
                $pd.set_revealed("tentacles", True)
                jump scene_choosing

        "My sharp spike" if pd.get_quality("spines") is not False:
            if pd.get_revealed("spines"):
                "You attack."
                "They kill you."
                jump game_over
            else:
                "You attack."
                $pd.investigators_remaining -= 1
                "he dies."
                $pd.set_quality("spines", True)
                $pd.set_revealed("spines", True)
                jump scene_choosing

        "On second thought. I'm just going to hide and watch them.":
            "The investigators complete their search and seems to find no trace of you."
            jump scene_choosing

label non_mythos_ending:
    "You are a [pd.animal]"
    return

label game_over:
    "You died"
    return

label winning:
    "You destroy the Earth"
    return

label mixed_ending:
    "The investigators are dead or run off, but you are just a [pd.animal], so the world survives."