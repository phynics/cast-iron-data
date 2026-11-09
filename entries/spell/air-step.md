+++
id = "ref/spell/air-step"
kind = "spell"
title = "Air Step"
aon = "SpellDisplay.aspx?ItemName=Air%20Step"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "air_step", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/air-walk" },
]
[[sources]]
publication = "advanced-class-guide"
page = "173"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["air"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a goose feather)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Alchemist, Arcanist, Bard, Cleric, Druid, Hunter, Investigator, Occultist, Oracle, Ranger, Red Mantis Assassin, Skald, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a goose feather)
Range: personal
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: you
Descriptors: air
:::

This spell functions as [air walk](ref/spell/air-walk), except you can rise no higher than 1 foot
off the ground, you cannot pass over liquid, and the air you walk on is less stable than solid
ground. When walking on air, you ignore difficult terrain that is less than 1 foot high, you do not
trigger effects based on weight (such as a pressure plate), and any creature trying to track you
through areas you crossed with this spell takes a -10 penalty on its Perception or Survival check to
do so. However, because of the instability of the air you walk on, your speed is reduced by 10 feet
(to a minimum of 5 feet) and you take a -4 penalty on Acrobatics, Climb, and Ride checks.

If you have 1 rank in Fly, your speed is not reduced when using this spell, and you can cross over
liquid at half speed. If you have 5 ranks in Fly, you can cross liquid at full speed and do not take
the penalties to your skill checks.
