+++
id = "ref/rule/breaking-things"
kind = "rule"
title = "Breaking Things"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "breaking_things", path = "json/rules_basics04.json" },
]
[[sources]]
publication = "core-rulebook"
page = "173"

[fields]
kind = "none"
+++

When attempting to break an object, you have two choices: smash it with a weapon or break it with
sheer strength.

### Smashing an Object

Smashing a weapon or shield with a slashing or bludgeoning weapon is accomplished with the
[sunder](ref/rule/sunder) combat maneuver. Smashing an object is like sundering a weapon or shield,
except that your combat maneuver check is opposed by the object's AC. Generally, you can smash an
object only with a bludgeoning or slashing weapon.

**Armor Class:** Objects are easier to hit than creatures because they don't usually move, but many
are tough enough to shrug off some damage from each blow. An object's Armor Class is equal to 10 +
its size modifier (see Table 7-11) + its Dexterity modifier. An inanimate object has not only a
Dexterity of 0 (-5 penalty to AC), but also an additional -2 penalty to its AC. Furthermore, if you
take a full-round action to line up a shot, you get an automatic hit with a melee weapon and a +5
bonus on attack rolls with a ranged weapon.

**Hardness:** Each object has **[hardness](ref/umr/hardness)** - a number that represents how well
it resists damage. When an object is damaged, subtract its hardness from the damage. Only damage in
excess of its hardness is deducted from the object's hit points (see Table 7-12, Table 7-13, and
Table 7-14).

**Hit Points:** An object's hit point total depends on what it is made of and how big it is (see
Table 7-12, Table 7-13, and Table 7-14). Objects that take damage equal to or greater than half
their total hit points gain the [broken condition](ref/misc/broken). When an object's hit points
reach 0, it's ruined.

Very large objects have separate hit point totals for different sections.

**Energy Attacks:** Energy attacks deal half damage to most objects. Divide the damage by 2 before
applying the object's [hardness](ref/umr/hardness). Some energy types might be particularly
effective against certain objects, subject to GM discretion. For example, fire might do full damage
against parchment, cloth, and other objects that burn easily. Sonic might do full damage against
glass and crystal objects.

**Ranged Weapon Damage:** Objects take half damage from ranged weapons (unless the weapon is a
[siege engine](ref/rule/siege-engines) or something similar). Divide the damage dealt by 2 before
applying the object's [hardness](ref/umr/hardness).

**Ineffective Weapons:** Certain weapons just can't effectively deal damage to certain objects.
Likewise, most melee weapons have little effect on stone walls and doors, unless they are designed
for breaking up stone, such as a pick or hammer.

**Immunities:** Objects are immune to nonlethal damage and to critical hits.

**Magic Armor, Shields, and Weapons:** Each +1 of enhancement bonus adds 2 to the
[hardness](ref/umr/hardness) of armor, a weapon, or a shield, and +10 to the item's hit points.

**Vulnerability to Certain Attacks:** Certain attacks are especially successful against some
objects. In such cases, attacks deal double their normal damage and may ignore the object's
[hardness](ref/umr/hardness).

**Damaged Objects:** A damaged object remains functional with the broken condition until the item's
hit points are reduced to 0, at which point it is destroyed.

Damaged (but not destroyed) objects can be repaired with the Craft skill and a number of spells.

