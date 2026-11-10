+++
id = "ref/feat/modification-trainer"
kind = "feat"
title = "Modification Trainer"
aon = "FeatDisplay.aspx?ItemName=Modification%20Trainer"
source_ids = ["adventurers-armory-2"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "modification_trainer", path = "json/feat11.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/armor-adept", label = "or" },
  { kind = "prerequisite", target = "ref/feat/weapon-adept", label = "or" },
]
[[sources]]
publication = "adventurers-armory-2"
page = "11"

[fields]
kind = "feat"
feat_types = ["Combat"]
prerequisites = "Cha 13, Armor Adept or Weapon Adept, fighter level 4th."
prerequisite_feats = ["ref/feat/armor-adept", "ref/feat/weapon-adept"]
benefit = "Choose a modification that you have selected with the Armor Adept or Weapon Adept feat. Once per day with 10 minutes of drilling, you can instruct a number of allies equal to your Charisma modifier in the use of that modification. The allies to be trained must have an Intelligence of at least 3. The instructed allies gain the benefit of Armor Adept or Weapon Adept with that modification for 8 hours."
+++

## Modification Trainer (Combat)

You can drill others in the use of modified weapons or armor.\
**Prerequisites:** Cha 13, [Armor Adept](ref/feat/armor-adept) or
[Weapon Adept](ref/feat/weapon-adept), fighter level 4th.\
**Benefit:** Choose a modification that you have selected with the Armor Adept or Weapon Adept feat.
Once per day with 10 minutes of drilling, you can instruct a number of allies equal to your Charisma
modifier in the use of that modification. The allies to be trained must have an Intelligence of at
least 3. The instructed allies gain the benefit of Armor Adept or Weapon Adept with that
modification for 8 hours.
