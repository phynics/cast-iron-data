+++
id = "ref/spell/crushing-hand"
kind = "spell"
title = "Crushing Hand"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "crushing_hand", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/interposing-hand" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Psychic", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V, S, F (a soft glove)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "10-ft.-hand" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 9: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F (a soft glove)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: yes
Effect: 10-ft.-hand
Descriptors: force
:::

**Sources:** PRPG Core Rulebook pg 262

This spell functions as [interposing hand](ref/spell/interposing-hand), except that it can also
grapple one opponent as grasping hand. Its CMB and CMD for grapple checks use your caster level in
place of its base attack bonus, with a +12 bonus for its Strength score (35) and a +1 bonus for
being Large (its Dexterity is 10, granting no bonus to the CMD). A crushing hand deals 2d6+12 points
of damage on each successful grapple check against an opponent. The crushing hand can instead be
directed to bull rush a target (as forceful hand), using the same bonuses outlined above, or it can
be directed to interpose itself, as interposing hand does.
