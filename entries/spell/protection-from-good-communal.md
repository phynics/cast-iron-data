+++
id = "ref/spell/protection-from-good-communal"
kind = "spell"
title = "Communal Protection from Good"
source_ids = ["core-rulebook", "mythic-adventures", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "protection_from_good_communal", path = "json/spells15.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/protection-from-good" },
]

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["good"]
levels = [
  { class = "Adept", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M/DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "no; see text"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Adept, Arcanist, Bloodrager, Cleric, Inquisitor, Medium, Oracle, Paladin, Shaman, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF
Range: touch
Duration: 1 minute/level (D)
Saving throw: Will negates (harmless)
Spell resistance: no; see text
Target: creature touched
Descriptors: good
:::

### Mythic Protection from Evil

**Sources:** Mythic Adventures pg 105

The bonuses to AC and on saves increase to +4. Any evil creature attempting to possess or exercise
mental control over the target must attempt a Will save against this spell. If it fails, the
creature takes 1d6 points of damage per 2 caster levels (maximum 5d6) from mental feedback. An evil
creature that uses [spell resistance](ref/rule/spell-resistance) to bypass the spell's protection
against contact must successfully save or take this damage once each round it attacks the protected
target.

### Mythic Protection from Chaos

**Sources:** Mythic Adventures pg 104

As mythic protection from evil, except against chaotic creatures.

### Mythic Protection from Good

**Sources:** Mythic Adventures pg 105

As _mythic protection from evil,_ except against good creatures.

### Communal Protection from Good

**Sources:** Ultimate Combat pg 240

This spell functions like _[protection from good](ref/spell/protection-from-good),_ except you
divide the duration in 1-minute intervals among the creatures touched.

### Mythic Protection from Law

**Sources:** Mythic Adventures pg 105

As _mythic protection from evil,_ except against lawful creatures.
