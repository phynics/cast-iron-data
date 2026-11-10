+++
id = "ref/spell/intellect-fortress-3"
kind = "spell"
title = "Intellect Fortress III"
aon = "SpellDisplay.aspx?ItemName=Intellect%20Fortress%20III"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "intellect_fortress_3", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/intellect-fortress-2" },
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

### Intellect Fortress III

This spell functions as [intellect fortress II](ref/spell/intellect-fortress-2), but creatures
within the area who succeed at a saving throw against a fear or emotion effect suffer no effects,
even if there is usually a partial effect on a successful saving throw. This spell can be undercast.
