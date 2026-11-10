+++
id = "ref/arc-hunter/packmaster"
kind = "archetype"
title = "Packmaster"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "packmaster", path = "json/archetypes_hunter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/hunter" },
]
[[sources]]
publication = "advanced-class-guide"
page = "96"

[fields]
kind = "archetype"
replaces = ["Animal companion", "Animal focus", "Second animal focus", "Master hunter"]
alters = ["Precise companion", "woodland stride", "teamwork feats", "Teamwork feats"]
replaces_features = ["animal-companion", "animal-focus", "second-animal-focus", "master-hunter"]
alters_features = ["precise-companion", "woodland-stride"]
+++

Some hunters form bonds with packs of well-trained creatures. Whether such a hunter is a northern
berserker running with a pack of timber wolves or a savage warrior dashing through the jungle
alongside her herd of dimetrodons, the packmaster revels in the thrill of the hunt and the glory of
the kill. A packmaster is more comfortable in groups than alone, and although her animal companions
may be weaker than a typical hunter's, what they lack in strength they make up for in numbers.

**Pack Bond (Ex)**

**Action:** Ability

**Alters:** Precise companion, woodland stride, teamwork feats

**Replaces:** Animal companion

A packmaster can have more than one animal companion, but she must divide her effective druid level
between her companions to determine the abilities of each one. For example, a 4th-level packmaster
can have one 4th-level animal companion, two 2nd-level companions, one 3rd-level companion and one
1st-level companion, or four 1st-level companions.

When a packmaster gains a level, she must decide how to allocate the increase among her animal
companions, including whether or not to add a new 1st-level companion. Once a hunter level is
allocated to a particular companion, it cannot be redistributed while that companion is in the
packmaster's service. She must release the companion or wait until the companion dies to allocate
its levels to another companion, which she can then do the next time she refreshes her spell slots
for the day. The _share spells_ animal companion ability applies to only one animal companion at a
time - the packmaster cannot use it to cast a spell that affects only a single target and have the
spell affect all of her animal companions.

A packmaster's _precise companion, woodland stride,_ and _teamwork feats_ apply to only one of her
animal companions at a time. (For example, a packmaster can apply _precise companion_ to one
companion, _woodland stride_ to another, and a given teamwork feat to a third, but cannot apply any
of those to two animal companions at once.) As a **swift action**, she can change which companion
gains any or all of these benefits.

**Pack Focus (Su)**

**Ability:** This ability functions like [animal focus](ref/ability/animal-foci), with the following
exceptions. A packmaster can apply her animal aspect to only one of her animal companions at a time
without it counting against the number of minutes per day she can use that ability. When using
_animal focus_ on herself or her other animal companion, the ability counts against her minutes per
day as normal.

**Replaces:** Animal focus

**Special:** She can have only two animal aspects in effect at a time - one that counts against her
minutes per day and one that doesn't - and they can't both target the same companion. Unless both
her companions are dead, the hunter can't apply the companion's aspect to herself (and thereby gain
the benefit of its unlimited duration).

**Teamwork Feat (Ex)**

**Ability:** At any level at which a packmaster would gain a bonus teamwork feat, she can instead
increase the number of her animal companions that gain the benefits of her _precise companion,
woodland stride,_ and _teamwork feats_ by 1. She can select this ability multiple times.

**Alters:** Teamwork feats

**Gained:** At 3rd Level

**Second Pack Focus (Su)**

**Ability:** The hunter gains an ability that functions like the _second animal focus,_ but the
hunter can either assign each companion one aspect each or assign both aspects to the same
companion. The foci on the companions don't need to be the same, nor do they need to be the same as
the one assigned to the packmaster.

**Gained:** At 8th Level

**Replaces:** Second animal focus

**Master of the Pack (Ex)**

**Ability:** Each day when a packmaster gains new spells for the day, she chooses one _animal focus_
to be active on herself or one of her animal companions for the entire day (if all of her animal
companions are dead, she instead chooses two animal foci to be active on herself for the entire
day). This focus is in addition to her _pack focus_ class ability.

**Gained:** At 20th Level

**Passive:** A packmaster and her animal companions can always move at full speed while using
Survival to follow tracks without penalty.

**Replaces:** Master hunter
