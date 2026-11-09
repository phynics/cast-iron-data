+++
id = "ref/spell/blessed-fist"
kind = "spell"
title = "Blessed Fist"
aon = "SpellDisplay.aspx?ItemName=Blessed%20Fist"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blessed_fist", path = "json/spells12.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "175"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["good"]
levels = [
  { class = "Cleric", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Cleric, Oracle, Paladin, Warpriest
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute/level
Saving throw: none
Spell resistance: yes
Target: creature touched
Descriptors: good
:::

The target is considered to be armed even when unarmed, so it doesn't provoke attacks of opportunity
when it attacks foes with unarmed strikes. Its unarmed strikes can deal lethal or nonlethal damage
(target's choice). If the target already has this ability (such as from the monk unarmed strike
ability or the [Improved Unarmed Strike](ref/feat/improved-unarmed-strike) feat), its unarmed
strikes gain a +1 enhancement bonus on attack rolls and damage rolls, and they count as good-aligned
weapons for the purposes of overcoming [damage reduction](ref/rule/damage-reduction).
