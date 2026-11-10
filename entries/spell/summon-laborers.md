+++
id = "ref/spell/summon-laborers"
kind = "spell"
title = "Summon Laborers"
source_ids = ["monster-summoners-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summon_laborers", path = "json/spells16.json" },
]
[[sources]]
publication = "monster-summoners-handbook"
page = "23"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Cleric", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Shaman", level = 6 },
  { class = "Summoner", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
]
casting_time = "10 minutes"
components = "V, S, F/DF (a strip of rune-inscribed parchment)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one summoned petitioner/caster level" },
]
duration = "8 hours (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 6: Cleric, Oracle, Shaman, Summoner, Warpriest, Witch
Casting time: 10 minutes
Components: V, S, F/DF (a strip of rune-inscribed parchment)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 8 hours (D)
Saving throw: none
Spell resistance: no
Effect: one summoned petitioner/caster level
Subschool: Summoning
:::

Summon laborers summons one humanoid petitioner per caster level. These petitioners hail from one
plane of your choice and perform tasks at your direction. The petitioners cannot fight or travel to
dangerous lands, but do assist your downtime activities within a settlement, increasing the effect
of Influence or Labor you spend by 50%, to a maximum of 1 additional point of Influence or Labor for
every 2 caster levels you possess. This stacks with any increase to the effect of Influence or Labor
that you receive from your followers within the settlement where the downtime activity takes place
(if any). Summon laborers is a spell of the same alignment type as the plane from which the summoned
petitioners hail (chaotic and evil for the Abyss, lawful and good for Heaven, and so on). Effects
that increase the number of creatures summoned by a spell (such as Superior Summoning) do not affect
summon laborers.
