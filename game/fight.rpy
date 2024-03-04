

label fight_the_investigators:
    scene monster_attack
    $ pd.compare_to_candidates()
    $ pd.set_qualities_from_elimination()
    $ pd.calculate_mythos()

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

        "My massive, sharp claws" if pd.get_quality("claws") is not False:
            "You attempt to grab an investigator between your claws."
            if pd.get_revealed("claws"):
                "The investigator is too quick and leaps out of the way, closing back in and holding your pincers together."
                "The investigators attack, attaching thick belts around your claws."
                "With your claws stuck closed the investigators are on you quickly. They cast an exorcism ritual which banishes you from the Earth."
                jump game_over
            else:
                $pd.investigators_remaining -= 1
                "Frozen with fear, the investigator stands no chance. You clamp around their neck and crush their windpipe."
                "Others make motions to help, but are quickly demoralized as you pull and rip their friend in two."
                $pd.set_quality("claws", True)
                $pd.set_revealed("claws", True)
                jump scene_choosing

        "My electricity powers" if pd.get_quality("elec") is not False:
            "Using your naturally generated electricity, you send a charge through the floor."
            if pd.get_revealed("elec"):
                "The investigators are unharmed. Stunned you realize they have prepared themselves with rubber soled shoes."
                "In your ironic state of shock, the investigators are on you quickly. They cast an exorcism ritual which banishes you from the Earth."
                jump game_over
            else:
                "The lead investigator convulses in place as the others quickly back away."
                "Smoke rises from the investigator as their flesh burns. The others, repulsed by the smell, scatter."
                $pd.investigators_remaining -= 1
                $pd.set_quality("elec", True)
                $pd.set_revealed("elec", True)
                jump scene_choosing

        "My corrosive acid" if pd.get_quality("acid") is not False:
            "You spray your acid on the unsuspecting investigator."
            if pd.get_revealed("acid"):
                "The investigator quickly reaches into their bag and spreads baking soda on the wound, neutralizing the acid."
                "With your acid unable to digest your prey, the investigators are on you quickly. They cast an exorcism ritual which banishes you from the Earth."
                jump game_over
            else:
                $pd.investigators_remaining -= 1
                "The rest react in horror as their friend is dissolved into a pile of protein rich goo and quickly run away."
                $pd.set_quality("acid", True)
                $pd.set_revealed("acid", True)
                jump scene_choosing

        "My constricting tentacles" if pd.get_quality("tentacles") is not False:
            "You reach down from above and attempt to grab one of the investigators by their neck with your tentacle."
            if pd.get_revealed("tentacles"):
                "The investigator appears to have been aware of the possibility and quickly ducks out of your grasp, calling out to the others."
                "The investigators quickly surround you in your place on the ceiling. They cast an exorcism ritual which banishes you from the Earth."
                jump game_over
            else:
                "As you wrap around their neck you pull upwards, lifting the investigator off their feet."
                "The investigator struggles making a gurgling sound followed by a snap."
                "Their lifeless body slumps to the floor as you drop them."
                "The other investigators scramble to escape your grasp."
                $pd.investigators_remaining -= 1
                $pd.set_quality("tentacles", True)
                $pd.set_revealed("tentacles", True)
                jump scene_choosing

        "My sharp spike" if pd.get_quality("spines") is not False:
            "You sense the foot falls of an investigator and time your spike perfectly to jut though their foot."
            if pd.get_revealed("spines"):
                "It was a trap!"
                "The investigator was wearing stilts and you've only managed to puncture one of those."
                "Stuck in the investigator's stilt slows you down while the rest of their team quickly sets up a ritual."
                "Performing the exorcism, they successfully banish you from the Earth."
                jump game_over
            else:

                "The investigator falls to the ground writhing in pain giving you the opportunity to impale them a second time through the torso."
                "The other investigators shriek in fright and scatter into other rooms of the temple."
                $pd.investigators_remaining -= 1
                $pd.set_quality("spines", True)
                $pd.set_revealed("spines", True)
                jump scene_choosing

        "On second thought. I'm just going to hide and watch them.":
            "The investigators complete their search and seems to find no trace of you."
            jump scene_choosing
