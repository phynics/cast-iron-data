+++
id = "ref/spell/umbral-weapon"
kind = "spell"
title = "Umbral Weapon"
aon = "SpellDisplay.aspx?ItemName=Umbral%20Weapon"
source_ids = ["melee-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "umbral_weapon", path = "json/spells11.json" },
]
[[sources]]
publication = "melee-tactics-toolbox"
page = "31"

[fields]
kind = "spell"
school = "illusion"
descriptors = ["cold", "shadow"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a pair of miniature swords)"
range = "touch"
effects = [
  { label = "Target", value = "melee weapon touched" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 2: Antipaladin, Arcanist, Bard, Magus, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a pair of miniature swords)
Range: touch
Duration: 1 round/level
Saving throw: none
Spell resistance: yes
Target: melee weapon touched
Descriptors: cold, shadow
:::

A shadowy afterimage trails behind the targeted weapon, potentially damaging foes even when the
weapon misses. Once per round, when the weapon's wielder misses a creature with the target weapon,
the wielder can reroll the attack. If the reroll hits, the spell hits the targeted creature and
deals 1d8 points of cold damage, plus 1 additional point per 2 caster levels (maximum +10). If an
attacked creature has [spell resistance](ref/rule/spell-resistance), you must attempt a caster level
check (1d20 + caster level) against that spell resistance the first time the spell damages the
target. If the creature successfully resists umbral weapon, the spell is dispelled. If not, the
creature takes damage as normal.
