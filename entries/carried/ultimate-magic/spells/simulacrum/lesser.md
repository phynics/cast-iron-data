+++
id = "ref/carried/ultimate-magic/spells/simulacrum/lesser"
kind = "spell"
title = "Simulacrum, Lesser"
source_ids = ["ultimate-magic"]
section = ["Spells", "Simulacrum"]
tags = ["illusion", "shadow"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Magic/Spells/Simulacrum/Lesser", path = "ultimate_magic/spell/simulacrum_lesser.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["shadow"]
levels = [
  { class = "Arcanist", level = 4 },
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
School: illusion (shadow)
Level: 4: Arcanist, Sorcerer, Wizard
Casting Time: 1 hour
Components: V, S, M (an ice sculpture of the target plus powdered rubies worth 50 gp per HD of the simulacrum)
Range: 0 ft.
Effect: one duplicate creature
Duration: 1 hour/level
Saving Throw: none
Spell Resistance: no
:::

_Creates a double of a weak creature._

This spell functions as _[simulacrum](ref/spell/simulacrum)_, except you can't create a simulacrum
of a creature whose HD or levels exceed your caster level, and it has no magical abilities. The
creature is not under your control, though it recognizes you are its creator.
