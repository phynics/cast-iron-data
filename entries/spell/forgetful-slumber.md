+++
id = "ref/spell/forgetful-slumber"
kind = "spell"
title = "Forgetful Slumber"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "forgetful_slumber", path = "json/spells13.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/deep-slumber" },
]
[[sources]]
publication = "advanced-race-guide"
page = "48"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 round"
components = "V, S, M (a few drops of river water)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 minute/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Arcanist, Bard, Mesmerist, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 1 round
Components: V, S, M (a few drops of river water)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Will negates
Spell resistance: yes
Target: one living creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

> _[Half-elves](ref/race/half-elf) have access to the following spell._

This spell acts as the [deep slumber](ref/spell/deep-slumber) spell, but only affects one creature
of 10 Hit Dice or fewer. In addition, a creature affected by this spell awakens with no knowledge of
the events that led to the spell's casting. The target loses all memory from the 5 minutes prior to
falling asleep. No effect short of a miracle or wish can restore memories lost by this spell.
