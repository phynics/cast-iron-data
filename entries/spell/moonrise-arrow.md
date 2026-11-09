+++
id = "ref/spell/moonrise-arrow"
kind = "spell"
title = "Moonrise Arrow"
source_ids = ["pathfinder-134-it-came-from-hollow-mountain"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "moonrise_arrow", path = "json/spells7.json" },
]
[[sources]]
publication = "pathfinder-134-it-came-from-hollow-mountain"
page = "72"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["light"]
levels = [
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "up to 50 pieces of ammunition, all of which must be together at the time of casting" },
]
duration = "10 minutes/level"
saving_throw = "Fortitude negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Cleric, Inquisitor, Magus, Occultist, Oracle, Paladin, Warpriest
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 10 minutes/level
Saving throw: Fortitude negates (object)
Spell resistance: yes (object)
Target: up to 50 pieces of ammunition, all of which must be together at the time of casting
Descriptors: light
:::

You cause ammunition, including shuriken, to glow with faint silvery light. The ammunition counts as
magic and silver for the purpose of overcoming [damage reduction](ref/rule/damage-reduction), in
addition to the properties of any other special material the ammunition has. Incorporeal undead and
shapechangers take an additional 1d8 points of damage from such ammunition. The targeted ammunition
sheds dim light in a 5-foot radius for 1 round after it is fired or thrown.
