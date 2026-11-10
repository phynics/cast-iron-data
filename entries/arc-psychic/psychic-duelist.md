+++
id = "ref/arc-psychic/psychic-duelist"
kind = "archetype"
title = "Psychic Duelist"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "psychic_duelist", path = "json/archetypes_psychic.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/psychic" },
]
[[sources]]
publication = "occult-adventures"
page = "107"

[fields]
kind = "archetype"
replaces = ["4th-level discipline spell", "7th-level phrenic amplification", "Telepathic bond", "Telepathy"]
alters = ["Phrenic amplifications"]
replaces_features = ["telepathic-bond", "telepathy"]
alters_features = ["phrenic-amplifications"]
+++

Psychic duelists hone their mental powers for combat, much as warriors do with their blades. They
specialize in [psychic duels](ref/rule/psychic-duels), perfecting their thought-form creatures into
mighty weapons.

**Psychic Duel Acumen (Ex)**

**Ability:** A psychic duelist adds [instigate psychic duel](ref/spell/instigate-psychic-duel) to
her list of spells known, and the save DC of any
_[instigate psychic duel](ref/spell/instigate-psychic-duel)_ spell she casts increases by 1.

**At 6th Level:** She can also expend any unused psychic spell slot of 3rd level or higher to cast
_[instigate psychic duel](ref/spell/instigate-psychic-duel)._ If she does so, she uses the level of
the spell slot expended to determine the Will save DC.

**At 7th Level:** When the psychic duelist sacrifices points from her phrenic pool to generate
_manifestation points_ (see below) for an offensive manifestation, she uses d8s for damage dice
instead of d4s.

**Gained:** At 4th Level

**Replaces:** 4th-level discipline spell

**Manifestation Amplifications**

**Ability:** A psychic duelist gains a _manifestation amplification_ instead of a phrenic
amplification; thereafter, whenever the psychic duelist gains a phrenic amplification, she can
select either a phrenic amplification or a _manifestation amplification._

**Alters:** Phrenic amplifications

**Info:** A _manifestation amplification_ functions for a manifestation as a phrenic amplification
does for a spell, with the same restrictions. The manifestation being amplified is called the linked
manifestation. Phrenic pool points spent toward _manifestation amplifications_ are separate from
points sacrificed to generate _manifestation points._ For example, a psychic duelist capable of
casting 4th-level spells (with a maximum of 4 _MP_ per manifestation) could turn 4 points from her
phrenic pool into _MP_ and spend 2 points on a _manifestation amplification,_ expending a total of 6
points from her phrenic pool.

**Gained:** At 7th Level

**Replaces:** 7th-level phrenic amplification

**Extended Effect (Ex)**

**Ability:** The psychic duelist can spend points from her phrenic pool to increase the duration of
a condition by 1 round per point spent. She can spend a maximum of 1 phrenic pool point in this way.

**Special:** If the target succeeds at its saving throw, this amplification has no effect (though
the points are still lost). This amplification can be linked only to offensive manifestations that
impose conditions.

At 11th level: This maximum 2.

At 15th level: This maximum 3.

At 19th level: This maximum 4.

**Faithful Creature (Ex)**

**Ability:** When she manifests a thought-form creature, the psychic duelist can spend 1 point from
her phrenic pool to give that creature the ability to persist even if it doesn't attack. She can
concentrate to maintain the creature as a **swift action** instead of as a full-round action, but
the creature can attack only if the psychic duelist concentrates as a **full-round action**. In
addition, the psychic backlash damage from that thought-form creature is halved.

**Special:** This amplification can be linked only to thought-form creature manifestations.

**Punishing Thought-form (Ex)**

**Ability:** The psychic duelist can spend 1 point from her phrenic pool to increase the damage die
size of an offensive manifestation by one step (d4 to d6, d6 to d8, or d8 to d10).

**Special:** This amplification can be linked only to offensive manifestations.

**Reciprocal Defense (Su)**

**Ability:** The psychic duelist can spend 1 point from her phrenic pool when using a defensive
manifestation to improve her defenses in the real world as well. Her physical body gains a +2
insight bonus to AC for the number of rounds the defensive manifestation lasts, or for 1 round if
the manifestation doesn't have a duration.

**Special:** This amplification can be linked only to defensive manifestations.

At 11th level: This bonus +3.

At 15th level: This bonus +4.

**Thought Made Real (Su)**

**Ability:** A psychic duelist can bring offensive manifestations directly into her foes' minds,
attacking with them without entering a psychic duel. When doing so, she can generate _manifestation
points_ only by sacrificing a spell, not through any other methods. Using an offensive manifestation
in this way functions as casting a spell with a **full-round action** casting time. Conditions
imposed by these offensive manifestations last for their full duration, even though the target isn't
in a psychic duel. The psychic duelist can use _manifestation amplifications_ on offensive
manifestations created this way. Such offensive manifestations can't affect thought-form creatures.

**Gained:** At 9th Level

**Replaces:** Telepathic bond

**Special:** This is a mind-affecting illusion (phantasm) effect. A thought-form creature manifested
in this way is visible only to its target.

**Expert Manifester (Ex)**

**Ability:** A psychic duelist doesn't have to expend as many resources to create manifestations.
She gains 1 additional _MP_ each time she creates a psychic manifestation, in addition to the _MP_
she gains by sacrificing resources. This doesn't increase the maximum number of points she can spend
per manifestation, but does allow her to create a manifestation costing 1 _MP_ without sacrificing
any resources.

**Gained:** At 17th Level

**Replaces:** Telepathy