**Saving Throws:** Nonmagical, unattended items never make saving throws. They are considered to
have failed their saving throws, so they are always fully affected by spells and other attacks that
allow saving throws to resist or negate. An item attended by a character (being grasped, touched, or
worn) makes saving throws as the character (that is, using the character's saving throw bonus).

Magic items always get saving throws. A magic item's Fortitude, Reflex, and Will save bonuses are
equal to 2 + half its caster level. An attended magic item either makes saving throws as its owner
or uses its own saving throw bonus, whichever is better.

**Animated Objects:** Animated objects count as creatures for purposes of determining their Armor
Class (do not treat them as inanimate objects).

### Table 7-11: Size and Armor Class of Objects

|Size|AC Modifier|
| --- | --- |
|Colossal|-8|
|Gargantuan|-4|
|Huge|-2|
|Large|-1|
|Medium|+0|
|Small|+1|
|Tiny|+2|
|Diminutive|+4|
|Fine|+8|

### Table 7-12: Common Armor, Weapon, and Shield Hardness and Hit Points

|Weapon or Shield|Hardness^[1](ref/rule/breaking-things#footnote-1)^|Hit Points^[2](ref/rule/breaking-things#footnote-2)^|
| --- | --- | --- |
|Light blade|10|2|
|One-handed blade|10|5|
|Two-handed blade|10|10|
|Light metal-hafted weapon|10|10|
|One-handed metal-hafted weapon|10|20|
|Light hafted weapon|5|2|
|One-handed hafted weapon|5|5|
|Two-handed hafted weapon|5|10|
|Projectile weapon|5|5|
|Armor|Special^[3](ref/rule/breaking-things#footnote-3)^|armor bonus × 5|
|Buckler|10|5|
|Light wooden shield|5|7|
|Heavy wooden shield|5|15|
|Light steel shield|10|10|
|Heavy steel shield|10|20|
|Tower shield|5|20|

### Table 7-13: Substance Hardness and Hit Points

|Substance|Hardness|Hit Points|
| --- | --- | --- |
|Glass|1|1/in. of thickness|
|Paper or cloth|0|2/in. of thickness|
|Rope|0|2/in. of thickness|
|Ice|0|3/in. of thickness|
|Leather or hide|2|5/in. of thickness|
|Wood|5|10/in. of thickness|
|Stone|8|15/in. of thickness|
|Iron or steel|10|30/in. of thickness|
|Mithral|15|30/in. of thickness|
|Adamantine|20|40/in. of thickness|

### Table 7-14: Object Hardness and Hit Points

|Object|Hardness|Hit Points|DC|
| --- | --- | --- | --- |
|Rope (1 in. diameter)|0|2|23|
|Simple wooden door|5|10|13|
|Small chest|5|1|17|
|Good wooden door|5|15|18|
|Treasure chest|5|15|23|
|Strong wooden door|5|20|23|
|Masonry wall (1 ft. thick)|8|90|35|
|Hewn stone (3 ft. thick)|8|540|50|
|Chain|10|5|26|
|Manacles|10|10|26|
|Masterwork manacles|10|10|28|
|Iron door (2 in. thick)|10|60|28|

### Breaking Items

When a character tries to break or burst something with sudden force rather than by dealing damage,
use a Strength check (rather than an attack roll and damage roll, as with the sunder special attack)
to determine whether he succeeds. Since [hardness](ref/umr/hardness) doesn't affect an object's
break DC, this value depends more on the construction of the item than on the material the item is
made of. Consult Table 7-15 for a list of common break DCs.

If an item has lost half or more of its hit points, the item gains the
[broken condition](ref/misc/broken) and the DC to break it drops by 2.

Larger and smaller creatures get size bonuses and size penalties on Strength checks to break open
doors as follows: Fine -16, Diminutive -12, Tiny -8, Small -4, Large +4, Huge +8, Gargantuan +12,
Colossal +16.

A [crowbar](ref/eq-misc/crowbar) or [portable ram](ref/eq-misc/portable-ram) improves a character's
chance of breaking open a door.

### Table 7-15: DCs to Break or Burst Items

|Strength Check to:|DC|
| --- | --- |
|Break down simple door|13|
|Break down good door|18|
|Break down strong door|23|
|Burst rope bonds|23|
|Bend iron bars|24|
|Break down barred door|25|
|Burst chain bonds|26|
|Break down iron door|28|

### Conditions That Alter DCs

|Condition|DC Adjustment\*|
| --- | --- |
|Hold portal|+5|
|Arcane lock|+10|

\* If both apply, use the larger number.

###### ^1^ {#footnote-1}

Add +2 for each +1 enhancement bonus of magic items.

###### ^2^ {#footnote-2}

The hp value given is for Medium armor, weapons, and shields. Divide by 2 for each size category of
the item smaller than Medium, or multiply it by 2 for each size category larger than Medium. Add 10
hp for each +1 enhancement bonus of magic items.

###### ^3^ {#footnote-3}

Varies by material; see Table 7-13: Substance [Hardness](ref/umr/hardness) and Hit Points.
