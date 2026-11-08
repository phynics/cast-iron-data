+++
id = "ref/arc-druid/pack-lord"
kind = "archetype"
title = "Pack Lord"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pack_lord", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]

[fields]
kind = "archetype"
replaces = ["Nature bond", "The 6th-level additional use of wild shape"]
+++

**Sources:** Ultimate Magic pg 38\
Some druids bond with many animal companions rather than just one, achieving a level of communion
rare even in druidic circles and leading their pack brothers and pack sisters with total authority.

**Pack Bond (Ex)**

**Action:** Special

**Choice:** A pack lord druid may not select a domain and must choose an animal companion.

**Passive:** The druid gains a +2 bonus on _wild empathy_ and Handle Animal checks made regarding
her animal companion.

**Replaces:** Nature bond

The pack lord may have more than one animal companion, but she must divide up her effective druid
level between her companions to determine the abilities of each companion. For example, a 4th-level
pack lord can have one 4th-level companion, two 2nd-level companions, or one 1st-level and one
3rd-level companion.

Each time a pack lord's druid level increases, she must decide how to allocate the increase among
her animal companions (including the option of adding a new 1st-level companion). Once a druid level
is allocated to a particular companion, it cannot be redistributed while that companion is in the
pack lord's service (she must release the companion or wait until the companion dies to allocate its
levels to another companion, which she can do the next time she prepares spells). The _share spells_
animal companion ability only applies to one animal companion at a time - the pack lord cannot use
it to cast a one-target spell and have it affect all of her animal companions.

**Improved Empathic Link (Su)**

**Ability:** The pack lord gains an _empathic link_ with all of her animal companions. This
functions like an empathic link with a [familiar](ref/sidekick/familiar).

**Replaces:** The 6th-level additional use of _wild shape_

**Swift:** The pack lord can shift her perception to one of her companions, allowing her to
experience what it sees, hears, and so on. She can maintain this connection as long as she likes (as
long as the companion is within 1 mile) and end it as a **free action**. The druid can only use this
ability on one companion at a time, and cannot see, hear, or smell with her own body while
maintaining this connection.
