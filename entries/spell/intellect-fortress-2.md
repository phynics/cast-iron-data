+++
id = "ref/spell/intellect-fortress-2"
kind = "spell"
title = "Intellect Fortress II"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "intellect_fortress_2", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/intellect-fortress-1" },
]
[[sources]]
publication = "occult-adventures"
page = "175"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Psychic", level = 4 },
]
casting_time = "1 immediate action"
components = "V"
range = "20 ft."
effects = [
  { label = "Area", value = "20-ft.-radius emanation centered on you" },
]
duration = "1 round"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Psychic
Casting time: 1 immediate action
Components: V
Range: 20 ft.
Duration: 1 round
Saving throw: none
Spell resistance: yes
Area: 20-ft.-radius emanation centered on you
:::

### Intellect Fortress II

This spell functions as [intellect fortress I](ref/spell/intellect-fortress-1), but in addition, any
mind-affecting effects that deal damage have their damage reduced by half (before any reduction due
to a successful save or other effect). This applies to both hit point damage and ability score
damage. This spell can be undercast.
