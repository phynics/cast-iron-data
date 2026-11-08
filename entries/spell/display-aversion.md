+++
id = "ref/spell/display-aversion"
kind = "spell"
title = "Display Aversion"
source_ids = ["blood-of-the-night"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "display_aversion", path = "json/spells13.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/minor-image" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a drop of holy water)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Effect", value = "visual figment that cannot extend beyond four 10-ft. cubes + one 10-ft. cube/level (S)" },
]
duration = "concentration+ 1d4 rounds"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 2: Bard, Cleric, Inquisitor, Oracle, Skald, Warpriest, Witch\
3: Arcanist, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a drop of holy water)
Range: long (400 ft. + 40 ft./level)
Duration: concentration+ 1d4 rounds
Saving throw: none
Spell resistance: no
Effect: visual figment that cannot extend beyond four 10-ft. cubes + one 10-ft. cube/level (S)
Subschool: Shadow
:::

**Sources:** Blood of the Night pg 30

This spell functions like [minor image](ref/spell/minor-image), except it always creates an animated
illusion of you presenting to a vampire a material, object, or sound that it is averse to, such as
garlic, a holy symbol, or bells ringing. You specify what aversion the illusion depicts when you
cast the spell. The vampire reacts to the illusion as if it were real; it can overcome the effect by
succeeding at a disbelief save or a normal Will save against the illusion's DC (instead of the
normal DC 25 to overcome its revulsion). The illusion is only quasi-real and cannot otherwise affect
creatures.
