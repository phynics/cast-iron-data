+++
id = "ref/spell/martial-marionette"
kind = "spell"
title = "Martial Marionette"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "martial_marionette", path = "json/spells6.json" },
]
[[sources]]
publication = "inner-sea-magic"
page = "58"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 3 },
  { class = "Skald", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a marionette's crossbar)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "1 creature" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Bard, Skald
Casting time: 1 standard action
Components: V, S, M (a marionette's crossbar)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: 1 creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

When you cast this spell, you take partial control of an opponent's limbs, making it difficult for
him to attack you. Any attacks made against you by the target of the spell take a -2 penalty due to
the erratic and random motions the spell forces onto any efforts to strike you. In addition, any
creature suffering the effects of this spell cannot flank you and cannot aid other opponents in
flanking you.

As long as the affected creature is adjacent to you, you can cause the creature's limbs to flail
into the path of other attacks against you as an immediate action. This provides partial cover
against that attack, granting you a +2 bonus to AC and a +1 bonus on Reflex saves.
