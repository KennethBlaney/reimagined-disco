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
    window auto hide
    show stars with fade:
        subpixel True
        matrixtransform ScaleMatrix(1.2, 1.2, 1.0)*OffsetMatrix(100.0, -100.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
        linear 15.00 matrixtransform ScaleMatrix(1.4, 1.4, 1.0)*OffsetMatrix(-100.0, 100.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
    with Pause(1.50)
    window auto show
    "You are an unknown, mysterious, alien entity on this world."
    "Your motives are understood only by yourself. They cannot be understood by mere mortal men."

    # Establish cult and creature name
    window auto hide
    scene cult_ritual with slow_fade:
        subpixel True
        matrixtransform ScaleMatrix(1.2, 1.2, 1.0)*OffsetMatrix(150.0, 20.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
        linear 30.00 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-100.0, -20.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
    with Pause(1.10)
    window auto show
    "Not even the cultists who wish to pay you tribute can comprehend the vastness of your intellect."
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
    "[pd.get_quality('name')], guard your mythos power and don't let yourself be defined by anything."

    # Set up danger
    scene investigators with slow_fade
    "Unfortunately, there is a group of investigators who will stop at nothing to learn your secrets, discover your weaknesses and remove you from this world."
    "Protect yourself from them so that you may rise from your palace under the waves and dominate the Earth."
    jump scene_choosing
    return


label show_game_status_screen:
    screen game_status:
            text "mythos power: [pd.mythos]\ninvestigators: [pd.investigators_remaining]" xalign 0.02 yalign 0.02
    show screen game_status
    return


label scene_choosing:
    $ pd.compare_to_candidates()
    $ pd.set_qualities_from_elimination()
    $ pd.calculate_mythos()
    scene temple_interior with fade
    call show_game_status_screen

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
    $animal = pd.animal.replace(" ", "_")
    show expression animal with fade:
        pos (0.5, 0.5) anchor (0.5, 0.5)
    "As you look down at your form, you realize the decisions you've made about yourself have transformed you into... an ordinary [pd.animal]."
    $killed = 4-pd.investigators_remaining
    if killed == 0:
        return
    jump reward_runes
    return

label game_over:
    scene stars
    "Banished from Earth, you float aimlessly in the black space between the stars."
    "Try as you might, you are unable to push or pull yourself in any direction."
    "Perhaps one day, your orbit will bring you close enough to Earth so you may have your revenge."
    if killed == 0:
        return
    jump reward_runes
    return

label reward_runes:
    "However, all is not lost."
    $runes = generate_runes(killed)
    if killed == 1:
        "You killed [killed] investigators and so have earned [killed] rune of the true name of the Great Old One."
        "The Great Old One's name includes the rune: [runes]"
    else:
        "You killed [killed] investigators and so have earned [killed] runes of the true name of the Great Old One."
        "The Great Old One's name includes the runes: [runes]"
    return


label mixed_ending:
    "As the last investigator dies at your hands, you feel tired."
    "Your mythos power is gone."
    "As you look at your form, you realize you are merely.{w}.. an ordinary [pd.animal], and no longer the eldritch monster you once were."
    "However, all is not lost."
    "For killing all of the investigators you have earned 5 runes in the true name of the Great Old One."
    $runes = generate_runes(5)
    "The Great Old One's name includes the runes: [runes]"
    return

label win:
    if pd.is_an_evil_clown:
        "You laugh manically and honk your large clown nose."
    "As the last investigator dies, so does Earth's last hope."
    "Now, no one can stop you, oh Great Old One [pd.get_quality('name')] from your dark and unknowable plan."
    "Your cult gathers around you."
    "Now is the time of your ascension!"

    if pd.rocket_launcher:
        "Circling the corpses of the investigators around you, the cultists one by one remove their masks."
        "Each of them, secretly one of the Octopus Chairment of Fishsanto, the evil genetic engineering company that has been poisoning the oceans."
        "If four of them are here, then there is only one left."
        "Jetting off into the water, you set course for the Southern Ocean."
        ""
        "Thank you for playing 'Arise Oh Elder God' and probably 'Sharktillary' as well.{w}\nThe End."
        return

    menu:
        "What is your plan for the world?"

        "Dominate the world":
            "These tiny humans stand no chance against you."
            "With a show of force and power, world leaders are soon begging for your mercy."
            "You grant it to them.{w}.. so long as they promise you devotion and servitude."
            "The Earth is yours."

        "Bring peace via alien technology":
            "Your gathered cult suddenly understands your divine plan."
            "Schematics for beneficial devices appear, fully formed in their heads."
            "New scientific and mathematical insights become child's play to them."
            "Each cultist becomes a captain of industry or an award winning academic within the decade."
            "Earth enjoys a new golden age of productivity and leisure."
            "And it is all thanks to you."

        "Ascend into space. Earth is insignificant.":
            "Earth isn't your home planet, or even significant to your larger goals."
            "It was merely your prison for the last thousand years."
            "Now you have escaped and the rest of the universe doesn't know what it coming for it."

        "Destroy everything":
            "Earth isn't your home planet, or even significant to your larger goals."
            "It was merely your prison for the last thousand years."
            "Now that you have escaped, you ensure that you will never be imprisioned in such a place ever again."
            "You channel your power into the core of the Earth... this pitiful ball of wet dirt in a vast expanse of space."
            "Existing on Earth is hellish for but a moment as the planet splits apart."
            "Humans are extinct in a flash.{w}.. but on a cosmic scale, it is as if nothing happened at all."

    "Thank you for playing 'Arise Oh Elder God'.{w}\nThe End."
    return