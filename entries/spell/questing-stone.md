+++
id = "ref/spell/questing-stone"
kind = "spell"
title = "Questing Stone"
source_ids = ["seekers-of-secrets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "questing_stone", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/arcane-eye" },
]
[[sources]]
publication = "seekers-of-secrets"
page = "17"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "10 minutes"
components = "V, S, F"
range = "touch and unlimited"
effects = [
  { label = "Target", value = "one ioun stone touched" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 4: Arcanist, Bard, Skald, Sorcerer, Wizard
Casting time: 10 minutes
Components: V, S, F
Range: touch and unlimited
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: one ioun stone touched
:::

This spell functions like [arcane eye](ref/spell/arcane-eye), except that it uses an ioun stone as a
visible scrying sensor. The ioun stone moves at the same rate as an arcane eye, and may pass through
holes or spaces as small as 2 inches in diameter. It can enter another plane of existence using a
gate or similar portal, but the caster loses contact with the sensor should this occur. The enhanced
ioun stone has AC 24, 10 hp, [hardness](ref/umr/hardness) 5, fly speed 30 (perfect), and a +16
Stealth bonus. The stone does not provide you with its normal benefits while you are using it as a
scrying sensor.
