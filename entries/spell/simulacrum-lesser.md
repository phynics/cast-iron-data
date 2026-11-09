+++
id = "ref/spell/simulacrum-lesser"
kind = "spell"
title = "Lesser Simulacrum"
source_ids = ["core-rulebook", "ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "simulacrum_lesser", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/simulacrum" },
]
[[sources]]
publication = "ultimate-magic"
page = "238"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 hour"
components = "V, S, M (an ice sculpture of the target plus powdered rubies worth 50 gp per HD of the simulacrum)"
range = "0 ft."
effects = [
  { label = "Effect", value = "one duplicate creature" },
]
duration = "1 hour/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 4: Arcanist, Psychic, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 hour
Components: V, S, M (an ice sculpture of the target plus powdered rubies worth 50 gp per HD of the simulacrum)
Range: 0 ft.
Effect: one duplicate creature
Duration: 1 hour/level
Saving throw: none
Spell resistance: no
Subschool: Shadow
:::

### Lesser Simulacrum

This spell functions as [simulacrum](ref/spell/simulacrum), except you can't create a simulacrum of
a creature whose HD or levels exceed your caster level, and it has no magical abilities. The
creature is not under your control, though it recognizes you are its creator.
