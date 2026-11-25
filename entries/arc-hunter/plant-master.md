+++
id = "ref/arc-hunter/plant-master"
kind = "archetype"
title = "Plant Master"
aon = "ArchetypeDisplay.aspx?FixedName=Hunter%20Plant%20Master"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "plant_master", path = "json/archetypes_hunter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/hunter" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "53"

[fields]
kind = "archetype"
features = [
  { anchor = "plant-companion", level = 1 },
  { anchor = "plant-focus", level = 1 },
  { anchor = "green-empathy", level = 1 },
  { anchor = "plant-shield", level = 17 },
  { anchor = "master-hunter", level = 20 },
]
trades = [
  { replaces = "Animal companion", feature = "animal-companion", by = ["plant-companion"] },
  { replaces = "Animal focus", feature = "animal-focus", by = ["plant-focus"] },
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["green-empathy"] },
  { replaces = "One with the wild", feature = "one-with-the-wild", by = ["plant-shield"] },
  { alters = "Master hunter", feature = "master-hunter", by = ["master-hunter"] },
]
+++

Some hunters form a bond with plant life instead of an animal and take on those aspects instead.
These hunters form potent bonds with plant creatures, and their leafy or fungal friends are more
than capable of anything another hunter's animal allies can accomplish.

## Plant Companion (Ex) {#plant-companion}

A plant master forms a mystic bond with a plant companion. A plant master can begin play with any
plant companion (see page 182 and page 26 of the _Pathfinder RPG Advanced Race Guide_). Except for
the companion being a creature of the plant type, this ability otherwise works like the druid's
animal companion.

This replaces animal companion.

## Plant Focus (Su) {#plant-focus}

A plant master can take on the aspect of a plant as a swift action. He must select one type of plant
to emulate, gaining a bonus or special ability based on the type of plant emulated and his hunter
level. The plant master can use this ability for a number of minutes per day equal to his level.
This duration does not need to be consecutive but must be spent in 1-minute increments. He can
emulate only one plant at a time.

The plant master can also apply one of these aspects to his plant companion. An aspect applied in
this way does not count against the hunter's minutes of duration per day—it remains in effect until
he changes it. The companion's aspect can be the same aspect the hunter has taken on or a different
one. A plant master can select or change the plant foci on both himself and his plant companion as
part of the same swift action.

### Assassin Vine {#assassin-vine}

The creature gains a +2 bonus on combat maneuver checks to grapple. This bonus increases to +3 at
8th level and +4 at 15th level.

### Brambles {#brambles}

When the creature is hit by an unarmed strike or natural attack, the attacker takes 1 point of
piercing damage. This increases to 2 points at 8th level and 3 points at 15th level.

### Creeping Vine {#creeping-vine}

The creature gains a +4 competence bonus on Climb checks. This bonus increases to +6 at 8th level
and +8 at 15th level.

### Giant Flytrap {#giant-flytrap}

The creature gains a +4 competence bonus on Stealth checks. This bonus increases to +6 at 8th level
and +8 at 15th level.

### Mushroom {#mushroom}

The creature gains a +4 enhancement bonus on saves against poison. This bonus increases to +6 at 8th
level and +8 at 15th level.

### Oak {#oak}

The creature gains a +2 enhancement bonus to CMD. This bonus increases to +4 at 8th level and +6 at
15th level.

### Shrieker {#shrieker}

The creature gains [darkvision](ref/rule/darkvision) with a range of 60 feet. At 8th level, the
range increases by 30 feet. At 15th level, the creature also gains [blindsense](ref/umr/blindsense)
with a range of 10 feet.

### Spore {#spore}

The creature gains a +4 competence bonus on Fly checks. This bonus increases to +6 at 8th level and
+8 at 15th level.

### Water Lily {#water-lily}

The creature gains a +4 competence bonus on Swim checks. This bonus increases to +6 at 8th level and
+8 at 15th level.

This replaces animal focus.

## Green Empathy (Ex) {#green-empathy}

A plant master can improve the attitude of a plant creature.

Green empathy functions like a Diplomacy check to improve the attitude of a person.

The plant master rolls 1d20 and adds his hunter level and his Charisma modifier to determine the
wild empathy check result. The typical wild plant creature has a starting attitude of indifferent.

To use green empathy, the plant master and the plant creature must be within 30 feet of each other
under normal conditions.

Generally, influencing a plant creature in this way takes 1 minute, but as with influencing people,
it might take more or less time.

A plant master can also use this ability to influence an animal, but he takes a -4 penalty on the
check. He has no ability to influence magical beasts.

This replaces the wild empathy class feature.

## Plant Shield (Ex) {#plant-shield}

At 17th level, a plant master and his companion are distasteful to plant creatures. Creatures of the
plant type with an Intelligence score of 2 or lower will not willingly attack either the plant
master or his companion unless magically compelled to do so or the plant master or his companion
attacks the creature first.

This replaces one with the wild.

## Master Hunter (Ex) {#master-hunter}

At 20th level, when a plant master prepares spells for the day, he chooses one plant focus to be
active for the entire day.

This alters master hunter.
