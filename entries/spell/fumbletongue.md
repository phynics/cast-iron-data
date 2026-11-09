+++
id = "ref/spell/fumbletongue"
kind = "spell"
title = "Fumbletongue"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fumbletongue", path = "json/spells13.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "221"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Witch", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1d4 rounds"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Bard, Mesmerist, Psychic, Skald, Witch
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1d4 rounds
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

This enchantment causes a creature to be unable to speak intelligibly. Any effort the target makes
to talk, in any language, comes out as a useless mix of unconnected words and noises. Even magic
words are affected to some extent; the target has a 20% spell failure chance for any spell it
attempts to cast with verbal components, and a 20% chance to incorrectly use a command word to
activate a magic item. This spell has no effect on telepathic communication, or the vocalizations of
creatures that lack a spoken language.
