+++
id = "ref/spell/litany-of-duty"
kind = "spell"
title = "Litany of Duty"
source_ids = ["disciples-doctrine"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "litany_of_duty", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["lawful"]
levels = [
  { class = "Inquisitor", level = 2 },
  { class = "Paladin", level = 1 },
]
casting_time = "1 immediate action"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Paladin\
2: Inquisitor
Casting time: 1 immediate action
Components: V, S, DF
Range: personal
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: you
Descriptors: lawful
:::

**Sources:** Disciple's Doctrine pg 13

You repeat a mantra or phrase that reminds you of your duty. You can immediately reroll a failed
saving throw against a spell that would force you to take an action against your will, and you gain
a +2 bonus against enchantment effects for 1 round. You can use this spell to reroll only a saving
throw that you failed within the past round. While subject to this spell, the target cannot be the
target of another spell that has the word "litany" in the title.
