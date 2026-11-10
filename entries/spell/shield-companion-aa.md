+++
id = "ref/spell/shield-companion-aa"
kind = "spell"
title = "Shield Companion (AA)"
aon = "SpellDisplay.aspx?ItemName=Shield%20Companion%20%28AA%29"
source_ids = ["core-rulebook", "animal-archive"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shield_companion_aa", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/shield-other" },
]
[[sources]]
publication = "animal-archive"
page = "25"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, F (a pair of platinum rings worth 50 gp worn by both you and the target)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 hour/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Cleric, Inquisitor, Oracle, Paladin, Psychic, Warpriest
Casting time: 1 standard action
Components: V, S, F (a pair of platinum rings worth 50 gp worn by both you and the target)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one creature
:::

### Shield Companion (AA)

This spell functions as [shield other](ref/spell/shield-other) but affects only the caster's animal
companion or familiar. Spellcasters from classes that do not normally gain an animal companion,
familiar, or fiendish servant but who gain one through an alternate class feature, archetype, or
prestige class can prepare and cast this spell as a 1st-level spell if they are capable of casting
spells.
