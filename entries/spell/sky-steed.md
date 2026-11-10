+++
id = "ref/spell/sky-steed"
kind = "spell"
title = "Sky Steed"
aon = "SpellDisplay.aspx?ItemName=Sky%20Steed"
source_ids = ["ultimate-wilderness", "animal-archive"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sky_steed", path = "json/spells9.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "235"
[[sources]]
publication = "animal-archive"
page = "25"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Paladin", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "a creature you are mounted upon" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Paladin
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 minute/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: a creature you are mounted upon
Subschool: Polymorph
:::

The target sprouts angelic wings and gains a fly speed equal to its base speed with average
maneuverability. It also gains a bonus on Fly checks equal to your caster level.
