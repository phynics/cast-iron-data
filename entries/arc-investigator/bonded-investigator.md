+++
id = "ref/arc-investigator/bonded-investigator"
kind = "archetype"
title = "Bonded Investigator"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bonded_investigator", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]

[fields]
kind = "archetype"
replaces = ["Poison lore", "poison resistance", "poison immunity", "Studied strike damage gained at 4th level", "Investigator talent gained at 7th level"]
alters = ["Studied strike"]
+++

**Sources:** Inner Sea Intrigue pg 38\
Bonded investigators use intelligent familiars to assist them in their investigations. They are
common in the Inner Sea region's bustling cities, where a rat, cat, raven, or another small animal
can go largely unnoticed.

**Familiar (Ex)**

**Ability:** A bonded investigator gains a [familiar](ref/ability/familiars) to aid him. This
[familiar](ref/sidekick/familiar) functions as the [wizard](ref/class/wizard) arcane bond class
feature, using the bonded investigator's class level to determine the familiar's special abilities.
The bonded investigator's extracts are considered spells for the purposes of familiar abilities like
_share spell_ and _deliver touch spells._

**Gained:** At 2nd Level

**Replaces:** Poison lore, poison resistance, poison immunity

**Inspired Familiar (Ex)**

**Ability:** A bonded investigator's familiar becomes a cunning assistant to the investigator. The
familiar can access the investigator's _inspiration pool_ to augment its own actions; the use of
_inspiration_ is deducted from the investigator's number of daily uses as normal. The familiar can
use the _inspiration_ ability (and gains the increased benefits of investigator talents that affect
the bonus dice used in this ability) but cannot expend uses of _inspiration_ for other purposes.

**Gained:** At 4th Level

**Replaces:** Studied strike damage gained at 4th level

**Studied Strike (Ex)**

**Ability:** A bonded investigator gains _studied strike_ +1d6.

**Alters:** Studied strike

**Gained:** At 6th Level

At 10th level: This damage +2d6.

At 14th level: This damage +3d6.

At 18th level: This damage +4d6.

**Improved Familiar (Ex)**

**Ability:** A bonded investigator gains the [Improved Familiar](ref/feat/improved-familiar) feat as
a bonus feat, treating his investigator level as his arcane caster level for the purposes of
determining what familiars are available to him.

**Gained:** At 7th Level

**Replaces:** Investigator talent gained at 7th level

**Investigator Talents:** The following investigator talents complement the bonded investigator
archetype: [effortless aid](ref/invtalent/effortless-aid),
[perceptive tracking](ref/invtalent/perceptive-tracking),
[tenacious inspiration](ref/invtalent/tenacious-inspiration), and
[unconventional inspiration](ref/invtalent/unconventional-inspiration).
