from copy import copy
import os
import hashlib
from dataclasses import dataclass
from pprint import pprint


@dataclass
class AnimalCandidate:
    name: str = "Animal"
    fins: bool = False
    gills: bool = False
    lungs: bool = False
    venom: bool = False
    shell: bool = False
    claws: bool = False
    elec: bool = False
    teeth: bool = False
    acid: bool = False
    tentacles: bool = False
    spines: bool = False
    sonar: bool = False

    def get_quality(self, quality):
        return self.__getattribute__(quality)

@dataclass
class PlayerData:
    mythos = 0
    investigators_remaining = 0
    animal = None
    qualities = {"name": None,
                 "fins": None,
                 "gills": None,
                 "lungs": None,
                 "venom": None,
                 "shell": None,
                 "claws": None,
                 "elec": None,
                 "teeth": None,
                 "acid": None,
                 "tentacles": None,
                 "spines": None,
                 "sonar": None,
                 }
    revealed = copy(qualities)

    start_candidates = [
        AnimalCandidate(**{"name": "anemone",
                           "venom": True,
                           }),
        AnimalCandidate(**{"name": "coral",
                           "venom": True,
                           "shell": True
                           }),
        AnimalCandidate(**{"name": "axolotl",
                           "gills": True,
                           "lungs": True
                           }),
        AnimalCandidate(**{"name": "vampire bat",
                           "sonar": True,
                           "lungs": True,
                           "teeth": True,
                           }),
        AnimalCandidate(**{"name": "bear",
                           "lungs": True,
                           "claws": True,
                           "teeth": True
                           }),
        AnimalCandidate(**{"name": "caecilian",
                           "lungs": True,
                           "tentacles": True,
                           "venom": True
                           }),
        AnimalCandidate(**{"name": "catfish",
                           "fins": True,
                           "gills": True,
                           "elec": True,
                           }),
        AnimalCandidate(**{"name": "clam",
                           "shell": True,
                           }),
        AnimalCandidate(**{"name": "crab",
                           "gills": True,
                           "shell": True,
                           "claws": True,
                           }),
        AnimalCandidate(**{"name": "cobra",
                           "lungs": True,
                           "venom": True,
                           "teeth": True,
                           "acid": True
                           }),
        AnimalCandidate(**{"name": "cuttlefish",
                           "fins": True,
                           "gills": True,
                           "venom": True,
                           "tentacles": True,
                           }),
        AnimalCandidate(**{"name": "dart frog",
                           "lungs": True,
                           "venom": True
                           }),
        AnimalCandidate(**{"name": "dolphin",
                           "fins": True,
                           "lungs": True,
                           "teeth": True,
                           "sonar": True,
                           }),
        AnimalCandidate(**{"name": "eel",
                           "fins": True,
                           "gills": True,
                           "elec": True,
                           "teeth": True
                           }),
        AnimalCandidate(**{"name": "fish",
                           "fins": True,
                           "gills": True,
                           }),
        AnimalCandidate(**{"name": "jellyfish",
                           "venom": True,
                           "acid": True,
                           "tentacles": True,
                           }),
        AnimalCandidate(**{"name": "lion fish",
                           "fins": True,
                           "gills": True,
                           "spines": True,
                           "venom": True
                           }),
        AnimalCandidate(**{"name": "lobster",
                           "fins": True,
                           "gills": True,
                           "shell": True,
                           "claws": True,
                           }),
        AnimalCandidate(**{"name": "lungfish",
                           "gills": True,
                           "lungs": True,
                           "fins": True,
                           }),
        AnimalCandidate(**{"name": "mollusk",
                           "shell": True,
                           "tentacles": True
                           }),
        AnimalCandidate(**{"name": "horned lizard",
                           "lungs": True,
                           "teeth": True,
                           "acid": True
                           }),
        AnimalCandidate(**{"name": "horseshoe crab",
                           "gills": True,
                           "shell": True,
                           "spines": True
                           }),
        AnimalCandidate(**{"name": "manatee",
                           "fins": True,
                           "lungs": True,
                           }),
        AnimalCandidate(**{"name": "mantis shrimp",
                           "fins": True,
                           "gills": True,
                           "shell": True,
                           "acid": True,
                           "claws": True
                           }),
        AnimalCandidate(**{"name": "octopus",
                           "gills": True,
                           "tentacles": True,
                           }),
        AnimalCandidate(**{"name": "platypus",
                           "fins": True,
                           "lungs": True,
                           "claws": True,
                           "spines": True,
                           "venom": True
                           }),
        AnimalCandidate(**{"name": "sand dollar",
                           "shell": True,
                           "spines": True
                           }),
        AnimalCandidate(**{"name": "sea cucumber",
                           "acid": True,
                           "tentacles": True,
                           }),
        AnimalCandidate(**{"name": "sea sponge"}),
        AnimalCandidate(**{"name": "sea snake",
                           "lungs": True,
                           "venom": True,
                           "teeth": True
                           }),
        AnimalCandidate(**{"name": "sea turtle",
                           "fins": True,
                           "lungs": True,
                           "shell": True,
                           }),
        AnimalCandidate(**{"name": "seal",
                           "fins": True,
                           "lungs": True,
                           "claws": True,
                           }),
        AnimalCandidate(**{"name": "shark",
                           "fins": True,
                           "gills": True,
                           "teeth": True,
                           }),
        AnimalCandidate(**{"name": "shrimp",
                           "fins": True,
                           "gills": True,
                           "shell": True,
                           }),
        AnimalCandidate(**{"name": "squid",
                           "gills": True,
                           "venom": True,
                           "tentacles": True,
                           }),
        AnimalCandidate(**{"name": "starfish",
                           "spines": True,
                           }),
        AnimalCandidate(**{"name": "stargazer fish",
                           "fins": True,
                           "gills": True,
                           "elec": True,
                           "spines": True,
                           "venom": True
                           }),
        AnimalCandidate(**{"name": "manta ray",
                           "fins": True,
                           "gills": True,
                           "spines": True,
                           }),
        AnimalCandidate(**{"name": "turtle",
                           "lungs": True,
                           "shell": True,
                           }),
        AnimalCandidate(**{"name": "urchin",
                           "venom": True,
                           "shell": True,
                           "spines": True,
                           }),
        AnimalCandidate(**{"name": "walrus",
                           "fins": True,
                           "lungs": True,
                           "teeth": True,
                           }),
        AnimalCandidate(**{"name": "whale",
                           "fins": True,
                           "lungs": True,
                           "sonar": True,
                           })
    ]

    candidates = []
    candidate_names = []
    path = []

    rocket_launcher = False
    the_hidden_name = False
    is_an_evil_clown = False
    name_hash = 0

    def set_quality(self, quality: str = None, val: [bool, str] = False) -> None:
        if not quality:
            return
        self.qualities[quality] = val
        if quality == "name":
            val = list(set(val))
            val.sort()
            val = "".join(val)
            self.name_hash = hashlib.sha1(val.encode()).hexdigest()

    def set_revealed(self, quality: str = None, val: bool = False) -> None:
        if not quality:
            return
        self.revealed[quality] = val

    def get_quality(self, quality: str = "name"):
        return self.qualities[quality]

    def get_revealed(self, quality: str = "name"):
        return self.revealed[quality]

    def reset_qualities(self):
        self.mythos = 100
        self.investigators_remaining = 4
        self.animal = None
        self.qualities = {"name": None,
                          "fins": None,
                          "gills": None,
                          "lungs": None,
                          "venom": None,
                          "shell": None,
                          "claws": None,
                          "elec": None,
                          "teeth": None,
                          "acid": None,
                          "tentacles": None,
                          "spines": None,
                          "sonar": None,
                          }
        self.revealed = copy(self.qualities)
        self.candidates = self.start_candidates[:]
        self.candidate_names = [item.get_quality('name') for item in self.candidates]
        self.path = []
        self.rocket_launcher = False
        self.the_hidden_name = False
        self.is_an_evil_clown = False
        self.name_hash = 0

    def calculate_mythos(self) -> None:
        self.mythos = len([q for q in self.qualities.values() if q is None])
        if self.the_hidden_name:
            self.mythos = 13

    def compare_to_candidates(self):
        for quality in self.qualities:
            if quality == "name":
                continue
            print(f"compare on {quality}")
            self.compare_to_candidates_by_quality(quality)

    def compare_to_candidates_by_quality(self, quality: str) -> None:
        output = []
        if self.qualities[quality] is None:
            return
        for candidate in self.candidates:
            if candidate.get_quality(quality) == self.qualities[quality]:
                output.append(candidate)
        self.candidates = output
        self.candidate_names = [item.get_quality('name') for item in self.candidates]
        if len(self.candidates) == 1:
            self.animal = self.candidates[0].get_quality("name")
        elif len(self.candidates) == 0:
            self.animal = "horror"

    def set_qualities_from_elimination(self):
        if len(self.candidates) == 0:
            self.animal = "horror"
            return
        for quality in self.qualities:
            target = self.candidates[0].get_quality(quality)
            # TODO: replace with All()
            eliminated = True
            for candidate in self.candidates:
                if candidate.get_quality(quality) != target:
                    eliminated = False
                    break
            if eliminated:
                self.qualities[quality] = target

    def test_validity_of_candidates(self):
        anon_candidates = []
        names = []
        for candidate in self.start_candidates[:]:
            names.append(candidate.name)
            candidate.name = "Animal"
            anon_candidates.append(candidate)
        for i, candidate in enumerate(anon_candidates):
            for j, candidate2 in enumerate(anon_candidates):
                if i >= j:
                    continue
                if candidate == candidate2:
                    print(f"Candidate collision on {names[i]} and {names[j]}")

    def count_features(self):
        qualities = {"fins": 0,
                     "gills": 0,
                     "lungs": 0,
                     "venom": 0,
                     "shell": 0,
                     "claws": 0,
                     "elec": 0,
                     "teeth": 0,
                     "acid": 0,
                     "tentacles": 0,
                     "spines": 0,
                     "sonar": 0,
                     }
        for candidate in self.start_candidates:
            for quality in qualities:
                if candidate.get_quality(quality):
                    qualities[quality] += 1
        pprint(f"Total animals: {len(self.start_candidates)}")
        pprint(qualities)

    def art_check(self):
        files = set(os.listdir(os.path.join("game", "images", "real_animals")))
        missing =[]
        for candidate in self.start_candidates:
            os.listdir(os.path.join("game", "images", "real_animals"))
            name = f"{candidate.get_quality("name")}.jpg".replace(" ", "_")
            if name not in files:
                missing.append(name)
        pprint(missing)
