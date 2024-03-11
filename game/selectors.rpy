label fins_selector:
    "The investigators have you surrounded, but they don't know it yet. Your only hope is to escape or to hide."
    menu:
        "What do you do to survive?"

        "Use my powerful fins to escape.":
            $pd.set_quality("fins", True)
            "You flip your fins and manage to swim past one of the investigators."
            "The puny human is stunned by your appearance and you easily escape."
            jump scene_choosing

        "Hide in the shadows and hope they pass you by.":
            $pd.set_quality("fins", False)
            "Hidden in the shadows the investigators don't even know you are there."
            "You hear them converge and talk to each other for a bit before leaving together."
            "You are safe for now."
            jump scene_choosing

        "Hide in the shadows and ambush them.":
            "You hide in the shadows and take your opportunity"
            jump fight_the_investigators
    return

label lungs_selector:
    "The investigators believe that you might succumb to poisonous gas released into your lair."
    menu:
        "What do you do to survive the poison?"

        "Take a deep breath. I have impressive lung capacity":
            $pd.set_quality("lungs", True)
            "You take a deep breath in before the poison gets to you."
            "In a mere half hour, the heavy poison gas settles to the ground. You survive the investigators weak attempt on your life."

        "I don't breathe air, so the gas won't affect me.":
            $pd.set_quality("lungs", False)
            "The gas floods into your chamber but you sit motionless."
            "The investigators will have to try harder than that to kill you."

    jump scene_choosing
    return

label gills_selector:
    "The investigators have piled up some dynamite in your temple."
    menu:
        "What do you do to survive the explosion?"

        "Jump into a pool of water. The water will absorb the heat and pressure.":
            $pd.set_quality("gills", True)
            "You leap into a nearby pool breathing the water through your gills."
            "The explosion is unable to effect the deep pool leaving you unharmed."

        "Run from the explosion and hide behind a sturdy structure in the temple.":
            $pd.set_quality("gills", False)
            "The explosion echos through your temple, but the labrynthian hallways absorb the expanding gas's heat and pressure."
            "You survive the explosion, but your temple is a mess."

    jump scene_choosing
    return

label venom_selector:
    "A cultist calls out to you. By his garb, he appears to be a leader in your cult."
    "He says, \"Oh wise and powerful [pd.get_quality('name')]. Grant me some venom from your most terrifying maw so that we may worship you better.\""
    menu:
        "Can you manifest some venom for this pitiful mortal and his rituals dedicated to you?"

        "Yes":
            $pd.set_quality("venom", True)
            "You gape open your mouth as the cultist cautiously approaches."
            "The cultist reaches in and extracts a small bottle of venom to bring back."
            "He seems elated at the opportunity to share this relic with the cult."

        "Yes, but only for the purpose of eating him":
            $pd.set_quality("venom", True)
            "You gape open your mouth as the cultist cautiously approaches."
            "As the cultist reaches for a venom sac to fill a small bottle, you lunge forward and devour him."
            "The cultist yelps in surprise, but then in ecstasy"
            "\"My life to help nourish the dark lord. Thank you [pd.get_quality('name')]!\""

        "No":
            $pd.set_quality("teeth", False)
            "The cult leader bows. Dejected, but understanding."
            "He leaves empty handed, but seemingly happy for the opportunity to have met you."

    jump scene_choosing
    return

label shell_selector:
    "Look out! The investigators have ambushed you and they've brought automatic weapons."
    menu:
        "They try to spray you with bullets. What do you do?"

        "Nothing. I have a thick shell and their bullets don't scare me.":
            $pd.set_quality("shell", True)
            "The investigators open fire against you, but the bullets plink harmlessly off your thick shell."

        "I'm nimble and flexible enough to avoid their bullets.":
            $pd.set_quality("shell", False)
            "As the bullets rip through the air, you lithe form drifts around them easily."

    menu:
        "The investigators are stunned their attack doesn't work. Do you seize the opportunity to attack?"

        "Yes. Make them regret attacking you.":
            jump fight_the_investigators
        "No. Staying alive is more important.":
            "They say 'Discretion is the better part of valor' and you know now is not the time to attack."
            jump scene_choosing

    return

