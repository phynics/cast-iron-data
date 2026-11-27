+++
id = "ref/arc-paladin/mind-sword"
kind = "archetype"
title = "Mind Sword"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Mind%20Sword"
source_ids = ["occult-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mind_sword", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "occult-origins"
page = "20"

[fields]
kind = "archetype"
features = [
  { anchor = "mind-arsenal", level = 2 },
  { anchor = "touch-treatment", level = 3 },
  { anchor = "spells", level = 4 },
]
trades = [
  { replaces = "Lay on hands", feature = "lay-on-hands", by = ["mind-arsenal"] },
  { replaces = "Mercy", feature = "mercy", by = ["touch-treatment"] },
  { replaces = "Channel positive energy", feature = "channel-positive-energy", by = ["spells"] },
]
+++

Veterans of mystical battles against demons of the Worldwound, mind swords merge psychic and divine
power, probing and cleansing minds while their telekinetic blades cleave demonic flesh.

## Mind Arsenal (Su) {#mind-arsenal}

At 2nd level, a mind sword can make a telekinetic attack with a melee weapon. This functions as the
hand of the apprentice [universalist](ref/arcaneschool/universalist) wizard school ability, but any
calculations of that ability based on Intelligence are instead based on Charisma. At 6th level, a
mind sword can expend two uses of this ability as a full-round action to attack the same opponent
multiple times, as if using the full-attack action. At 12th level, a mind sword can expend one use
of this ability as a full-round action to combine melee attacks and ranged attacks aimed at
different targets within 60 feet as part of a single full-attack action. This ability replaces lay
on hands.

## Touch Treatment (Su) {#touch-treatment}

At 3rd level, a mind sword can expend one use of her mind arsenal ability to remove minor harmful
mental conditions, as per the [mesmerist](ref/class/mesmerist) touch treatment class feature
(_Pathfinder RPG Occult Adventures_ 43). At 9th level, she can remove moderate conditions, and at
15th level, she can remove major conditions. This ability replaces mercy.

## Spells {#spells}

A mind sword adds the following psychic spells to her paladin spell list at the listed spell levels:
1st—_detect psychic significance, mage hand, telekinetic projectile, thought shield I_; 2nd—_apport
object, enshroud thoughts, mental barrier I, thought shield II_; 3rd—_intellect fortress I, mental
barrier II, telekinetic maneuver, thought shield III_; 4th—_intellect fortress II, telekinesis,
thought shield IV, thoughtsense, tower of iron will I_. The mind sword can prepare and cast these
psychic spells as divine paladin spells. However, the mind sword cannot use these spells for item
creation, including making potions or scrolls of these spells. This ability replaces channel
positive energy.
