+++
id = "ref/arc-magus/eldritch-scion"
kind = "archetype"
title = "Eldritch Scion"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "eldritch_scion", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]
[[sources]]
publication = "advanced-class-guide"
page = "104"

[fields]
kind = "archetype"
replaces = ["Spells", "Spell recall", "Arcane pool", "Knowledge pool"]
alters = ["Spell combat", "Improved spell combat", "Greater spell combat"]
replaces_features = ["spells", "spell-recall", "arcane-pool", "knowledge-pool"]
alters_features = ["spell-combat", "improved-spell-combat", "greater-spell-combat"]
+++

Unlike typical magi, eldritch scions do not study tomes of magic or spend time learning to combine
martial and magical skills. Rather, eldritch scions find that their spells and abilities come to
them instinctively.

**Spells**

**Action:** Ability

**Replaces:** Spells

An eldritch scion casts arcane spells drawn from the magus spell list. He can cast any spell he
knows without preparing it ahead of time. To learn or cast a spell, an eldritch scion must have a
Charisma score equal to at least 10 + the spell's level. The DC for a saving throw against an
eldritch scion's spell is 10 + the spell's level + the eldritch scion's Charisma modifier. An
eldritch scion can cast only a certain number of spells of each spell level per day. His base daily
spell allotment is the same as a bard of the same level. In addition, he receives bonus spells per
day if he has a high Charisma score.

An eldritch scion's selection of spells is limited. He has the same number of spells known as a bard
of the same level, and can choose new spells to replace old ones at 5th level and every 3 class
levels after that, just as a bard does. See the [bard](ref/class/bard) for more information on
swapping spells known.

**Bloodline**

**Ability:** An eldritch scion gains a [bloodrager bloodline](ref/ability/bloodrager-bloodlines).
The bloodline is selected at 1st level, and this choice cannot be changed. An eldritch scion's
effective bloodrager level for his bloodline abilities is equal to his eldritch scion level. He does
not gain any bonus feats, and he gains bonus spells from his bloodline at different levels (see the
_bonus spells_ class feature below). To use any ability that normally functions when in a bloodrage,
an eldritch scion must spend a point from his _eldritch pool_ (see below).

**Replaces:** Spell recall

**Special:** If an eldritch scion takes levels in another class that grant a bloodline, the
bloodlines must be the same type, even if that means that the bloodline of one of the classes must
change. Subject to GM discretion, an eldritch scion can change his former bloodline to make them
conform.

**Eldritch Pool (Su)**

**Action:** Ability

**At 4th Level:** An eldritch scion can also use his _eldritch pool_ as an _arcane pool,_ gaining
all the benefits listed with the magus's _arcane pool_ class feature.

**Replaces:** Arcane pool

**Special:** Abilities that modify _arcane pool_ also modify _eldritch pool._

An eldritch scion gains an _eldritch pool_ of personal magical energy, equal to 1/2 his magus level
(minimum 1) + his Charisma modifier. As a **swift action**, he can spend a point of eldritch energy
to enter a state of mystical focus for 2 rounds. This allows him to use abilities from his
bloodrager bloodline as though he were in a bloodrage, though he gains none of the other benefits or
drawbacks of bloodraging.

Additionally, any magus's class feature or spell from the magus spell list that normally uses a
calculation based on Intelligence is instead based on Charisma for an eldritch scion. For example,
an eldritch scion with the [arcane accuracy](ref/arcana/arcane-accuracy) magus arcana grants himself
an insight bonus on attacks equal to his Charisma bonus, not his Intelligence bonus. This has no
effect on the eldritch scion's skills or skill points.

**Spell Combat (Ex)**

**Ability:** An eldritch scion can only use _spell combat_ while in a state of mystic focus (see
_eldritch pool,_ above).

**Alters:** Spell combat

**At 8th Level:** An eldritch scion can use _spell combat_ at any time.

**Bonus Spells**

**Ability:** An eldritch scion gains the bonus spell from his bloodrager bloodline that is normally
gained at 10th level.

**Gained:** At 7th Level

**Replaces:** Knowledge pool

**Improved Spell Combat (Ex)**

**Ability:** An eldritch scion gains the _improved spell combat_ class feature.

**Alters:** Improved spell combat

**Gained:** At 14th Level

**Greater Spell Combat (Ex)**

**Ability:** An eldritch scion gains the _greater spell combat_ class feature.

**Alters:** Greater spell combat

**Gained:** At 18th Level
