+++
id = "ref/spell/shield-the-banner"
kind = "spell"
title = "Shield the Banner"
source_ids = ["orcs-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shield_the_banner", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/sanctuary" },
]
[[sources]]
publication = "orcs-of-golarion"
page = "29"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Adept", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "object touched" },
]
duration = "1 minute/level"
saving_throw = "Will negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Adept, Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 minute/level
Saving throw: Will negates
Spell resistance: no
Target: object touched
:::

This spell is used to protect one of a tribe's most valuable possessions: its tribal banner. Any
creature (other than a member of the tribe which the standard represents) attempting to directly
attack or touch the standard must make a Will save. This spell functions as
[sanctuary](ref/spell/sanctuary), but only protects a standard or banner. In addition, the spell
grants a +2 bonus to the standard's [hardness](ref/umr/hardness), and +10 to the standard's hit
points for the duration of the spell.
