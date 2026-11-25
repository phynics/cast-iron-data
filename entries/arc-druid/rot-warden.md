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
features = [
  { anchor = "invoke-decay" },
  { anchor = "nature-bond" },
  { anchor = "vermin-empathy", level = 1 },
  { anchor = "swarmcaller", level = 3 },
  { anchor = "enduring-druid", level = 4 },
  { anchor = "wild-shape", level = 6 },
]
trades = [
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["vermin-empathy"] },
  { replaces = "Trackless step", feature = "trackless-step", by = ["swarmcaller"] },
  { replaces = "venom immunity", feature = "venom-immunity", by = ["swarmcaller"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["enduring-druid"] },
  { replaces = "Wild shape", feature = "wild-shape", by = ["wild-shape"] },
  { alters = "Spontaneous casting", feature = "spontaneous-casting", by = ["invoke-decay"] },
  { alters = "Nature bond", feature = "nature-bond", by = ["nature-bond"] },
]
+++

Harbingers of decay, rot wardens live in damp lands where insects and rot break down the dead to
feed the living. They see in the process of rot the beauty of nature's capacity to recycle and
repurpose material into something wondrous and new.

## Invoke Decay (Su) {#invoke-decay}

A rot warden can channel stored spell energy into specific spells he hasn't prepared ahead of time.
He can "lose" a prepared spell in order to cast the following spells at the indicated levels:
1st—_decompose corpse_, 2nd—_warp wood_, 3rd—_fungal infestation_, 4th—_explosion of rot_,
5th—_insect plague_, 6th—_swarm skin_, 7th—_creeping doom_, 8th—_horrid wilting_, 9th—_massacre_.

This alters spontaneous casting.

## Nature Bond {#nature-bond}

A rot warden who chooses a cleric domain as his nature bond must choose from the
[Destruction](ref/domain/destruction), [Erosion](ref/druiddomain/erosion), Repose, or
[Vermin](ref/druiddomain/vermin) domains.

This alters nature bond.

## Vermin Empathy (Su) {#vermin-empathy}

A rot warden can improve the attitude of vermin as a normal druid can with animals. Vermin have a
starting attitude of unfriendly. The rot warden can also improve the attitude of vermin swarms, but
he takes a -4 penalty on the check unless the swarm consists of the same kind of vermin as his
vermin companion or his current wild shape.

This replaces wild empathy.

## Swarmcaller (Sp) {#swarmcaller}

At 3rd level, a rot warden can summon a swarm of vermin once per day as a standard action. This
functions like _[summon swarm](ref/spell/summon-swarm)_, except the swarm the rot warden summons
must be a [cockroach](ref/monster/cockroach-cockroach-swarm),
[locust](ref/monster/locust-locust-swarm), or [spider swarm](ref/monster/spider-spider-swarm). If he
uses this ability during the surprise round of combat, nearby animals and vermin become hushed until
the first round of combat ends; during this surprise round and first round of combat,
[flat-footed](ref/rule/flat-footed) creatures also gain the [shaken](ref/misc/shaken) condition
(this doesn't stack with other fear effects). At 9th level, he adds
[army ant](ref/monster/ant-army-ant-swarm), [centipede](ref/monster/centipede-centipede-swarm), and
[wasp swarms](ref/monster/wasp-wasp-swarm) to the list of swarms he can call with this ability.

This replaces trackless step and venom immunity.

## Enduring Druid (Su) {#enduring-druid}

At 4th level, a rot warden gains a +4 bonus on saving throws against attacks and special abilities
of vermin and swarms with the vermin type. This bonus also applies on saving throws against effects
that would age or decay the rot warden or his equipment.

This replaces resist nature's lure.

## Wild Shape {#wild-shape}

A rot warden gains this ability at 6th level, except his effective druid level is his druid
level - 2. He cannot take the form of an elemental.

At 8th level, a rot warden can assume the form of a Small or Medium vermin as if using
_[vermin shape I](ref/spell/vermin-shape-1)_. At 10th level, the rot warden can assume the shape of
a Tiny or Large vermin as if using _[vermin shape II](ref/spell/vermin-shape-2)_. At 12th level, he
can take the form of a Huge vermin as if using _vermin shape III_.

This alters wild shape.
