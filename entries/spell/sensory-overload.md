+++
id = "ref/spell/sensory-overload"
kind = "spell"
title = "Sensory Overload"
aon = "SpellDisplay.aspx?ItemName=Sensory%20Overload"
source_ids = ["psychic-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sensory_overload", path = "json/spells15.json" },
]
[[sources]]
publication = "psychic-anthology"
page = "11"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "1 creature" },
]
duration = "1 round/level"
saving_throw = "Will negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates (see text)
Spell resistance: yes
Target: 1 creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

You overload the target creature's senses, making it difficult for the target to concentrate. For
the duration of the effect, the target must succeed at a Will save at the same DC as the original
effect to perform any standard or full-round action. On a failure, the creature loses the action
that triggered the saving throw. If successful, the creature is able to take the action, but this
spell effect is not negated.
