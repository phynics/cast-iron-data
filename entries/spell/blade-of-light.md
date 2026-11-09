+++
id = "ref/spell/blade-of-light"
kind = "spell"
title = "Blade of Light"
aon = "SpellDisplay.aspx?ItemName=Blade%20of%20Light"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blade_of_light", path = "json/spells12.json" },
]
[[sources]]
publication = "adventurers-guide"
page = "16"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["good"]
levels = [
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Paladin", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one melee weapon" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Cleric, Inquisitor, Oracle, Paladin, Warpriest
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: one melee weapon
Descriptors: good
:::

This spell infuses a weapon with pure sunlight (the weapon need not be a bladed weapon). A weapon
enhanced by this spell sheds light as if [daylight](ref/spell/daylight) had been cast on it. It
functions as a magic and good weapon for the purposes of overcoming
[damage reduction](ref/rule/damage-reduction). The weapon grants a +2 sacred bonus on attack rolls
against undead and deals +1d6 points of damage on a successful hit against such foes; against
incorporeal undead, it functions as if it had the [ghost touch](ref/magic-enh/ghost-touch-weapon)
weapon special ability. The weapon automatically confirms critical hits against foes that are
vulnerable to sunlight.