label claws_selector:
    "The investigators are looking around your home, but they've made the fatal mistake of not looking up."
    menu:
        "This is the opportunity to pounce on one of them."

        "Grab an investigator with your claws." if pd.get_quality("claws") is not False:
            if pd.get_revealed("claws"):
                "You attempt to grab an investigator between your claws."
                "The investigator is too quick and leaps out of the way, closing back in and holding your pincers together."
                "The investigators attack, attaching thick belts around your claws."
                "With your claws stuck closed the investigators are on you quickly. They cast an exorcism ritual which banishes you from the Earth."
                jump game_over
            else:
                "You attempt to grab an investigator with your claws."
                $pd.investigators_remaining -= 1
                "Frozen with fear, the investigator stands no chance. You clamp around their neck and crush their windpipe."
                "Others make motions to help, but are quickly demoralized as you pull and rip their friend in two."
                $pd.set_quality("claws", True)
                $pd.set_revealed("claws", True)
                jump scene_choosing

        "Drip some corrosive acid on them from above" if pd.get_quality("acid") is not False:
            if pd.get_revealed("acid"):
                "You drip your acid on the unsuspecting investigator."
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

        "I don't think I can kill them safely.":
            if pd.get_quality('claws') is None:
                $pd.set_quality("claws", False)
            if pd.get_quality('acid') is None:
                $pd.set_quality("acid", False)
            "You remain hidden and the investigators pass you by."
            jump scene_choosing

        "Attack some other way.":
            jump fight_the_investigators

    jump scene_choosing
    return

label elec_selector:

    "A group of cultists approach you asking you for a display of your might. They request a gift of power."
    menu:
        "They dare? Electrocute them ironically.":
            "Using your naturally generated electricity, you send a charge through the floor."
            "The cultists convulse in place. Their convulsing seems to become a sort of ritualistic dance to pay you tribute."
            $pd.set_quality("elec", True)
            jump scene_choosing

        "Refuse. It is wrong of them to ask as you don't control electricity.":
            "Apologetically, your cultists back away believing they have some how offended you."
            $pd.set_quality("elec", False)
            jump scene_choosing

    jump scene_choosing
    return

label teeth_selector:

    "A cultist calls out to you. By his garb, he appears to be a leader in your cult."
    "He says, \"Oh wise and powerful [pd.get_quality('name')]. Grant me a tooth from your most terrifying maw so that we may worship you better.\""
    menu:
        "Do you have a tooth to spare for this pitiful mortal?"

        "Yes":
            $pd.set_quality("teeth", True)
            "You gape open your mouth as the cultist cautiously approaches."
            "The cultist reaches in and extracts a vicious looking tooth to bring back."
            "He seems elated at the opportunity to share this relic with the cult."

        "Yes, but only for the purpose of eating him":
            $pd.set_quality("teeth", True)
            "You gape open your mouth as the cultist cautiously approaches."
            "As the cultist reaches for a tooth, you lunge forward and devour him."
            "The cultist yelps in surprise, but then in ecstasy"
            "\"My life to help nourish the dark lord. Thank you [pd.get_quality('name')]!\""

        "No":
            $pd.set_quality("teeth", False)
            "The cult leader bows. Dejected, but understanding."
            "He leaves empty handed, but seemingly happy for the opportunity to have met you."

    jump scene_choosing
    return

label acid_selector:
    jump claws_selector
    return

label tentacles_selector:
    "You sense that the investigators are in the next room over which is connected by a thin, underwater cave."
    "Will you use your tentacles to reach through the cave and drag away one of the investigators?"
    menu:
        "Do you even have tentacles?"

        "Yes, kill one of the investigators":
            $pd.set_quality("tentacles", True)
            $pd.set_revealed("tentacles", True)
            "You reach through the cavern and wrap around one of the investigators legs."
            "As you drag the investigator to the cave, you meet some resistance as the others try to save their friend."
            "However, it is of no use. You are too strong for them and rip your victim from their hands."
            $pd.investigators_remaining -= 1
            jump scene_choosing

        "Yes, but I don't want to reveal that to the investigators yet":
            $pd.set_quality("tentacles", True)

        "No, I don't":
            $pd.set_quality("tentacles", False)

    "The investigators poke around the other room noticing the cave, but appear to decide that they can't fit."
    "Soon enough, they move on."
    jump scene_choosing
    return

label spines_selector:
    "You feel the investigators walking in the room above you. Unbeknownst to them, you are hiding in the muddy floor below."
    "A surprise attack with a sharp spikey part of your body could impale an investigator easily."
    menu:
        "Attack with a spike?"

        "Yes, kill one of the investigators":
            $pd.set_quality("spines", True)
            $pd.set_revealed("spines", True)
            "You sense the foot falls of an investigator and time your spike perfectly to jut though their foot."
            "The investigator falls to the ground writhing in pain giving you the opportunity to impale them a second time through the torso."
            "The other investigators shriek in fright and scatter into other rooms of the temple."
            $pd.investigators_remaining -= 1
            jump scene_choosing

        "No, keep my spikes a secret for now.":
            $pd.set_quality("spines", True)

        "No. I don't have any spikes like that.":
            $pd.set_quality("spines", False)

    "Clearly feeling uncomfortable walking on the mud of this room, the investigators quickly move through to elsewhere in the temple."
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