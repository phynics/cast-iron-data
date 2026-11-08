+++
id = "ref/spell/vitriolic-mist"
kind = "spell"
title = "Vitriolic Mist"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vitriolic_mist", path = "json/spells11.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/fire-shield" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["acid"]
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of lemon rind)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Alchemist, Arcanist, Bloodrager, Investigator, Sorcerer, Summoner, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of lemon rind)
Range: personal
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Target: you
Descriptors: acid
:::

**Sources:** Ultimate Magic pg 248

This functions as [fire shield](ref/spell/fire-shield), except it wreathes you in yellow or green
acidic mist instead of hot or cold flames. The spell deals acid damage to attackers and protects you
against acid damage. This spell does not shed light.
