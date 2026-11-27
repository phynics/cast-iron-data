+++
id = "ref/arc-samurai/sword-saint"
kind = "archetype"
title = "Sword Saint"
aon = "ArchetypeDisplay.aspx?FixedName=Samurai%20Sword%20Saint"
source_ids = ["dragon-empires-primer"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sword_saint", path = "json/archetypes_samurai.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/samurai" },
]
[[sources]]
publication = "dragon-empires-primer"
page = "22"

[fields]
kind = "archetype"
features = [
  { anchor = "iaijutsu-strike", level = 1 },
  { anchor = "brutal-slash", level = 3 },
  { anchor = "terrifying-iaijutsu", level = 5 },
  { anchor = "roaring-iaijutsu", level = 14 },
]
trades = [
  { replaces = "Mount", feature = "mount", by = ["iaijutsu-strike"] },
  { replaces = "Mounted charge", by = ["brutal-slash"] },
  { replaces = "Banner", feature = "banner", by = ["terrifying-iaijutsu"] },
  { replaces = "Greater banner", feature = "greater-banner", by = ["roaring-iaijutsu"] },
]
+++

Sword saints hail from lands where samurai are prevalent, and are often [ronin](ref/order/ronin) who
wander the world seeking new challenges to perfect their intricate style of swordplay called
_iaijutsu_. The following benefits apply only when a sword saint is using a sword and carrying
nothing in his other hand. The sword saint is an archetype of the samurai alternate class (_Ultimate
Combat_ 18).

## Iaijutsu Strike (Ex) {#iaijutsu-strike}

A sword saint can perform a lightning-quick iaijutsu strike against the target of his challenge to
inflict devastating wounds while drawing his sword. After the sword saint has challenged a foe but
before he has attacked the target of his challenge, he may choose to use his iaijutsu strike as a
full-round action, making an attack roll with his weapon as normal. In order to use this ability,
the sword saint's weapon must be sheathed at the start of his turn. If he successfully hits his
opponent with an iaijutsu strike, his attack deals an additional +1d6 points of damage. This bonus
damage increases by an additional +1d6 at 3rd level and every two levels thereafter to a maximum of
+10d6 damage at 19th level. Any extra damage as a result of a successful iaijutsu strike is not
multiplied by a critical hit.

After making an iaijutsu strike, a sword saint takes a -4 penalty to his AC until his next turn, but
his weapon is now drawn and he may continually to fight normally. Regardless of whether he hits his
opponent with the iaijutsu strike, a sword saint cannot use this ability on the same foe more than
once per day.

At 10th level, a sword saint learns to focus faster and is able to make an iaijutsu strike as a
standard action, and the penalty to his AC is reduced to -2.

This ability replaces a samurai's mount.

## Brutal Slash (Ex) {#brutal-slash}

At 3rd level, a sword saint's iaijutsu strike becomes even more deadly. If a sword saint threatens a
critical hit with his iaijutsu strike, he adds a bonus equal to 1/2 his class level to the attack
roll to confirm a critical hit. This ability replaces mounted charge.

## Terrifying Iaijutsu (Ex) {#terrifying-iaijutsu}

At 5th level, a sword saint's iaijutsu strike devastates the morale of foes that witness it. When a
sword saint successfully hits with an iaijutsu strike, all foes within 30 feet must succeed at a
Will save (DC 10 + 1/2 the sword saint's class level + the sword saint's Cha modifier) or become
[shaken](ref/misc/shaken) for 1d4+1 rounds. This ability replaces banner.

## Roaring Iaijutsu (Ex) {#roaring-iaijutsu}

At 14th level, a sword saint's iaijutsu strike deafens foes upon impact. When a sword saint
successfully hits with an iaijutsu strike, all foes within 30 feet must succeed at a Fortitude save
(DC 10 + 1/2 the sword saint's class level + the sword saint's Str modifier) or be
[deafened](ref/misc/deafened) for 1d4 minutes. This ability replaces greater banner.
