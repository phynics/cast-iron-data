+++
id = "ref/spell/blade-of-bright-victory"
kind = "spell"
title = "Blade of Bright Victory"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blade_of_bright_victory", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["good"]
levels = [
  { class = "Paladin", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "your paladin bonded weapon" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Paladin
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: no
Target: your paladin bonded weapon
Descriptors: good
:::

**Sources:** Ultimate Magic pg 208

You strengthen the bond between your divine bond weapon and its celestial spirit. The weapon gains
the [ghost touch](ref/magic-enh/ghost-touch-weapon) property. You may change your weapon's damage
type (bludgeoning, piercing, slashing) as a swift action. You gain a sacred bonus to your CMD
against disarm and sunder attacks directed at your bonded weapon; this bonus is equal to half your
caster level.
