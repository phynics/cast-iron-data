+++
id = "ref/arc-druid/eagle-shaman"
kind = "archetype"
title = "Eagle Shaman"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Eagle%20Shaman"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "eagle_shaman", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "advanced-players-guide"
page = "102"

[fields]
kind = "archetype"
replaces = ["Woodland stride", "Wild shape"]
alters = ["Nature bond", "Wild empathy"]
+++

A shaman with this totem calls upon the noble eagle, stern and proud, soaring high above the world
with keen and pitiless eyes that miss nothing.

**Nature Bond**

**Alters:** Nature bond

**Choice:** An eagle shaman who chooses an animal companion must select a
[bird (eagle)](ref/companion/bird). If choosing a domain, the eagle shaman must choose from the
[Air](ref/domain/air), [Animal](ref/domain/animal), Nobility, and [Weather](ref/domain/weather)
domains.

**Wild Empathy (Ex)**

**Ability:** An eagle shaman can use _wild empathy_ with birds as a **full-round action** with a +4
bonus.

**Alters:** Wild empathy

**Totem Transformation (Su)**

**Action:** Standard Action

**At 12th Level:** This becomes a **swift action**.

**At 5th Level:** The druid may select a new option: **Movement** (fly speed 30 ft. \[average\])

**At 7th Level:** This becomes a **move action**.

**Gained:** At 2nd Level

**Replaces:** Woodland stride

**Special:** This is a polymorph effect and cannot be used while the druid is using another
polymorph effect, such as _wild shape._

**Usage:** 1 minute/day per druid level; these minutes need not be consecutive, but must be spent in
1-minute increments

An eagle shaman may adopt an aspect of the eagle while retaining her normal form. The druid may
select from the following bonuses:

- **Senses** ([low-light vision](ref/rule/low-light-vision), +4 racial bonus to Perception)
- **[Natural weapons](ref/umr/natural-attacks)** (bite \[1d4\], 2 talons \[1d4\] for a Medium
  shaman)

While using _totem transformation,_ the eagle shaman may speak normally and can cast
[speak with animals](ref/spell/speak-with-animals) (birds only) at will.

**Totemic Summons (Su)**

**Gained:** At 5th Level

**Standard:** An eagle shaman may cast [summon nature's ally](ref/spell/summon-natures-ally) to
summon [eagles](ref/monster/eagle), [rocs](ref/monster/roc), and
[giant eagles](ref/monster/eagle-giant-eagle) (added to the 4th-level list), and these summoned
creatures gain [temporary hit points](ref/rule/temporary-hit-points) equal to her druid level. She
can apply the [young](ref/template/young) template to any eagle or roc to reduce the level of the
summoning spell required by one. She can also increase the level of summoning required by one in
order to apply either the [advanced](ref/template/advanced) or the [giant](ref/template/giant)
template, or increase it by two to apply both the advanced and giant templates.

**Wild Shape (Su)**

**Gained:** At 6th Level

**Passive:** An eagle shaman gains _wild shape,_ but the ability functions at her druid level - 2.
If she takes on the form of an eagle or roc, she instead uses her druid level + 2.

**Replaces:** Wild shape

**Special:** The lack of suitable giant bird stat blocks in official Paizo products hinders the
rules options for this archetype.

To remedy this problem, an eagle shaman druid can use _wild shape_ to take the form of a Medium
eagle (as if applying the giant creature simple template to a Small eagle), and can use _wild shape_
to take the form of a Huge roc (as if applying the young creature simple template to a Gargantuan
roc). Abilities of the assumed form are determined by which _[beast shape](ref/spell/beast-shape)_
spell the _wild shape_ ability functions as, as determined by the eagle shaman's effective druid
level.
