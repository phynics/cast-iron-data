+++
id = "ref/spell/oppressive-boredom"
kind = "spell"
title = "Oppressive Boredom"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "oppressive_boredom", path = "json/spells7.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "230"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level or until broken (see text)"
saving_throw = "Will negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Arcanist, Bard, Medium, Mesmerist, Psychic, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level or until broken (see text)
Saving throw: Will negates (see text)
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

You fill your target with boredom. The target loses all interest in its current task and must make a
Will save against the spell's effect in order to perform its next action. If the target fails, it
takes no action that round. The boredom lasts until the duration expires or the target breaks the
spell's effect with a successful Will save.
