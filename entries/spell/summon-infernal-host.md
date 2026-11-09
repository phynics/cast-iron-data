+++
id = "ref/spell/summon-infernal-host"
kind = "spell"
title = "Summon Infernal Host"
aon = "SpellDisplay.aspx?ItemName=Summon%20Infernal%20Host"
source_ids = ["rival-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summon_infernal_host", path = "json/spells16.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/summon-monster-5" },
]
[[sources]]
publication = "rival-guide"
page = "59"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
descriptors = ["evil", "lawful"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 round"
components = "V, S, F/DF (strip of rune-inscribed parchment)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "1d4+1 lesser host devils or 1 greater host devil" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Arcanist, Bard, Cleric, Oracle, Skald, Sorcerer, Summoner, Unchained Summoner, Warpriest, Witch, Wizard
Casting time: 1 round
Components: V, S, F/DF (strip of rune-inscribed parchment)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Effect: 1d4+1 lesser host devils or 1 greater host devil
Subschool: Summoning
Descriptors: evil, lawful
:::

This spell functions as [summon monster V](ref/spell/summon-monster-5), save that it can only be
used to summon host devils, noxious flying devils, known also as
[gaavs](ref/monster/devil-host-devil-lesser-gaav) and
[magaavs](ref/monster/devil-host-devil-greater-magaav).
