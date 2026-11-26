+++
id = "ref/arc-occultist/construct-collector"
kind = "archetype"
title = "Construct Collector"
aon = "ArchetypeDisplay.aspx?FixedName=Occultist%20Construct%20Collector"
source_ids = ["construct-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "construct_collector", path = "json/archetypes_occultist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/occultist" },
]
[[sources]]
publication = "construct-handbook"
page = "11"

[fields]
kind = "archetype"
features = [
  { anchor = "constructed-focus", level = 3 },
  { anchor = "repower-construct", level = 8 },
]
trades = [
  { replaces = "Focus power selected at 3rd level, 9th level, and 15th level", feature = "focus-powers", levels = [3, 9, 15], by = ["constructed-focus"] },
  { replaces = "Magic circles", feature = "magic-circles", by = ["repower-construct"] },
  { replaces = "outside contact", feature = "outside-contact", by = ["repower-construct"] },
  { replaces = "binding circles", feature = "binding-circles", by = ["repower-construct"] },
  { replaces = "fast circles", feature = "fast-circles", by = ["repower-construct"] },
]
+++

Trapped within each construct is a spiritual presence, be it a bound elemental or raw magical
energy. Construct collectors draw out that presence and use it to gain unlikely power in the
battlefield.

## Constructed Focus (Su) {#constructed-focus}

At 3rd level, a construct collector can harvest components from destroyed constructs to fuel his
implements. Harvesting a component takes 1 minute. A construct collector can harvest a number of
active components equal to his Intelligence modifier per day. An active component is infused with 1
point of generic mental focus, which the construct collector can expend to activate any focus power
at that power's normal cost, as opposed to the increased cost normally associated with generic
mental focus. This otherwise functions as expending focus saved inside a construct collector's body.
Once this mental focus is expended, the component becomes inactive and is useless. An unused
component does not lose its mental focus, even after a construct collector refreshes his mental
focus. A construct collector can initially have only one active component at a time. He can have two
active components at a time at 9th level and three active components at a time at 15th level.

This replaces the focus power selected at 3rd level, 9th level, and 15th level.

## Repower Construct (Su) {#repower-construct}

At 8th level, a construct collector can use his mental focus to restore and gain control of a
construct. As an immediate action, he can expend a number of points of generic mental focus (minimum
2 points) to prevent a construct within 30 feet from becoming destroyed when reduced to 0 or fewer
hit points. The construct immediately regains a number of hit points equal to half of the construct
collector's current hit points (minimum 1). The construct follows all of the construct collector's
orders until the end of the collector's next turn or until reduced to 0 or fewer hit points.
Afterwards, the construct is completely destroyed and cannot be repowered again, even by another
construct collector. At 12th level, the construct is instead completely destroyed after a number of
rounds equal to the number of points of generic mental focus expended. At 16th level, the construct
is instead completely destroyed after a number of minutes equal to the number of points of generic
mental focus expended.

This replaces magic circles, outside contact, binding circles, and fast circles.
