+++
id = "ref/rule/spell-damage"
kind = "rule"
title = "Spell Damage and Damage Caps"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spell_damage", path = "json/rules_adv_magic01.json" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Magic pg 129

One of the easiest ways to measure an offensive spell's power is to look at how much damage it does.
Offensive spells are the easiest spells to design in the game, and there are dozens of examples of
them in the Core Rulebook. A typical damage spell deals 1 die of damage (typically a d6) per caster
level for an arcane spell (for example, [shocking grasp](ref/spell/shocking-grasp) or
[fireball](ref/spell/fireball)), or 1 die of damage (typically a d6, but sometimes a d8) per two
caster levels for a divine spell (for example, [searing light](ref/spell/searing-light)).

### Damage Caps

Low-level damage spells are not as good as medium- or high-level damage spells - the game is
designed so lower-level spells eventually reach a maximum amount of damage they can deal. This is
because if low-level spells continued to increase in damage without hitting a maximum amount, they'd
rival some higher-level spells for effectiveness, and the game isn't as interesting if casters are
using the same spells at 20th level as they were at 1st.

The maximum damage depends on the level of the spell and whether the spell is arcane or divine. This
is because arcane magic is deliberately designed to be better at dealing damage to balance the fact
that divine magic is better at healing. A "single target" spell only damages one creature (like
_[shocking grasp](ref/spell/shocking-grasp)_), or divides its damage among several creatures (like
[burning hands](ref/spell/burning-hands) or [magic missile](ref/spell/magic-missile)). A "multiple
target" spell applies its full damage to several creatures (like _[fireball](ref/spell/fireball)_).

For example, a 1st-level single-target wizard spell like
_[shocking grasp](ref/spell/shocking-grasp)_ can deal a maximum of 5 dice of damage (specifically
5d6). _[Magic missile](ref/spell/magic-missile)_ can be used against a single target, or the caster
can split up the missiles to affect multiple creatures, dividing the single-target damage among
them. _[Burning hands](ref/spell/burning-hands)_ initially looks like it doesn't obey the damage cap
table because it deals multiple dice of damage against multiple creatures, but this is offset by the
fact that it only deals d4s instead of d6s, and it has an extremely close and limited area of
effect.

When looking at the Maximum Damage tables, also keep in mind that arcane spells usually use d6s for
damage and divine spells usually use d8s, and these tables assume d6s; when looking at the damage
caps for divine spells, count each d8 as 2d6. Thus, [searing light](ref/spell/searing-light) is a
3rd-level single-target cleric spell that deals up to 5d8 points of damage; treating each d8 as 2d6,
that counts as 10d6, which is on target for a 3rd-level cleric spell. (Note that the 1d6 per level
and maximum 10d6 points of damage against undead are still correct for a spell of this level, and
the slightly higher damage against light-vulnerable undead is offset by the reduced damage against
constructs).

**Tip:** If your spell does _more_ damage than the amount defined on the table, you should reduce
the damage or increase the spell's level. If your spell does _less_ damage than the amount defined
on the table, you should increase the damage or add another effect to the spell. An example of this
is [sound burst](ref/spell/sound-burst), which only deals 1d8 points of damage (this amount never
increases), but can stun creatures in the area.

### Table 2-5: Maximum Damage for Arcane Spells

|Spell Level|Max Damage (Single Target)|Max Damage (Multiple Targets)|
| --- | --- | --- |
|1st|5 dice|-|
|2nd|10 dice|5 dice|
|3rd|10 dice|10 dice|
|4th|15 dice|10 dice|
|5th|15 dice|15 dice|
|6th|20 dice|15 dice|
|7th|20 dice|20 dice|
|8th|25 dice|20 dice|
|9th|25 dice|25 dice|

### Table 2-6: Maximum Damage for Divine Spells

|Spell Level|Max Damage (Single Target)|Max Damage (Multiple Targets)|
| --- | --- | --- |
|1st|1 die|-|
|2nd|5 dice|1 die|
|3rd|10 dice|5 dice|
|4th|10 dice|10 dice|
|5th|15 dice|10 dice|
|6th|15 dice|15 dice|
|7th|20 dice|15 dice|
|8th|20 dice|20 dice|
|9th|25 dice|20 dice|
