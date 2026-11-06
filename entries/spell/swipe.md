+++
id = "ref/spell/swipe"
kind = "spell"
title = "Swipe"
source_ids = ["rise-of-the-runelords-anniversary-edition", "pathfinder-5-sins-of-the-saviors"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "swipe", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one held item" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Bard, Skald\
3: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: one held item
Subschool: Teleportation
:::

**Sources:** Rise of the Runelords Anniversary Edition pg 419, Pathfinder \#5: Sins of the Saviors
pg 62

By flicking a finger in the appropriate direction and proclaiming ownership, you attempt to
magically wrest an item from the target's grip and summon it to your hand. To claim an object held
by an opponent, you must make a CMB check-this check has a bonus equal to your caster level + your
Intelligence, Wisdom, or Charisma modifier (whichever is highest). If you fail this check, the
target retains the item and the spell fails. If you succeed, the item teleports into one of your
free hands or comes to rest at your feet.
