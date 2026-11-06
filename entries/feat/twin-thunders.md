+++
id = "ref/feat/twin-thunders"
kind = "feat"
title = "Twin Thunders"
source_ids = ["ultimate-combat", "pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "twin_thunders", path = "json/feat16.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/two-weapon-fighting", label = "or" },
]

[fields]
kind = "feat"
feat_types = ["Combat"]
prerequisites = "Dwarf or gnome, defensive training racial trait, Two-Weapon Fighting or flurry of blows class feature, Weapon Focus with both wielded weapons."
prerequisite_feats = ["ref/feat/two-weapon-fighting", "ref/feat/weapon-focus"]
benefit = "Once per round, when wielding a bludgeoning weapon in each hand against a creature with the giant subtype, if you hit the creature with your off-hand weapon after you hit with your primary weapon, roll the damage dice for your off-hand weapon twice and add the results together before adding any bonuses. Such extra weapon damage dice are not multiplied on a critical hit."
+++

## Twin Thunders (Combat)

**Sources:** Ultimate Combat pg 123

When you fight giants, your powerful blows combine with skills learned from generations of your
people to quickly even the odds.\
**Prerequisites:** [Dwarf](ref/race/dwarf) or [gnome](ref/race/gnome), defensive training racial
trait, [Two-Weapon Fighting](ref/feat/two-weapon-fighting) or flurry of blows class feature,
[Weapon Focus](ref/feat/weapon-focus) with both wielded weapons.\
**Benefit:** Once per round, when wielding a bludgeoning weapon in each hand against a creature with
the giant subtype, if you hit the creature with your off-hand weapon after you hit with your primary
weapon, roll the damage dice for your off-hand weapon twice and add the results together before
adding any bonuses. Such extra weapon damage dice are not multiplied on a critical hit.

### Stamina

**Sources:** Pathfinder Unchained pg 134\
You can spend 2 stamina points to gain the benefits of this feat against a creature at least one
size category larger than you that does not have the giant subtype. You gain this benefit until the
start of your next turn.
