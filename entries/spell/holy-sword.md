+++
id = "ref/spell/holy-sword"
kind = "spell"
title = "Holy Sword"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "holy_sword", path = "json/spells5.json" },
]
[[sources]]
publication = "core-rulebook"
page = "297"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["good"]
levels = [
  { class = "Paladin", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "melee weapon touched" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Paladin
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: melee weapon touched
Descriptors: good
:::

This spell allows you to channel holy power into your sword, or any other melee weapon you choose.
The weapon acts as a +5 [holy](ref/magic-enh/holy) weapon (+5 enhancement bonus on attack and damage
rolls, extra 2d6 damage against evil opponents). It also emits a
[magic circle against evil](ref/spell/magic-circle-against-evil) effect (as the spell). If the magic
circle ends, the sword creates a new one on your turn as a free action. The spell is automatically
canceled 1 round after the weapon leaves your hand. You cannot have more than one holy sword at a
time.

If this spell is cast on a magic weapon, the powers of the spell supercede any that the weapon
normally has, rendering the normal enhancement bonus and powers of the weapon inoperative for the
duration of the spell. This spell is not cumulative with bless weapon or any other spell that might
modify the weapon in any way. This spell does not work on artifacts. A masterwork weapon's bonus to
attack does not stack with an enhancement bonus to attack.
