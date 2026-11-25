+++
id = "ref/spell/fey-gate"
kind = "spell"
title = "Fey Gate"
aon = "SpellDisplay.aspx?ItemName=Fey%20Gate"
source_ids = ["ultimate-wilderness", "the-first-world-realm-of-the-fey"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fey_gate", path = "json/spells13.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/gate" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "230"
[[sources]]
publication = "the-first-world-realm-of-the-fey"
page = "12"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["creation"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Bard", level = 6 },
  { class = "Cleric", level = 8 },
  { class = "Druid", level = 8 },
  { class = "Oracle", level = 8 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 8 },
  { class = "Summoner", level = 6 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
duration = "1 round/level; see text"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 6: Bard, Skald, Summoner, Unchained Summoner\
8: Arcanist, Cleric, Druid, Oracle, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level; see text
Saving throw: none
Spell resistance: no
Subschool: creation
:::

### Fey Gate

This spell functions as [the planar travel function of gate](ref/spell/gate), except it can be used
to travel only between points on the Material Plane and the First World, and it comes with
additional dangers.

This spell forms a circular portal between 5 and 20 feet in diameter (your choice) oriented in the
direction you desire when it comes into being (typically vertical and facing you). The portal is
full of gray fog that blocks line of sight. Anyone or anything that moves through the portal to
enter the First World is shunted instantly to a random point on that plane (the same point for
everything traveling via a particular casting). At the end of the spell's duration, the caster can
attempt a DC 30 Spellcraft check. On a success, the portal remains open for 1d4+1 days. Creatures
exiting the First World through a fey gate always arrive at the location the spell was cast.

While the spell always deposits travelers on solid ground in the First World, it conveys no
protections against whatever creatures or environmental hazards may be present there.
