+++
id = "ref/spell/ki-leech"
kind = "spell"
title = "Ki Leech"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ki_leech", path = "json/spells6.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "225"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
Descriptors: evil
:::

You place your spirit in a receptive state so when you confirm a critical hit against a living enemy
or reduce a living enemy to 0 or fewer hit points, you can steal some of that creature's ki. This
replenishes 1 point of ki as long as you have at least 1 ki point in your ki pool. This does not
allow you to exceed your ki pool's maximum. This ability does not stack with similar abilities (such
as the steal ki ability of the hungry ghost monk).

This spell has no effect if you do not have a ki pool.
