from random import choice, randint
import requests

from .player_data import PlayerData


def scene_chooser(pd: PlayerData) -> str:
    pd.set_qualities_from_elimination()
    pd.calculate_mythos()
    if pd.the_hidden_name:
        name = pd.get_quality("name")
        investigators = pd.investigators_remaining
        pd.reset_qualities()
        pd.the_hidden_name = True
        pd.set_quality("name", name)
        pd.investigators_remaining = investigators

    if pd.investigators_remaining == pd.mythos == 0:
        return "mixed_ending"
    if pd.investigators_remaining == 0:
        return "win"
    if pd.mythos == 0:
        return "non_mythos_ending"

    remaining_unknowns = [q for q in pd.qualities if pd.qualities[q] is None]
    next_scene = choice(remaining_unknowns)
    pd.path.append(next_scene)
    return f"{next_scene}_selector"


def generate_runes(n: int) -> str:
    output = []
    i = 0
    while i < n:
        output.append(chr(choice([67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109])))
        i += 1
    return ",".join(output)
