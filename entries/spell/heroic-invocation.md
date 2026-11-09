+++
id = "ref/spell/heroic-invocation"
kind = "spell"
title = "Heroic Invocation"
aon = "SpellDisplay.aspx?ItemName=Heroic%20Invocation"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "heroic_invocation", path = "json/spells5.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "231"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Psychic", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Witch", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "10 minutes"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one or more creatures, no two of which can be more than 30 ft. apart" },
]
duration = "10 minutes /level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 9: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes /level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one or more creatures, no two of which can be more than 30 ft. apart
Subschool: Compulsion
Descriptors: mind-affecting
:::

Using worlds of ancient power, you bestow heroic powers on all creatures subject to this spell. They
gain a +4 morale bonus on attack and damage rolls, gain 2d8+4 temporary hit points, and become
immune to both fear and charm effects for the spell's duration.

At the end of the spell's duration, the subjects become fatigued.
