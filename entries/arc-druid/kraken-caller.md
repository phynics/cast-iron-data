+++
id = "ref/arc-druid/kraken-caller"
kind = "archetype"
title = "Kraken Caller"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Kraken%20Caller"
source_ids = ["dirty-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "kraken_caller", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "dirty-tactics-toolbox"
page = "16"

[fields]
kind = "archetype"
replaces = ["Woodland stride", "Trackless step", "Resist nature's lure", "A thousand faces"]
alters = ["Bonus languages", "Wild shape"]
replaces_features = ["woodland-stride", "trackless-step", "resist-nature-s-lure", "a-thousand-faces"]
alters_features = ["bonus-languages", "wild-shape"]
+++

Some druids draw upon power irreverently stolen from one of the most dangerous creatures of the
depths: the kraken.

**Call of the Waves (Ex)**

**Info:** A kraken caller must choose [Besmara](ref/faith/besmara) as her deity. If she ever changes
her deity, she loses this archetype and becomes a normal druid.

**Bonus Languages**

**Alters:** Bonus languages

**Info:** A kraken caller's bonus language options include Aquan instead of Sylvan.

**Dauntless Swimmer (Ex)**

**Ability:** A kraken caller can always take 10 on Swim checks, even if she is rushed or threatened.

**Gained:** At 2nd Level

**Replaces:** Woodland stride

**Hold Breath (Ex)**

**Ability:** A kraken caller can [hold her breath](ref/misc/hold-your-breath) for a number of
minutes equal to her Constitution score before she risks drowning.

**Gained:** At 3rd Level

**Replaces:** Trackless step

**Resist the Waves' Lure (Ex)**

**Gained:** At 4th Level

**Passive:** A kraken caller gains a +4 bonus on saving throws against the spell-like and
supernatural abilities of creatures with the aquatic subtype.

**Replaces:** Resist nature's lure

**Wild Shape (Su)**

**Action:** Ability

**Alters:** Wild shape

**At 10th Level:** A kraken caller can grow three additional tentacles.

**At 12th Level:** A kraken caller can grow four additional tentacles.

**At 6th Level:** A kraken caller can grow one additional tentacle.

**At 8th Level:** A krakan caller can grow two additional tentacles. As a **move action**, she can
retract or regrow any number of the additional tentacles, redistributing the mass of any retracted
tentacles. For every 2 retracted tentacles, she can increase the reach of the remaining tentacles by
5 feet (to a maximum of 15 feet), or increase the damage dealt by her tentacles as if she were
[one size category larger](ref/misc/damage-die-adjustments).

**Gained:** At 4th Level

A kraken caller's options for _wild shape_ are limited to animals with the aquatic or water subtype
or that have the amphibious special quality. The kraken caller can alternatively expend a daily use
of _wild shape_ to grow two tentacles out of her body while otherwise retaining her own form. This
effect lasts for 10 minutes per level, or until the kraken caller changes back.

The tentacles have a reach of 5 feet regardless of the kraken caller's size, and the kraken caller
can use them as secondary [natural attacks](ref/umr/natural-attacks) that deal 1d4 points of damage
(1d3 for a Small kraken caller). She also gains a racial bonus on Climb, Swim, and
[dirty trick](ref/rule/dirty-trick) combat maneuver checks equal to the number of tentacles grown.

While in this form, a kraken caller can expel a 10-foot-radius cloud of ink once per minute as a
**standard action**. This cloud provides [total concealment](ref/rule/concealment) in water and
persists for 1 round per level. The ink has no effect out of water.

**Beast of the Depths (Su)**

**Gained:** At 13th Level

**Passive:** A kraken caller gains a swim speed equal to her base land speed and can breathe water
as though affected by the spell [water breathing](ref/spell/water-breathing).

**Replaces:** A thousand faces
