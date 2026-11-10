+++
id = "ref/spell/emergency-force-sphere"
kind = "spell"
title = "Emergency Force Sphere"
aon = "SpellDisplay.aspx?ItemName=Emergency%20Force%20Sphere"
source_ids = ["cheliax-empire-of-devils"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "emergency_force_sphere", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/wall-of-force" },
]
[[sources]]
publication = "cheliax-empire-of-devils"
page = "23"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 immediate action"
components = "V"
range = "5 ft."
effects = [
  { label = "Effect", value = "5-ft.-radius hemisphere of force centered on you" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Arcanist, Sorcerer, Wizard
Casting time: 1 immediate action
Components: V
Range: 5 ft.
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Effect: 5-ft.-radius hemisphere of force centered on you
Descriptors: force
:::

As [wall of force](ref/spell/wall-of-force), except you create a hemispherical dome of force with
[hardness](ref/umr/hardness) 20 and a number of hit points equal to 10 per caster level. The bottom
edge of the dome forms a relatively watertight space if you are standing on a reasonably flat
surface. The dome shape means that falling debris (such as rocks from a collapsing ceiling) tend to
tumble to the side and pile up around the base of the dome. If you make a DC 20 Craft
(stonemasonry), Knowledge (engineering), or Profession (architect or engineer) check, the debris is
stable enough that it retains its dome-like configuration when the spell ends, otherwise it
collapses. Normally this spell is used to buy time for dealing with avalanches, floods, and
rockslides, though it is also handy in dealing with ambushes.
