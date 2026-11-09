+++
id = "ref/spell/locate-gate"
kind = "spell"
title = "Locate Gate"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "locate_gate", path = "json/spells6.json" },
]
[[sources]]
publication = "horror-adventures"
page = "121"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Occultist", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, F/DF (a small lodestone sphere)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Area", value = "circle centered on you with a radius of 400 ft. + 40 ft./level" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 5: Arcanist, Bard, Cleric, Occultist, Oracle, Psychic, Skald, Sorcerer, Summoner, Unchained Summoner, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, F/DF (a small lodestone sphere)
Range: long (400 ft. + 40 ft./level)
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Area: circle centered on you with a radius of 400 ft. + 40 ft./level
:::

You sense the direction of the nearest teleportation circle (permanent or with a remaining
duration), gate spell, or other effect which magically connects two different locations (for
example, an active magic item, a creature's special ability, or unique adventure location). Locate
gate detects only spells or effects with a permanent or ongoing duration, not instantaneous effects
like dimension door or teleport.

Locate gate can be blocked by spells like nondetection, if the effect originates from a specific
object or creature. However, spell effects can't likewise be warded. For example, ring gates are a
specific object, but a permanent teleportation circle is not (the surface in which it's inscribed
doesn't count). Locate gate isn't blocked by lead, water, or other physical environmental
conditions, but it is blocked by any intervening area that is dimensionally warded (such as by
dimensional lock or forbiddance).
