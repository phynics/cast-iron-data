+++
id = "ref/spell/fey-gate"
kind = "spell"
title = "Fey Gate"
aon = "SpellDisplay.aspx?ItemName=Fey%20Gate"
source_ids = ["core-rulebook", "ultimate-wilderness", "the-first-world-realm-of-the-fey"]
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
subschools = ["Creation", "Calling"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Cleric", level = 9 },
  { class = "Oracle", level = 9 },
  { class = "Psychic", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V, S, M (see text)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "see text" },
]
duration = "instantaneous or concentration (up to 1 round/level); see text"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 9: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (see text)
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous or concentration (up to 1 round/level); see text
Saving throw: none
Spell resistance: no
Effect: see text
Subschool: Creation, Calling
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
