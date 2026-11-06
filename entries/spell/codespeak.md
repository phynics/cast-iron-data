+++
id = "ref/spell/codespeak"
kind = "spell"
title = "Codespeak"
source_ids = ["ultimate-intrigue", "second-darkness-players-guide", "black-markets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "codespeak", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a complex rune inscribed on a slip of paper that is then placed under your tongue)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "you plus one willing creature per 2 levels, no two of which can be more than 30 ft. apart" },
]
duration = "10 minutes/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Bard, Medium, Mesmerist, Occultist, Psychic, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a complex rune inscribed on a slip of paper that is then placed under your tongue)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes/level (D)
Saving throw: none
Spell resistance: no
Target: you plus one willing creature per 2 levels, no two of which can be more than 30 ft. apart
:::

**Sources:** Ultimate Intrigue pg 206, Second Darkness Player's Guide pg 26, Black Markets pg 24

Upon casting this spell, all recipients gain the ability to speak a new language. This language
sounds like random, babbling syllables to anyone not under the influence of the spell, but the
targets understand each other perfectly.

Anyone using codespeak can read and write in this new language as well. Once the spell expires,
however, any coded writing suddenly appears as gibberish. If the exact same group of individuals
become the targets of a codespeak spell again, cast by the same caster, they can once again read any
coded writings. A dedicated codebreaker can crack such writing's code, deciphering it one page at a
time with a series of DC 30 Linguistics checks.

Comprehend languages doesn't enable a caster to understand the language of another's codespeak
spell, but it does reveal that the targets are speaking a magical language. Tongues translates
codespeak normally.
