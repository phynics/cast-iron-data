+++
id = "ref/spell/absorb-rune-2"
kind = "spell"
title = "Absorb Rune II"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "absorb_rune_2", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/absorb-rune-1" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a white silk glove worth 25 gp)"
range = "touch"
effects = [
  { label = "Target", value = "one spell effect" },
]
duration = "instantaneous plus 1 minute/level (see text)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Arcanist, Bard, Cleric, Magus, Occultist, Oracle, Skald, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M (a white silk glove worth 25 gp)
Range: touch
Duration: instantaneous plus 1 minute/level (see text)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one spell effect
:::

### Absorb Rune II

**Sources:** Adventurer's Guide pg 60

This spell functions like [absorb rune I](ref/spell/absorb-rune-1), but it can affect runes
equivalent to a spell of 5th level or lower.
