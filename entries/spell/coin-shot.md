+++
id = "ref/spell/coin-shot"
kind = "spell"
title = "Coin Shot"
aon = "SpellDisplay.aspx?ItemName=Coin%20Shot"
source_ids = ["heroes-of-the-streets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "coin_shot", path = "json/spells2.json" },
]
[[sources]]
publication = "heroes-of-the-streets"
page = "30"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "S"
range = "touch"
effects = [
  { label = "Target", value = "up to three coins touched" },
]
duration = "10 minutes or until discharged"
saving_throw = "none"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Alchemist, Antipaladin, Arcanist, Bloodrager, Bard, Investigator, Magus, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: S
Range: touch
Duration: 10 minutes or until discharged
Saving throw: none
Spell resistance: yes (object)
Target: up to three coins touched
:::

You turn up to three coins into deadly projectiles that gain the velocity of a bullet when thrown.
The coins retain their normal appearance but can be used as simple thrown weapons with a range
increment of 20 feet and a critical multiplier of ×2. The transmuted coins are treated as ammunition
for the purposes of drawing them. Like firearm bullets, the coins deal bludgeoning and piercing
damage, and attacks with them are resolved as touch attacks within the first range increment.
Regardless of whether a transmuted coin hits or misses the target, it is destroyed after the attack.
Only you can make attacks with the coins, though other creatures can safely handle them without
discharging the spell.

You can make a single ranged attack with a coin as part of casting this spell. Different types of
coins create different bullet effects. Copper coins deal 1d4 points of damage. Silver coins deal 1d6
points of damage and count as silver for the purpose of overcoming
[damage reduction](ref/rule/damage-reduction). Gold coins deal 1d8 points of damage and count as
masterwork weapons. Platinum coins deal 1d10 points of damage, count as masterwork weapons, and are
treated as adamantine weapons for the purposes of overcoming damage reduction and bypassing
[hardness](ref/umr/hardness). All coin bullets deal an additional 1 point of damage per 2 caster
levels (to a maximum of an extra 10 points of damage at 20th level).
