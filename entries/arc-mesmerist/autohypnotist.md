+++
id = "ref/arc-mesmerist/autohypnotist"
kind = "archetype"
title = "Autohypnotist"
aon = "ArchetypeDisplay.aspx?FixedName=Mesmerist%20Autohypnotist"
source_ids = ["psychic-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "autohypnotist", path = "json/archetypes_mesmerist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/mesmerist" },
]
[[sources]]
publication = "psychic-anthology"
page = "17"

[fields]
kind = "archetype"
replaces = ["Mental potency"]
alters = ["Hypnotic stare"]
replaces_features = ["mental-potency"]
alters_features = ["hypnotic-stare"]
+++

An autohypnotist has incredibly powerful psychic abilities that he can't entirely control. As a
result, maintaining his powers against an opponent hinders him as much as his target.

**Autohypnosis (Su)**

**Action:** Ability

**Alters:** Hypnotic stare

**Gained:** At 1st Level

An autohypnotist has mastered techniques that make his _hypnotic stare_ ability more potent, but at
a terrible cost - the autohypnotist succumbs to his own power when he uses it. Whenever the
autohypnotist focuses his stare on an opponent, the penalties that opponent takes from the _hypnotic
stare_ (as well as any _bold stare_ improvements or stare feats that the autohypnotist has) increase
by 1. However, the autohypnotist takes the same penalties as his target while focusing his stare,
including those of any _bold stare_ improvements he has.

An autohypnotist can reduce or negate the penalty he imposes upon himself with his _hypnotic stare,_
but doing so allows his opponent an opportunity to escape from the stare as well. The autohypnotist
can reduce the penalty he takes from his _hypnotic stare_ ability by
[half](ref/misc/fractions-and-rounding) for 1 round as a **swift action**. If he does so, there is a
25% chance that his _hypnotic stare_ ends altogether. Alternatively, he can choose to negate the
penalty he takes from his _hypnotic stare_ for 1 round, but his _hypnotic stare_ then has a 50%
chance of ending.

**Wide Stare (Su)**

**Gained:** At 5th Level

**Replaces:** Mental potency

**Special:** When the autohypnotist uses this ability, he cannot exclude allies or any other
creatures from this effect. If the autohypnotist's _hypnotic stare_ ends for the focused opponent,
this effect ends.

**Standard:** Whenever an autohypnotist is focusing his stare on a foe, he can broaden his _hypnotic
stare._ When he does so, all creatures within 10 feet of his opponent take penalties from the
mesmerist's _hypnotic stare_ and _bold stare_ class features as if he were maintaining his _hypnotic
stare_ against each of those creatures, except such creatures treat his _hypnotic stare_ penalty as
if it were 2 lower.
