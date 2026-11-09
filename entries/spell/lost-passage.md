+++
id = "ref/spell/lost-passage"
kind = "spell"
title = "Lost Passage"
aon = "SpellDisplay.aspx?ItemName=Lost%20Passage"
source_ids = ["inner-sea-races"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lost_passage", path = "json/spells6.json" },
]
[[sources]]
publication = "inner-sea-races"
page = "220"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Area", value = "one 30-ft. cube/level (S)" },
]
duration = "2 hours/level (D)"
saving_throw = "Will partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Arcanist, Bard, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: long (400 ft. + 40 ft./level)
Duration: 2 hours/level (D)
Saving throw: Will partial
Spell resistance: yes
Area: one 30-ft. cube/level (S)
Subschool: Compulsion
Descriptors: mind-affecting
:::

> _The following spells are available to the indicated race or ethnicity:
> [Samsaran](ref/race/samsaran)_

Creatures in the area of this spell are subject to a subtle enchantment that confounds their senses
of direction, interferes with recognizing landmarks, and causes them to misjudge distances and
angles. Creatures that enter the area must succeed at a new Survival check to avoid becoming lost
immediately, whether or not they succeed at their saving throws. Those that fail the save take a
penalty on such Survival checks equal to double your caster level, treat all squares they enter as
difficult terrain for as long as they are in the area and for 1 hour per caster level thereafter,
lose the benefit of all effects that allow them to ignore difficult terrain, and take a -4 penalty
to Dexterity.

Lost passage can be made permanent with [permanency](ref/spell/permanency) at a cost of 10,000 gp.
