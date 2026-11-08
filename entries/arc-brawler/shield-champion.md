+++
id = "ref/arc-brawler/shield-champion"
kind = "archetype"
title = "Shield Champion"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shield_champion", path = "json/archetypes_brawler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/brawler" },
]

[fields]
kind = "archetype"
replaces = ["Weapon and armor proficiencies", "Maneuver training at 3rd", "7th", "and 11th levels", "Brawler's strike", "Maneuver training gained at 15th and 19th levels"]
+++

**Sources:** Advanced Class Guide pg 86\
Stalwart in battle, a shield champion has perfected an entire martial discipline relying on only her
hand-to-hand fighting skills and her ever-present shield. What she forgoes in weapon versatility and
improved combat maneuvering, she makes up for in her ability to turn her defense into a weapon.

**Weapon and Armor Proficiency**

**Info:** A shield champion is proficient with all simple weapons and with shields as weapons. She
is also proficient with light armor, and with [bucklers](ref/eq-armor/buckler), light shields, and
heavy shields.

**Replaces:** Weapon and armor proficiencies

**Throw Shield (Ex)**

**Ability:** A shield champion can throw a heavy or light shield as a normal (non-improvised) thrown
weapon with a range increment of 10 feet or the shield's range increment, whichever is greater. The
thrown shield deals the same damage as a [shield bash](ref/misc/shield-bash), and any damage
increases from [shield spikes](ref/eq-armorenh/shield-spikes) apply to this attack. A shield
champion is treated as having the [Far Shot](ref/feat/far-shot) feat for the purpose of determining
range increment penalties for throwing a shield.

**At 11th Level:** A shield champion gains [Shield Master](ref/feat/shield-master) as a bonus feat.
She must meet all prerequisites before selecting that feat.

**At 7th Level:** A shield champion can use a thrown shield to perform a bull rush, dirty trick,
disarm, reposition, or trip [combat maneuver](ref/rule/combat-maneuvers) as if she were making a
melee shield bash attack.

**Gained:** At 3rd Level

**Replaces:** Maneuver training at 3rd, 7th, and 11th levels

**Returning Shield (Ex)**

**Action:** Ability

**At 12th Level:** A shield champion can use her unarmed strike damage when dealing damage with a
shield (whether in melee or thrown) or the shield's damage, whichever is greater.

**At 17th Level:** By ricocheting her shield off a nearby surface before hitting her intended
target, she can treat that surface as the origin square of the attack to determine whether the
target is [flanked](ref/rule/flanking) and whether the target gains a [cover](ref/rule/cover) bonus
to its AC. She can use this ability to attack a creature with
[total concealment](ref/rule/concealment) from her if she knows what square it occupies, but the
attack still has a 50% miss chance.

**At 9th Level:** A shield champion gains [Greater Shield Focus](ref/feat/greater-shield-focus) as a
bonus feat. She must meet all prerequisites before selecting that feat.

**Gained:** At 5th Level

**Replaces:** Brawler's strike

**Special:** A shield champion can throw a shield as part of a brawler's flurry.

A shield champion can throw a shield so it ricochets off her target (and possibly other solid
objects) to return to her at the end of her turn. This ability functions whether or not the shield
champion hits her opponent or moves on her turn. The shield deals no damage to targets it bounces
off other than the original target of the shield champion's attack. Other circumstances can prevent
the shield from returning to the shield champion, such as an opponent using a
[readied action](ref/rule/ready) to catch the shield, or the shield sticking to a
[mimic's](ref/monster/mimic) adhesive. The shield champion can opt to not have a thrown shield
return to her, in which case it falls to the ground as it normally would. If the shield has the
[returning](ref/magic-enh/returning) weapon special ability, she can use either that or this
ability.

If a shield champion has additional attacks from a high base attack bonus, these additional attacks
can be ricochets off an earlier target. The distance to each additional target adds to the total
range of the shield, and range penalties apply, but there are no additional penalties for attacking
in this manner. Because ricocheting attacks are treated as separate attacks, effects and modifiers
that only apply to one attack roll (such as [true strike](ref/spell/true-strike)) only apply to the
first attack and not to the others.

**Champion Defense (Ex)**

**Ability:** Once per day when she would be reduced to 0 or fewer hit points by damage in combat
from a weapon, unarmed, or natural attack, the shield champion can attempt to absorb all the damage
with her shield. To use this ability, the shield champion must attempt a Fortitude saving throw,
with the DC equal to the damage dealt. If it succeeds, she takes only half damage from the blow;
otherwise, she takes full damage. She must be aware of the attack and able to react to it in order
to use this ability - if she is denied her Dexterity bonus to AC, she can't use this ability.

**At 19th Level:** She can use this ability twice per day.

**Gained:** At 15th Level

**Replaces:** Maneuver training gained at 15th and 19th levels
