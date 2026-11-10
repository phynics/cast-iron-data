+++
id = "ref/spell/transfer-regeneration"
kind = "spell"
title = "Transfer Regeneration"
aon = "SpellDisplay.aspx?ItemName=Transfer%20Regeneration"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "transfer_regeneration", path = "json/spells10.json" },
]
[[sources]]
publication = "monster-codex"
page = "225"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "1 willing living creature" },
]
duration = "1 minute"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Cleric, Druid, Hunter, Oracle, Psychic, Shaman, Warpriest, Witch
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute
Saving throw: none
Spell resistance: no
Target: 1 willing living creature
:::

You bestow your regenerative abilities on the target. Your regeneration stops functioning for the
duration of the spell, and the target gains your regeneration. For example, if you have regeneration
5 (acid or fire), your target gains regeneration 5 (acid or fire). This regeneration overlaps (does
not stack) with any regeneration the creature already has, including other castings of this spell.
This spell has no effect if you don't have the regeneration ability or your regeneration isn't
functioning when you cast the spell.
