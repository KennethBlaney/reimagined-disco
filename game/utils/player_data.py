from dataclasses import dataclass


@dataclass
class PlayerData:
    mythos = 0
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

    shark = {"name": "shark",
             "fins": True,
             "gills": True,
             "lungs": False,
             "venom": False,
             "shell": False,
             "claws": False,
             "elec": False,
             "teeth": True,
             "acid": False,
             "tentacles": False,
             "spines": False,
             "sonar": False,
             }

    octopus = {"name": "octopus",
               "fins": False,
               "gills": True,
               "lungs": False,
               "venom": False,
               "shell": False,
               "claws": False,
               "elec": False,
               "teeth": False,
               "acid": False,
               "tentacles": True,
               "spines": False,
               "sonar": False,
               }

    squid = {"name": "squid",
             "fins": False,
             "gills": True,
             "lungs": False,
             "venom": True,
             "shell": False,
             "claws": False,
             "elec": False,
             "teeth": False,
             "acid": False,
             "tentacles": True,
             "spines": False,
             "sonar": False,
             }

    cuttlefish = {"name": "cuttlefish",
                  "fins": True,
                  "gills": True,
                  "lungs": False,
                  "venom": True,
                  "shell": False,
                  "claws": False,
                  "elec": False,
                  "teeth": False,
                  "acid": False,
                  "tentacles": True,
                  "spines": False,
                  "sonar": False,
                  }

    jellyfish = {"name": "jellyfish",
                 "fins": False,
                 "gills": False,
                 "lungs": False,
                 "venom": True,
                 "shell": False,
                 "claws": False,
                 "elec": False,
                 "teeth": False,
                 "acid": True,
                 "tentacles": True,
                 "spines": False,
                 "sonar": False,
                 }

    fish = {"name": "fish",
            "fins": True,
            "gills": True,
            "lungs": False,
            "venom": False,
            "shell": False,
            "claws": False,
            "elec": False,
            "teeth": False,
            "acid": False,
            "tentacles": False,
            "spines": False,
            "sonar": False,
            }

    urchin = {"name": "urchin",
              "fins": False,
              "gills": False,
              "lungs": False,
              "venom": True,
              "shell": True,
              "claws": False,
              "elec": False,
              "teeth": False,
              "acid": False,
              "tentacles": False,
              "spines": True,
              "sonar": False,
              }

    starfish = {"name": "starfish",
                "fins": False,
                "gills": False,
                "lungs": False,
                "venom": False,
                "shell": True,
                "claws": False,
                "elec": False,
                "teeth": False,
                "acid": False,
                "tentacles": False,
                "spines": True,
                "sonar": False,
                }

    dolphin = {"name": "dolphin",
               "fins": True,
               "gills": False,
               "lungs": True,
               "venom": False,
               "shell": False,
               "claws": False,
               "elec": False,
               "teeth": True,
               "acid": False,
               "tentacles": False,
               "spines": False,
               "sonar": True,
               }

    whale = {"name": "whale",
             "fins": True,
             "gills": False,
             "lungs": True,
             "venom": False,
             "shell": False,
             "claws": False,
             "elec": False,
             "teeth": False,
             "acid": False,
             "tentacles": False,
             "spines": False,
             "sonar": True,
             }

    clam = {"name": "clam",
            "fins": False,
            "gills": False,
            "lungs": False,
            "venom": False,
            "shell": True,
            "claws": False,
            "elec": False,
            "teeth": False,
            "acid": False,
            "tentacles": False,
            "spines": False,
            "sonar": False,
            }

    seal = {"name": "seal",
            "fins": True,
            "gills": False,
            "lungs": True,
            "venom": False,
            "shell": False,
            "claws": True,
            "elec": False,
            "teeth": False,
            "acid": False,
            "tentacles": False,
            "spines": False,
            "sonar": False,
            }

    manatee = {"name": "manatee",
               "fins": True,
               "gills": False,
               "lungs": True,
               "venom": False,
               "shell": False,
               "claws": False,
               "elec": False,
               "teeth": False,
               "acid": False,
               "tentacles": False,
               "spines": False,
               "sonar": False,
               }

    walrus = {"name": "walrus",
              "fins": True,
              "gills": False,
              "lungs": True,
              "venom": False,
              "shell": False,
              "claws": False,
              "elec": False,
              "teeth": True,
              "acid": False,
              "tentacles": False,
              "spines": False,
              "sonar": False,
              }

    shrimp = {"name": "shrimp",
              "fins": True,
              "gills": True,
              "lungs": False,
              "venom": False,
              "shell": True,
              "claws": False,
              "elec": False,
              "teeth": False,
              "acid": False,
              "tentacles": False,
              "spines": False,
              "sonar": False,
              }

    crab = {"name": "crab",
            "fins": False,
            "gills": True,
            "lungs": False,
            "venom": False,
            "shell": True,
            "claws": True,
            "elec": False,
            "teeth": False,
            "acid": False,
            "tentacles": False,
            "spines": False,
            "sonar": False,
            }

    lobster = {"name": "walrus",
               "fins": True,
               "gills": True,
               "lungs": False,
               "venom": False,
               "shell": True,
               "claws": True,
               "elec": False,
               "teeth": False,
               "acid": False,
               "tentacles": False,
               "spines": False,
               "sonar": False,
               }

    turtle = {"name": "turtle",
              "fins": False,
              "gills": False,
              "lungs": True,
              "venom": False,
              "shell": True,
              "claws": False,
              "elec": False,
              "teeth": False,
              "acid": False,
              "tentacles": False,
              "spines": False,
              "sonar": False,
              }

    sea_turtle = {"name": "sea turtle",
                  "fins": True,
                  "gills": False,
                  "lungs": True,
                  "venom": False,
                  "shell": True,
                  "claws": False,
                  "elec": False,
                  "teeth": False,
                  "acid": False,
                  "tentacles": False,
                  "spines": False,
                  "sonar": False,
                  }

    eel = {"name": "eel",
           "fins": True,
           "gills": True,
           "lungs": False,
           "venom": False,
           "shell": False,
           "claws": False,
           "elec": True,
           "teeth": False,
           "acid": False,
           "tentacles": False,
           "spines": False,
           "sonar": False,
           }

    sea_cucumber = {"name": "sea cucumber",
                    "fins": False,
                    "gills": False,
                    "lungs": False,
                    "venom": False,
                    "shell": False,
                    "claws": False,
                    "elec": False,
                    "teeth": False,
                    "acid": True,
                    "tentacles": True,
                    "spines": False,
                    "sonar": False,
                    }

    sting_ray = {"name": "sting ray",
                 "fins": True,
                 "gills": True,
                 "lungs": False,
                 "venom": True,
                 "shell": False,
                 "claws": False,
                 "elec": False,
                 "teeth": False,
                 "acid": False,
                 "tentacles": False,
                 "spines": True,
                 "sonar": False,
                 }

    sea_sponge = {"name": "sea sponge",
                  "fins": False,
                  "gills": False,
                  "lungs": False,
                  "venom": False,
                  "shell": False,
                  "claws": False,
                  "elec": False,
                  "teeth": False,
                  "acid": False,
                  "tentacles": False,
                  "spines": False,
                  "sonar": False,
                  }

    start_candidates = [clam, crab, cuttlefish, dolphin, eel, fish, jellyfish, lobster, manatee, octopus,
                        sea_cucumber, sea_sponge, sea_turtle, seal, shark, shrimp, squid, starfish, sting_ray, turtle,
                        urchin, walrus, whale]

    jellyfish, sea_cucumber

    candidates = start_candidates
    candidate_names = [item['name'] for item in candidates]

    def set_quality(self, quality: str = None, val: bool = False) -> None:
        if not quality:
            return
        self.qualities[quality] = val

    def get_quality(self, quality: str = "name"):
        return self.qualities[quality]

    def reset_qualities(self):
        self.mythos = 100
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
        self.candidates = self.start_candidates
        self.candidate_names = [item['name'] for item in self.candidates]

    def calculate_mythos(self) -> None:
        self.mythos = len([q for q in self.qualities.values() if q is None])

    def compare_to_candidates(self):
        for quality in self.qualities:
            if quality == "name":
                continue
            print(f"compare on {quality}")
            self.compare_to_candidates_by_quality(quality)

    def compare_to_candidates_by_quality(self, quality: str) -> None:
        output = []
        if self.qualities[quality] is None:
            print("Bouncing out.")
            return
        for candidate in self.candidates:
            if candidate[quality] == self.qualities[quality]:
                print(
                    f"\tAdding {candidate['name']} because {candidate[quality]} == {self.qualities[quality]} on {quality}")
                output.append(candidate)
            else:
                print(f"\tEliminating {candidate['name']} on {quality}")
        self.candidates = output
        self.candidate_names = [item['name'] for item in self.candidates]
        if len(self.candidates) == 1:
            self.animal = self.candidates[0].get("name", "error")
        elif len(self.candidates) == 0:
            self.animal = "horror"

    def set_qualities_from_elimination(self):
        if len(self.candidates) == 0:
            self.animal = "horror"
            return
        for quality in self.qualities:
            target = self.candidates[0][quality]
            # TODO: replace with All()
            eliminated = True
            for candidate in self.candidates:
                if candidate[quality] != target:
                    eliminated = False
                    break
            if eliminated:
                self.qualities[quality] = target

    def test_validity_of_candidates(self):
        anon_candidates = []
        for candidate in self.candidates:
            del candidate['name']
            anon_candidates.append(candidate)
        for i, candidate in enumerate(anon_candidates):
            for j, candidate2 in enumerate(anon_candidates):
                if i == j:
                    continue
                if candidate == candidate2:
                    print(f"Candidate collision on {i} and {j}")
