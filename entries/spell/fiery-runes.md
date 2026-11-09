+++
id = "ref/spell/fiery-runes"
kind = "spell"
title = "Fiery Runes"
source_ids = ["melee-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fiery_runes", path = "json/spells4.json" },
]
[[sources]]
publication = "melee-tactics-toolbox"
page = "30"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "melee weapon touched" },
]
duration = "1 minute/level or until discharged (see text)"
saving_throw = "none"
spell_resistance = "yes (see text)"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Alchemist, Arcanist, Bloodrager, Druid, Hunter, Investigator, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute/level or until discharged (see text)
Saving throw: none
Spell resistance: yes (see text)
Target: melee weapon touched
Descriptors: fire
:::

You charge a weapon with a magic rune of fire. When the wielder of the weapon successfully strikes a
foe in melee with the weapon, the wielder can discharge the rune as a swift action to deal 1d4+1
points of fire damage to the target. This damage isn't multiplied on a critical hit. If the target
has [spell resistance](ref/rule/spell-resistance), you attempt a caster level check (1d20 + caster
level) against that spell resistance when the rune is discharged. If the rune is successfully
resisted, the spell is dispelled; otherwise, the rune deals damage normally.

For every 2 caster levels beyond 3rd the caster possesses, the rune deals an additional 1d4+1 points
of fire damage (2d4+2 at caster level 5th, 3d4+3 at 7th, and so on) to a maximum of 5d4+5 points of
fire damage at caster level 11th.
