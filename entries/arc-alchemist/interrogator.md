+++
id = "ref/arc-alchemist/interrogator"
kind = "archetype"
title = "Interrogator"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "interrogator", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Intrigue pg 18\
An interrogator extracts vital information from reluctant individuals using alchemical and
traditional methods.

**Gained class skills:** intm, sm

**Injections (Su)**

**Gained:** At 1st Level

**Replaces:** Bomb

**Special:** An injection that hasn't been administered becomes inert if it leaves the
interrogator's possession, reactivating as soon as it returns to his possession. The penalties from
multiple injections don't stack, nor do the penalties from injections stack with penalties from a
[mesmerist's](ref/class/mesmerist) stare or a witch's [evil eye](ref/hex/evil-eye) hex. Injections
are mind-affecting poison effects.

**Standard:** Using an injection is a standard action that requires a melee touch attack. If the
attack hits, the target of an injection takes a -2 penalty on its Will saving throws for a number of
minutes equal to half the interrogator's class level (minimum 1). If the interrogator is also using
a _serum_ with this injection, the penalty on Will saves applies to any save against the _serum._ If
the melee touch attack fails, the injection isn't delivered but can still be used again - once
activated, it remains potent for 1 day.

**Usage:** An interrogator uses his skill with alchemy to create injections. Each day, an
interrogator can create a number of injections equal to his alchemist level + his Intelligence
modifier. It takes 1 hour to create the injections. An injection is inert until the interrogator
attempts to use it.

**Usage:** An interrogator uses his skill with alchemy to create injections. Each day, an
interrogator can create a number of injections equal to his alchemist level + his Intelligence
modifier. It takes 1 hour to create the injections. An injection is inert until the interrogator
attempts to use it.

**Serums (Su)**

**Ability:** An interrogator knows one serum at 1st level and can learn another serum in place of a
discovery. A creature can be under the effect of only a single serum at a time - with the exception
of _memory modification_ serum - with any further serums on the same creature replacing the old
serum.

**Flavor:** An interrogator augments his ability to influence others through supplemental serums.

**Gained:** At 1st Level

**Replaces:** Mutagen, persistent mutagen

**Special:** The save DCs of serums are equal to 10 + [half](ref/misc/fractions-and-rounding) the
interrogator's alchemist level + his Intelligence modifier. Unless otherwise noted, a creature that
succeeds on its saving throw against a serum is immune to that serum's effects for 24 hours. An
interrogator can never gain any sort of mutagen or cognatogen, even from a discovery or another
class.

**Swift:** An interrogator prepares his serums at the same time as his injections and he can apply
them to any injection as a **swift action** before he makes the attack roll for the injection.

**Charming**

**Ability:** The injected creature must succeed at a Will save or treat the interrogator favorably,
as if affected by [charm person](ref/spell/charm-person) with a caster level equal to the
interrogator's alchemist level.

**At 8th Level:** This serum acts as [charm monster](ref/spell/charm-monster).

**Compliance**

**Passive:** On a failed Will save, the subject of this injection is affected by a
[suggestion](ref/spell/suggestion) with a caster level equal to the interrogator's alchemist level.

**Prereq:** 8th-level interrogator

**Confusion**

**Passive:** On a failed Will save, the injected creature is [confused](ref/misc/confused) for 1
round per alchemist level the interrogator has.

**Prereq:** 6th-level interrogator

**Hypnosis**

**Passive:** The injected creature must succeed at a Will save or become
[fascinated](ref/misc/fascinated) for 1 round per alchemist level the interrogator has.

**Memory Modification**

**Passive:** On a failed Will save, the target of this serum is affected by
[modify memory](ref/spell/modify-memory) at a caster level equal to the interrogator's alchemist
level.

**Prereq:** 12th-level interrogator

**Paralytic**

**Passive:** On a failed Will save, the injected creature is affected by
[hold person](ref/spell/hold-person) with a caster level equal to the interrogator's alchemist
level.

**Prereq:** 8th-level interrogator

**Truth**

**Passive:** A creature injected with a truth serum must succeed at a Will save or be compelled to
answer the interrogator's questions truthfully. The interrogator can ask one question per 2
alchemist levels (minimum 1). Answers might be brief, cryptic, or repetitive, especially if the
injected creature is unfriendly, but they aren't false. If a creature has been subjected to a truth
serum within the past week, whether it succeeded at or failed its save, any new serum fails.
