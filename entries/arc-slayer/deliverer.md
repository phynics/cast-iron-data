+++
id = "ref/arc-slayer/deliverer"
kind = "archetype"
title = "Deliverer"
aon = "ArchetypeDisplay.aspx?FixedName=Slayer%20Deliverer"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "deliverer", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "advanced-class-guide"
page = "119"

[fields]
kind = "archetype"
features = [
  { anchor = "determined-zeal", level = 2 },
  { anchor = "true-believer", level = 6 },
  { anchor = "divine-anathema", level = 10 },
  { anchor = "ex-deliverers" },
]
trades = [
  { replaces = "Slayer talent gained at 2nd level", feature = "slayer-talents", levels = [2], by = ["determined-zeal"] },
  { replaces = "Slayer talent gained at 6th level", feature = "slayer-talents", levels = [6], by = ["true-believer"] },
  { replaces = "Advanced slayer talent gained at 10th level", feature = "advanced-talents", levels = [10], by = ["divine-anathema"] },
  { alters = "Weapon and armor proficiency", feature = "weapon-and-armor-proficiencies" },
]
+++

Also known as a divine assassin, god's blade, or wrath-bringer, a deliverer is a weapon chosen by a
god to punish those who have committed an affront to that deity. Evil deities are more likely to use
assassins than deliverers, but some good deities use deliverers to deal with problems of a subtler
nature than a cleric, inquisitor, paladin, or warpriest can typically handle.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A deliverer gains proficiency with his deity's favored weapon, in addition to the slayer's normal
weapon proficiencies. This ability alters the slayer's weapon and armor proficiency.

## Determined Zeal (Ex) {#determined-zeal}

At 2nd level, a deliverer shrugs off attempts by his moral opposite to control or kill him. On any
round in which deliverer attacks an opponent whose alignment is at least two steps away from his own
(such as a lawful good deliverer fighting a chaotic good or lawful evil foe, or a neutral foe with
no other alignment components), he gains a +2 bonus on Will saving throws against that opponent's
abilities, as well as the benefit of the [Diehard](ref/feat/diehard) feat until the end of his next
turn. This ability replaces the slayer talent gained at 2nd level.

## True Believer (Ex) {#true-believer}

At 6th level, mortal wounds cannot stop a deliverer from performing his divine duty. On any round in
which he attacks an opponent whose alignment is at least two steps away from his own (see Determined
Zeal, above) while benefiting from the Diehard feat, he isn't staggered from having negative hit
points, nor does he automatically lose 1 hit point per round. This ability replaces the slayer
talent gained at 6th level.

## Divine Anathema (Ex) {#divine-anathema}

At 10th level, as a free action a deliverer can declare a studied target to be his divine anathema.
The studied target's alignment must be at least two steps away from that of the deliverer. Against
this target, the deliverer's attacks deal an additional 2d6 points of damage; this damage is
directly from divine power and does not stack with the bonus damage from a
_[holy](ref/magic-enh/holy)_ or _[unholy](ref/magic-enh/unholy)_ weapon, or a weapon with a similar
weapon special ability or effect. A deliverer can have only one divine anathema at a time. This
ability replaces the advanced slayer talent gained at 10th level.

## Slayer Talents {#slayer-talents}

The following slayer talents (and rogue talents) complement the deliverer archetype: combat trick,
finesse rogue, foil scrutiny, terrain mastery, trap spotter, and trapfinding. (Those with asterisks
\[\*\] are detailed in the slayer class, starting on page 53.)

## Advanced Slayer Talents {#advanced-slayer-talents}

The following advanced slayer talents (and advanced rogue talents) complement the deliverer
archetype: assassinate, evasion, hunter's surprise, and master of disguise.

## Ex-Deliverers {#ex-deliverers}

A deliverer who grossly violates the code of conduct required by his deity loses all class features
granted by this archetype, except for the weapon proficiencies. (He does not gain the slayer class
abilities that the archetype replaces.) He cannot thereafter gain levels as a deliverer of that
deity until he atones for his deeds (see the _[atonement](ref/spell/atonement)_ spell description).
