+++
id = "ref/spell/mind-thrust-1"
kind = "spell"
title = "Mind Thrust I"
aon = "SpellDisplay.aspx?ItemName=Mind%20Thrust%20I"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mind_thrust_1", path = "json/spells14.json" },
]
[[sources]]
publication = "occult-adventures"
page = "177"

[fields]
kind = "spell"
school = "divination"
descriptors = ["mind-affecting"]
levels = [
  { class = "Psychic", level = 1 },
]
casting_time = "1 standard action"
components = "S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous"
saving_throw = "Will half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Psychic
Casting time: 1 standard action
Components: S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will half
Spell resistance: yes
Target: one creature
Descriptors: mind-affecting
:::

You divine the most vulnerable portions of your opponent's mind and overload it with a glut of
psychic information. This attack deals 1d6 points of damage per caster level (maximum 5d6). The
target receives a Will save for half damage. This attack has no effect on creatures without an
Intelligence score.
