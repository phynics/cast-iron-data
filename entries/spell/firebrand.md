+++
id = "ref/spell/firebrand"
kind = "spell"
title = "Firebrand"
aon = "SpellDisplay.aspx?ItemName=Firebrand"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "firebrand", path = "json/spells4.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "222"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["fire"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/4 levels, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Will negates (harmless), but see below"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 7: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates (harmless), but see below
Spell resistance: yes
Target: one creature/4 levels, no two of which can be more than 30 ft. apart
Descriptors: fire
:::

You mark several allies with a flaming rune. This rune does not cause damage, and sheds light as if
it were a torch. While the firebrand burns, any creature it marks is immune to damage from any fire
spell you cast. All of the target's weapons (both natural and manufactured) inflict +1d6 points of
fire damage on a hit (this bonus fire damage stacks with any amount of fire damage a creature's
weapons might already inflict). At any point during the spell's duration, a creature bearing a
firebrand can launch a beam of fire at any target within 30 feet as a swift action. This ray
requires a ranged touch attack to hit and deals 6d6 points of fire damage. Once a creature uses its
firebrand to fire a ray in this manner, the effects of the spell end for that creature.
