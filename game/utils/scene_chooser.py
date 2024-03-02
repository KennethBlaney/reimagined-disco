from random import choice

from .player_data import PlayerData


def scene_chooser(pd: PlayerData) -> str:
    pd.set_qualities_from_elimination()
    pd.calculate_mythos()
    if pd.mythos == 0:
        return "ending"
    remaining_unknowns = [q for q in pd.qualities if pd.qualities[q] is None]
    return f"{choice(remaining_unknowns)}_selector"
