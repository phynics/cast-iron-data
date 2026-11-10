+++
id = "ref/spell/merge-with-familiar"
kind = "spell"
title = "Merge with Familiar"
aon = "SpellDisplay.aspx?ItemName=Merge%20with%20Familiar"
source_ids = ["ultimate-wilderness", "familiar-folio"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "merge_with_familiar", path = "json/spells14.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "231"
[[sources]]
publication = "familiar-folio"
page = "23"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "your familiar or spirit animal; see text" },
]
duration = "1 hour/level (D)"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 hour/level (D)
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: your familiar or spirit animal; see text
:::

As long as the target is at least one size category smaller than you are, it can merge harmlessly
into your body while under the effect of this spell. For the duration of this spell, you and the
target can separate or merge at will as a move action. While merged, your familiar or spirit animal
can't be targeted or affected by most attacks and effects, though it still suffers from ongoing
effects and their durations continue. It can be the recipient of effects that originate from you.
