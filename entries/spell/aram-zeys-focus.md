+++
id = "ref/spell/aram-zeys-focus"
kind = "spell"
title = "Aram Zey's Focus"
source_ids = ["pathfinder-society-field-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aram_zeys_focus", path = "json/spells.json" },
]
[[sources]]
publication = "pathfinder-society-field-guide"
page = "56"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, F (masterwork thieves' tools worth 100 gp)"
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
School: divination
Level: 2: Alchemist, Arcanist, Bard, Investigator, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F (masterwork thieves' tools worth 100 gp)
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
:::

Aram Zey created this spell for use by his students, both to increase their confidence in their
skills and to ensure more of them survived encounters with deadly traps. If you don't have the
trapfinding class ability, this spell grants you the trapfinding ability of a rogue of half your
character level. If you have the trapfinding ability granted by class levels, however, this spell
grants you a +5 competence bonus on all Disable Device checks made to disarm mechanical (but not
magical) traps. While under the effects of Aram Zey's focus, whenever you trigger a trap by rolling
poorly on a Disable Device check, you may roll a second Disable Device check. This new roll uses the
same modifiers as the first roll. If your second roll is high enough to avoid accidentally springing
the trap, you avoid setting it off, but still fail to disarm it. Each time you take advantage of
this feature, the remaining duration of the spell is reduced by 1 minute - if less than a minute's
worth of duration remains, the spell ends as soon as you reroll your Disable Device check.
