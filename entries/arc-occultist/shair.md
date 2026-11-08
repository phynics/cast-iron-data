+++
id = "ref/arc-occultist/shair"
kind = "archetype"
title = "Sha'ir"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shair", path = "json/archetypes_occultist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/occultist" },
]

[fields]
kind = "archetype"
replaces = ["Implements", "Magic item skill", "object reading", "Aura sight"]
alters = ["Mental focus", "spellcasting", "implement mastery", "Outside contact"]
+++

**Sources:** Occult Adventures pg 102\
Sha'irs delve into the occult not through power over objects but instead via their connection with
minor servitor genies from the elemental planes. A sha'ir's jin is both a precious ally and a living
implement for its master.

**Jin (Su)**

**Action:** Ability

**Alters:** Mental focus, spellcasting, implement mastery

**At 14th Level:** The sha'ir contacts a third jin.

**At 20th Level:** A sha'ir selects one of her jin and chooses one of its two schools instead of
selecting an implement for _implement mastery._

**At 6th Level:** The sha'ir learns how to contact a second jin.

**Gained:** At 1st Level

**Replaces:** Implements

**Special:** If one of her jin is slain, the sha'ir is treated as if she didn't have the appropriate
implement to cast the spells associated with that jin. The sha'ir can replace the slain jin the
following morning by expending 1 point of mental focus in a special ritual that takes 1 hour to
perform.

A sha'ir learns how to contact a jin - a minor, insubstantial genie that makes its home on the
elemental planes. She learns how to contact more jin as she gains levels. Each of these jin is
connected to one of the eight schools of magic, just like an occultist
[implement](ref/ability/implements), but also to the [air](ref/arcaneschool/air),
[earth](ref/arcaneschool/earth), [fire](ref/arcaneschool/fire), or [water](ref/arcaneschool/water)
school. Each jin works like a living implement for both of its schools. To provide the implement
component for a spell or focus power, a jin must be within 30 feet of its master.

The elemental schools don't have focus powers or resonant powers. Instead, the sha'ir considers all
wizard spells of 6th level and lower from the lists corresponding to her jin's elemental schools to
be on her occultist spell list. In addition, she adds additional spells to her list of spells known.
For every spell level she can cast, she adds one spell from each jin's elemental school and one
spell from each jin's non-elemental school.

A jin in its natural form has the base statistics of a Small [elemental](ref/family/elemental) of
the chosen type with the [young](ref/template/young) simple template and without the _air mastery,
burn, drench, earth glide, earth mastery, vortex, water mastery,_ or
_[whirlwind](ref/spell/whirlwind)_ abilities.

**Augment Jin (Sp, Su)**

**At 10th Level:** The cost of giving a jin the statistics of a Medium elemental decreases to 1
point of mental focus, and the sha'ir can give a jin all the statistics of a Large elemental for 2
points of mental focus.

**At 12th Level:** The cost of giving a jin the statistics of a Large elemental decreases to 1 point
of mental focus and the sha'ir can give a jin the statistics of a Huge elemental for 2 points of
mental focus.

**At 14th Level:** The cost of giving a jin the statistics of a Huge elemental decreases to 1 point
of mental focus and the sha'ir can give a jin the statistics of a greater elemental for 2 points of
mental focus.

**At 16th Level:** The sha'ir can give a jin the statistics of an elder elemental for 3 points of
mental focus.

**At 8th Level:** She can instead expend 2 points of mental focus to give one of her jin all the
statistics of a Medium elemental.

**At 2nd Level:** A sha'ir's jin uses its master's base saving throws if they are better than its
own, and it uses either its own hit point total or 1/2 its master's hit points, whichever is higher.

**At 4th Level:** A sha'ir can concentrate for 1 full round and expend 1 point of mental focus
stored in a jin to grant that jin all the statistics of a Small elemental of its type for 1 round
per occultist level (this includes gaining any of the following abilities, if applicable: _air
mastery, burn, drench, earth glide, earth mastery, vortex, water mastery,_ and
_[whirlwind](ref/spell/whirlwind)_).

**Replaces:** Magic item skill, object reading

**Manifest Jin (Su)**

**Ability:** The sha'ir can designate one of her jin and manifest its powers, allowing it to count
as a Small elemental at all times, as if using _augment jin_ to augment it to a Small elemental but
with a permanent duration.

**Gained:** At 7th Level

**Replaces:** Aura sight

**Special:** By concentrating for 1 full round, she can change which of her jin she manifests in
this way.

**Jin Spy (Su)**

**Ability:** When a sha'ir gains her _outside contact_ ability, instead of learning the true names
of outsiders, she can ask one or more of her jin to perform tasks. She chooses from the same tasks
listed under _outside contact_ (as appropriate to her occultist level). This doesn't require
negotiation or gifts, but the jin is not available to the sha'ir during the time it spends
performing these tasks.

**Alters:** Outside contact

**Gained:** At 8th Level
