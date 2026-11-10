+++
id = "ref/rule/nonlethal-damage"
kind = "rule"
title = "Nonlethal Damage"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "nonlethal_damage", path = "json/rules_combat01.json" },
]
[[sources]]
publication = "core-rulebook"
page = "191"

[fields]
kind = "none"
+++

Nonlethal damage represents harm to a character that is not life-threatening. Unlike normal damage,
nonlethal damage is healed quickly with rest.

**Dealing Nonlethal Damage:** Certain attacks deal nonlethal damage. Other effects, such as heat or
being exhausted, also deal nonlethal damage. When you take nonlethal damage, keep a running total of
how much you've accumulated. Do not deduct the nonlethal damage number from your current hit points.
It is not "real" damage. Instead, when your nonlethal damage equals your current hit points, you're
staggered (see below), and when it exceeds your current hit points, you fall unconscious.

**Nonlethal Damage with a Weapon that Deals Lethal Damage:** You can use a melee weapon that deals
lethal damage to deal nonlethal damage instead, but you take a -4 penalty on your attack roll.

**Lethal Damage with a Weapon that Deals Nonlethal Damage:** You can use a weapon that deals
nonlethal damage, including an unarmed strike, to deal lethal damage instead, but you take a -4
penalty on your attack roll.

**Staggered and Unconscious:** When your nonlethal damage equals your current hit points, you're
[staggered](ref/misc/staggered). You can only take a standard action or a move action in each round
(in addition to free, immediate, and swift actions). You cease being staggered when your current hit
points once again exceed your nonlethal damage. When your nonlethal damage exceeds your current hit
points, you fall [unconscious](ref/misc/unconscious). While unconscious, you are
[helpless](ref/misc/helpless).

Spellcasters who fall unconscious retain any spellcasting ability they had before going unconscious.

If a creature's nonlethal damage is equal to his total maximum hit points (not his current hit
points), all further nonlethal damage is treated as lethal damage. This does not apply to creatures
with [regeneration](ref/umr/regeneration). Such creatures simply accrue additional nonlethal damage,
increasing the amount of time they remain unconscious.

**Healing Nonlethal Damage:** You heal nonlethal damage at the rate of 1 hit point per hour per
character level. When a spell or ability cures hit point damage, it also removes an equal amount of
nonlethal damage.
