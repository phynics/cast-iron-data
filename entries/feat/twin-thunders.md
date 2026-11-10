+++
id = "ref/feat/twin-thunders"
kind = "feat"
title = "Twin Thunders"
aon = "FeatDisplay.aspx?ItemName=Twin%20Thunders"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "twin_thunders", path = "json/feat16.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/two-weapon-fighting", label = "or" },
]
[[sources]]
publication = "ultimate-combat"
page = "123"

[fields]
kind = "feat"
feat_types = ["Combat"]
prerequisites = "Dwarf or gnome, defensive training racial trait, Two-Weapon Fighting or flurry of blows class feature, Weapon Focus with both wielded weapons."
prerequisite_feats = ["ref/feat/two-weapon-fighting", "ref/feat/weapon-focus"]
benefit = "Once per round, when wielding a bludgeoning weapon in each hand against a creature with the giant subtype, if you hit the creature with your off-hand weapon after you hit with your primary weapon, roll the damage dice for your off-hand weapon twice and add the results together before adding any bonuses. Such extra weapon damage dice are not multiplied on a critical hit."
+++

## Twin Thunders (Combat)

When you fight giants, your powerful blows combine with skills learned from generations of your
people to quickly even the odds.\
**Prerequisites:** [Dwarf](ref/race/dwarf) or [gnome](ref/race/gnome), defensive training racial
trait, [Two-Weapon Fighting](ref/feat/two-weapon-fighting) or flurry of blows class feature,
[Weapon Focus](ref/feat/weapon-focus) with both wielded weapons.\
**Benefit:** Once per round, when wielding a bludgeoning weapon in each hand against a creature with
the giant subtype, if you hit the creature with your off-hand weapon after you hit with your primary
weapon, roll the damage dice for your off-hand weapon twice and add the results together before
adding any bonuses. Such extra weapon damage dice are not multiplied on a critical hit.
