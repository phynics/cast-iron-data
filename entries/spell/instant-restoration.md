+++
id = "ref/spell/instant-restoration"
kind = "spell"
title = "Instant Restoration"
aon = "SpellDisplay.aspx?ItemName=Instant%20Restoration"
source_ids = ["monster-summoners-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "instant_restoration", path = "json/spells14.json" },
]
[[sources]]
publication = "monster-summoners-handbook"
page = "22"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Summoner", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
]
casting_time = "1 immediate action"
components = "V, S, F/DF (a thimble of water and a seed)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one summoned creature you control" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Cleric, Druid, Hunter, Oracle, Shaman, Summoner, Warpriest, Witch
Casting time: 1 immediate action
Components: V, S, F/DF (a thimble of water and a seed)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Target: one summoned creature you control
Subschool: Healing
:::

Instant restoration channels planar energy into a summoned creature. This spell can be cast as an
immediate action when a summoned creature you control drops to 0 or fewer hit points. Rather than
immediately disappear, the creature is healed for 4d8 hp + 1 hit point per caster level (maximum
4d8+10 hit points). If this healing brings your summoned creature's hit point total to 1 or more hit
points, it remains as if its hit points had never dropped to 0 or fewer. Creatures slain by death
effects cannot be saved by instant restoration. A summoner can target his eidolon with this spell.
