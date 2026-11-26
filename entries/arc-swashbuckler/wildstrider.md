+++
id = "ref/arc-swashbuckler/wildstrider"
kind = "archetype"
title = "Wildstrider"
aon = "ArchetypeDisplay.aspx?FixedName=Swashbuckler%20Wildstrider"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wildstrider", path = "json/archetypes_swashbuckler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/swashbuckler" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "96"

[fields]
kind = "archetype"
features = [
  { anchor = "deeds" },
  { anchor = "subterfuge", level = 1 },
  { anchor = "adroit-step", level = 3 },
  { anchor = "keen-gaze", level = 11 },
]
trades = [
  { replaces = "Dodging panache", feature = "deeds", power = "dodging panache", by = ["subterfuge"] },
  { replaces = "Kip-up", feature = "deeds", power = "kip-up", by = ["adroit-step"] },
  { replaces = "Subtle blade", feature = "deeds", power = "subtle blade", by = ["keen-gaze"] },
  { alters = "Derring-do", feature = "deeds", power = "derring-do", by = ["subterfuge"] },
  { alters = "swashbuckler's edge", feature = "deeds", power = "swashbuckler's edge", by = ["subterfuge"] },
  { alters = "Class skills" },
]
+++

Most swashbucklers call cities their home, but some prefer deserts, marshlands, mountains, or woods,
where the rough terrain grants them an advantage, and have little interest in the comforts of an
urban lifestyle.

## Class Skills {#class-skills}

A wildstrider gains Knowledge (nature), Stealth, and Survival as class skills, but does not gain
Knowledge (nobility), Sense Motive, and Sleight of Hand as class skills.

This alters the swashbuckler's class skills.

## Deeds {#deeds}

A wildstrider gains the following deeds, each of which replaces an existing deed.

## Subterfuge (Ex) {#subterfuge}

A wildstrider adds Stealth to the list of skills to which the [derring-do](ref/swashdeed/derring-do)
deed applies. At 15th level, she adds Stealth to the list of skills on which she can take 10 using
the [swashbuckler's edge](ref/swashdeed/swashbucklers-edge) deed.

This deed replaces dodging panache and alters derring-do and swashbuckler's edge.

## Adroit Step (Ex) {#adroit-step}

At 3rd level, a wildstrider can use a swift action to treat a 5-foot square of
[difficult terrain](ref/rule/terrain-and-obstacles) as if it were normal terrain. If she also spends
a panache point, she can treat all difficult terrain as though it were normal terrain until the end
of her turn.

This deed replaces kip-up.

## Keen Gaze (Ex) {#keen-gaze}

At 11th level, while a wildstrider has at least 1 panache point, she can ignore the miss chance from
[concealment](ref/rule/concealment) (but not total concealment) caused by normal and magical fog,
smoke, and undergrowth, but not other sources of concealment or a miss chance, such as
_[blur](ref/spell/blur)_.

This deed replaces subtle blade.
