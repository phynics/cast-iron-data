+++
id = "ref/spell/summon-totem-creature"
kind = "spell"
title = "Summon Totem Creature"
source_ids = ["humans-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summon_totem_creature", path = "json/spells16.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/summon-natures-ally-3" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "10 minutes"
components = "V, S, M/DF (a piece of bone from any one of your totem animals)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one summoned creature" },
]
duration = "1 hour (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Arcanist, Cleric, Druid, Hunter, Oracle, Ranger, Sorcerer, Summoner, Unchained Summoner, Warpriest, Wizard
Casting time: 10 minutes
Components: V, S, M/DF (a piece of bone from any one of your totem animals)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour (D)
Saving throw: none
Spell resistance: no
Effect: one summoned creature
Subschool: Summoning
:::

**Sources:** Humans of Golarion pg 29

The Shoanti revere more than the deities of distant planes, but also the animals and natural forces
of the rugged lands they call home. Shoanti spellcasters have learned ways to call upon the might of
their quahs' totem creatures in times of need. A character must have been raised by the Shoanti and
be considered part of a quah to be able to cast this spell. Characters with access to this spell can
only summon creatures revered by the quah they are a part of, as noted on the following lists.
Except as noted above, this spell functions as
[summon nature's ally III](ref/spell/summon-natures-ally-3).

_Lyrune-Quah (Moon Clan):_ air elemental (small), 1d3 bats, wolf, 1d3 owls.

_Shadde-Quah (Axe Clan):_ 1d3 eagles, earth elemental (small), water elemental (small).

_Shriikirri-Quah (Hawk Clan):_ air elemental (small), 1d3+1 hawks (familiars), horse.

_Shundar-Quah (Spire Clan):_ air elemental (small), earth elemental (small), 1d3 eagles.

_Sklar-Quah (Sun Clan):_ 1d3 fire beetles, fire elemental (small), horse.

_Skoan-Quah (Skull Clan):_ 1d3+1 eagles (vultures), 1d3 fire beetles, 1d3 giant centipedes.

_Tamiir-Quah (Wind Clan):_ air elemental (small), 1d3 eagles, earth elemental (small).
