+++
id = "ref/spell/resounding-blow"
kind = "spell"
title = "Resounding Blow"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "resounding_blow", path = "json/spells8.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "238"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["sonic"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Inquisitor", level = 5 },
  { class = "Paladin", level = 4 },
]
casting_time = "1 swift action"
components = "V"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "Fortitude partial, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Antipaladin, Paladin\
5: Inquisitor
Casting time: 1 swift action
Components: V
Range: personal
Duration: 1 round/level
Saving throw: Fortitude partial, see text
Spell resistance: no
Target: you
Descriptors: sonic
:::

You must have a melee weapon in hand to cast this spell. On a successful melee attack, your weapon
resounds with a thunderous clash. The target takes 1d6 points of sonic damage. Your weapon is not
harmed by this attack.

If you are using your judgment ability or smite ability against the target, it is staggered for 1
round on a successful attack. A successful Fortitude save negates the staggering effect.

On a successful critical hit, the target is stunned for 1 round and deafened for 1d6 rounds. A
successful Fortitude save negates the stunning and deafening effects. If you are also using judgment
or smite, your foe makes only a single save against all effects.

This spell immediately ends if your weapon leaves your hand. Resounding blow stacks with the
thundering weapon property.
