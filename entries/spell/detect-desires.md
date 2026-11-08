+++
id = "ref/spell/detect-desires"
kind = "spell"
title = "Detect Desires"
source_ids = ["core-rulebook", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "detect_desires", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/detect-thoughts" },
]

[fields]
kind = "spell"
school = "divination"
descriptors = ["mind-affecting"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, F/DF (a copper piece)"
range = "60 ft."
effects = [
  { label = "Area", value = "cone-shaped emanation" },
]
duration = "concentration, up to 1 min./level (D)"
saving_throw = "Will negates; see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Psychic\
2: Alchemist, Arcanist, Bard, Inquisitor, Investigator, Medium, Mesmerist, Skald, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F/DF (a copper piece)
Range: 60 ft.
Duration: concentration, up to 1 min./level (D)
Saving throw: Will negates; see text
Spell resistance: no
Area: cone-shaped emanation
Descriptors: mind-affecting
:::

### Detect Desires

**Sources:** Ultimate Intrigue pg 211

This spell functions as per [detect thoughts](ref/spell/detect-thoughts), except you sense
significant desires of creatures with an Intelligence score of 1 or higher, regardless of whether
they are conscious or not.

Instead of Intelligence, the second round of concentration reveals each mind's Charisma score. If
the highest Charisma score is 26 or higher (and at least 10 points higher than your own Charisma
score), you are stunned for 1 round and the spell ends. Instead of surface thoughts, the third round
of concentration reveals the most pressing current desire of any mind in the area (Will negates).

Presenting a creature with an opportunity to fulfill a significant desire grants you a +2
circumstance bonus (or higher, at the GM's discretion) on Diplomacy checks to influence it.
