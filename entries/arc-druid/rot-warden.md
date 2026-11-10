+++
id = "ref/arc-druid/rot-warden"
kind = "archetype"
title = "Rot Warden"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Rot%20Warden"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rot_warden", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "49"

[fields]
kind = "archetype"
replaces = ["Wild empathy", "Trackless step", "venom immunity", "Resist nature's lure", "Wild shape"]
alters = ["Spontaneous casting", "Nature bond"]
replaces_features = ["wild-empathy", "trackless-step", "venom-immunity", "resist-nature-s-lure", "wild-shape"]
alters_features = ["spontaneous-casting", "nature-bond"]
+++

Harbingers of decay, rot wardens live in damp lands where insects and rot break down the dead to
feed the living. They see in the process of rot the beauty of nature's capacity to recycle and
repurpose material into something wondrous and new.

**Invoke Decay (Su)**

**Ability:** A rot warden can channel stored spell energy into specific spells he hasn't prepared
ahead of time. He can &quot&lose&quot& a prepared spell in order to cast the following spells at the
indicated spell levels.

**Alters:** Spontaneous casting

**Spells:** Decompose corpse

**Spells:** Warp wood

**Spells:** Fungal infestation

**Spells:** Explosion of rot

**Spells:** Insect plague

**Spells:** Swarm skin

**Spells:** Creeping doom

**Spells:** Horrid wilting

**Spells:** Massacre

**Nature Bond**

**Alters:** Nature bond

**Choice:** A rot warden who chooses a cleric domain as his nature bond must choose from the
[Destruction](ref/domain/destruction), [Erosion](ref/druiddomain/erosion), Repose, or
[Vermin](ref/druiddomain/vermin) domains.

**Vermin Empathy (Su)**

**Ability:** A rot warden can improve the attitude of vermin as a normal druid can with animals.
Vermin have a starting attitude of unfriendly. The rot warden can also improve the attitude of
vermin swarms, but he takes a -4 penalty on the check unless the swarm consists of the same kind of
vermin as his vermin companion or his current _wild shape._

**Replaces:** Wild empathy

**Swarmcaller (Sp)**

**At 9th Level:** He adds [army ant](ref/monster/ant-army-ant-swarm),
[centipede](ref/monster/centipede-centipede-swarm), and [wasp swarms](ref/monster/wasp-wasp-swarm)
to the list of swarms he can call with this ability.

**Gained:** At 3rd Level

**Replaces:** Trackless step, venom immunity

**Standard:** A rot warden can summon a swarm of vermin once per day. This functions like
[summon swarm](ref/spell/summon-swarm), except the swarm the rot warden summons must be a
[cockroach](ref/monster/cockroach-cockroach-swarm), [locust](ref/monster/locust-locust-swarm), or
[spider swarm](ref/monster/spider-spider-swarm). If he uses this ability during the surprise round
of combat, nearby animals and vermin become hushed until the first round of combat ends; during this
surprise round and first round of combat, [flat-footed](ref/rule/flat-footed) creatures also gain
the [shaken](ref/misc/shaken) condition (this doesn't stack with other fear effects).

**Enduring Druid (Su)**

**Gained:** At 4th Level

**Passive:** A rot warden gains a +4 bonus on saving throws against attacks and special abilities of
vermin and swarms with the vermin type. This bonus also applies on saving throws against effects
that would age or decay the rot warden or his equipment.

**Replaces:** Resist nature's lure

**Wild Shape**

**Ability:** A rot warden gains _wild shape,_ except his effective druid level is his druid
level - 2. He cannot take the form of an elemental.

**At 10th Level:** The rot warden can assume the shape of a Tiny or Large vermin as if using
[vermin shape II](ref/spell/vermin-shape-2).

**At 12th Level:** He can take the form of a Huge vermin as if using vermin shape III.^1^

**At 8th Level:** A rot warden can assume the form of a Small or Medium vermin as if using
[vermin shape I](ref/spell/vermin-shape-1).

**Gained:** At 6th Level

**Replaces:** Wild shape

^No such spell was ever published. A similar spell could be made based on \[beast shape
III^(spell/beast\_shape\_iii) and _[vermin shape II](ref/spell/vermin-shape-2)_ - consult your
GM.\]\{from=1\}
