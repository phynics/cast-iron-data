+++
id = "ref/arc-mesmerist/chart-caster"
kind = "archetype"
title = "Chart Caster"
aon = "ArchetypeDisplay.aspx?FixedName=Mesmerist%20Chart%20Caster"
source_ids = ["blood-of-the-ancients"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "chart_caster", path = "json/archetypes_mesmerist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/mesmerist" },
]
[[sources]]
publication = "blood-of-the-ancients"
page = "10"

[fields]
kind = "archetype"
features = [
  { anchor = "subject-of-the-stars" },
  { anchor = "feign-destiny", level = 3 },
]
trades = [
  { replaces = "Touch treatment", feature = "touch-treatment", by = ["feign-destiny"] },
  { alters = "Mesmerist tricks", feature = "mesmerist-tricks", by = ["subject-of-the-stars"] },
  { alters = "manifold tricks", feature = "manifold-tricks", by = ["subject-of-the-stars"] },
]
+++

Lirgeni astrologists would divine their futures by consulting star charts, but some had no talent
for astrology and simply faked their results. When prophecy died with Aroden, a few Lirgeni
survivors continued with this "reliable" method.

## Class Skills {#class-skills}

A chart caster adds Knowledge (nature) and Knowledge (planes) to his list of class skills.

This alters the mesmerist's class skills.

## Subject of the Stars (Su) {#subject-of-the-stars}

A chart caster cannot implant tricks as a standard action. Instead, he can spend 5 minutes to
implant multiple tricks in a single willing target. The number of tricks he can implant per day is
unchanged from the regular mesmerist class, but he can apply as many of those tricks as he chooses
on a single use of this ability.

If implanting tricks in himself, the caster merely spends 5 minutes in contemplation; otherwise, he
consults star charts while ritually asking the creature questions, and still must touch them to do
so. At 1st level, he can select multiple instances of the same trick to implant in a single subject.
At 5th level, a chart caster can implant two different subjects with multiple instances of one trick
each and can choose a different trick for each subject. The number of additional subjects increases
by one for every 4 mesmerist levels he has beyond 5th.

Using this ability again on an existing subject or to implant any trick on a new subject ends all
previously implanted tricks. The caster can trigger only one instance of the same trick on a given
subject per round.

This alters mesmerist tricks and manifold tricks.

## Feign Destiny (Su) {#feign-destiny}

At 3rd level, as an immediate action, a chart caster can grant an ally a +1 competence bonus on a
failed attack roll, saving throw, or skill check by reminding his ally of their destined success.
The chart caster must use his ability within 1 round of the failed check, and his ally must be
within 30 feet of him when he does. If the bonus is enough to turn the failure into a success, the
ally succeeds at the check. At 6th level, the bonus increases to +2. At 10th level, it increases to
+5. A chart caster can use this ability a number of times per day equal to his Charisma modifier.

This replaces touch treatment.
