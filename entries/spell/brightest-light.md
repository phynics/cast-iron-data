+++
id = "ref/spell/brightest-light"
kind = "spell"
title = "Brightest Light"
source_ids = ["core-rulebook", "adventurers-guide", "inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "brightest_light", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/daylight" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["light"]
levels = [
  { class = "Adept", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "object touched" },
]
duration = "10 minutes/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Adept, Arcanist, Bard, Cleric, Druid, Hunter, Inquisitor, Magus, Occultist, Oracle, Paladin, Shaman, Skald, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 10 minutes/level (D)
Saving throw: none
Spell resistance: no
Target: object touched
Descriptors: light
:::

### Brightest Light

**Sources:** Adventurer's Guide pg 115, Inner Sea Intrigue pg 58

This trademark spell of the [Lantern Bearers](ref/rule/aff-lights) functions as
[daylight](ref/spell/daylight), except it lasts longer. In addition, as a swift action once during
the spell's duration, you can will the light to try to end a magical darkness effect located within
60 feet of the light this spell emits. Attempt a dispel check (1d20 + your caster level), with a DC
equal to 11 + the caster level of the darkness effect. If you succeed, the darkness effect ends.
Regardless of whether you are successful, the light from this spell dims to the brightness of a
torch for the spell's remaining duration.
