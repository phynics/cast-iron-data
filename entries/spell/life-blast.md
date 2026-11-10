+++
id = "ref/spell/life-blast"
kind = "spell"
title = "Life Blast"
aon = "SpellDisplay.aspx?ItemName=Life%20Blast"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "life_blast", path = "json/spells6.json" },
]
[[sources]]
publication = "horror-adventures"
page = "121"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Shaman", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a dead leaf)"
range = "150 ft."
effects = [
  { label = "Area", value = "150 ft. line" },
]
duration = "instantaneous"
saving_throw = "Will half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Hunter, Ranger\
4: Druid, Shaman
Casting time: 1 standard action
Components: V, S, M (a dead leaf)
Range: 150 ft.
Duration: instantaneous
Saving throw: Will half
Spell resistance: yes
Area: 150 ft. line
:::

This spell must be cast in an area with vegetation or it has no effect. When you cast this spell,
you draw the life force from the surrounding land and hurl it at your enemies, dealing 1d6 points of
positive energy damage per caster level (to a maximum of 12d6 at 12th level) to any undead creatures
in the spell's area. However, doing so blights the land around you in a spread with a radius of 5
feet per caster level you have (to a maximum of 60 feet at 12th level). All vegetation in that area
immediately withers and dies. Plant creatures aren't affected.

The blast starts from your palm and is able to travel through solid objects and obstacles.
