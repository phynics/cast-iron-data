+++
id = "ref/arc-gunslinger/techslinger"
kind = "archetype"
title = "Techslinger"
aon = "ArchetypeDisplay.aspx?FixedName=Gunslinger%20Techslinger"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "techslinger", path = "json/archetypes_gunslinger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/gunslinger" },
]
[[sources]]
publication = "technology-guide"
page = "13"

[fields]
kind = "archetype"
features = [
  { anchor = "covet-charge", level = 1 },
  { anchor = "reliable", level = 1 },
  { anchor = "charge-recycling", level = 11 },
  { anchor = "heavy-weaponry-deeds", level = 11 },
  { anchor = "technic-training", level = 5 },
]
trades = [
  { replaces = "Deadeye", feature = "deeds", power = "deadeye", by = ["covet-charge"] },
  { replaces = "Quick clear", feature = "deeds", power = "quick clear", by = ["reliable"] },
  { replaces = "Expert loading", feature = "deeds", power = "expert loading", by = ["charge-recycling"] },
  { replaces = "Gun training", feature = "gun-training", by = ["technic-training"] },
]
+++

Techslingers spurn unreliable gunpowder weapons in favor of high-tech armaments. They learn to
master the quirks of [timeworn technology](ref/rule/timeworn-technology) and methods of keeping
weapons charged in a primitive world. Techslingers still start play with the black powder
blunderbuss, pistol, or rifle granted by the gunsmith class ability, but they gain specialized
powers for use after they gain weapons of advanced technology. A techslinger has the following class
features.

## Deeds {#deeds}

Techslingers have access to all gunslinger deeds, except as noted below for new deeds that replace
standard gunslinger deeds.

## Covet Charge (Ex) {#covet-charge}

At 1st level, a techslinger can spend 1 grit point to use 1 charge fewer than normal when firing a
technological weapon (minimum 0), as long as the weapon has enough charges remaining to be fired at
least once. This deed replaces deadeye.

## Reliable (Ex) {#reliable}

At 1st level, a techslinger can spend 1 grit point as a free action to prevent a timeworn firearm
from glitching. This deed replaces quick clear.

## Charge Recycling (Ex) {#charge-recycling}

At 11th level, by spending 1 grit point, a techslinger can grant 1 temporary charge to a
technological firearm, even if the firearm normally can no longer be recharged. This charge must be
used within 1 hour or it fades. The techslinger can grant temporary charges to multiple firearms as
long as she has enough grit, but temporary charges do not stack with themselves in the same firearm.
At 15th level, the techslinger can grant 2 temporary charges when she uses this deed, and at 19th
level, she can grant 3 temporary charges. This deed replaces expert loading.

## Heavy Weaponry Deeds (Ex) {#heavy-weaponry-deeds}

At 11th level, as long as the techslinger has at least 1 grit point, she can treat a heavy weapon as
a firearm for the purpose of using deeds.

## Bonus Feats {#bonus-feats}

A techslinger can select [Technologist](ref/feat/technologist) as a bonus feat, even though it's
neither a combat nor a grit feat.

## Technic Training (Ex) {#technic-training}

Starting at 5th level, a techslinger can select one specific type of advanced technology firearm
(such as a [laser pistol](ref/tech-weapon/laser-pistol), [mindrender](ref/tech-weapon/mindrender),
[stun gun](ref/tech-weapon/stun-gun), or [zero rifle](ref/tech-weapon/zero-rifle)). Thereafter, she
gains a bonus equal to her Dexterity modifier on damage rolls when using that firearm. Furthermore,
she treats all detrimental [glitches](ref/rule/weapon-glitches) of timeworn versions of her selected
firearm as a result of no glitch. (She can retain the effects of beneficial glitches if she wishes.)

Every 4 levels thereafter (9th, 13th, and 17th), the techslinger selects another type of advanced
technology firearm, gaining these bonuses for those types as well. This ability replaces gun
training.
