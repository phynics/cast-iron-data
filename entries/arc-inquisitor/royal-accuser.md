+++
id = "ref/arc-inquisitor/royal-accuser"
kind = "archetype"
title = "Royal Accuser"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Royal%20Accuser"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "royal_accuser", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "45"

[fields]
kind = "archetype"
features = [
  { anchor = "meticulous-inspection", level = 1 },
  { anchor = "detect-monsters-and-secrets", level = 2 },
  { anchor = "favored-enemy", level = 3 },
  { anchor = "informed-hunch", level = 6 },
  { anchor = "greater-detect-magic", level = 12 },
  { anchor = "final-sway", level = 18 },
]
trades = [
  { replaces = "Stern gaze", feature = "stern-gaze", by = ["meticulous-inspection"] },
  { replaces = "Detect alignment", feature = "detect-alignment", by = ["detect-monsters-and-secrets"] },
  { replaces = "Solo tactics", feature = "solo-tactics", by = ["favored-enemy"] },
  { replaces = "teamwork feats gained at 3rd, 9th, and 15th levels", feature = "teamwork-feat", levels = [3, 9, 15], by = ["favored-enemy"] },
  { replaces = "Teamwork feat granted at 6th level", feature = "teamwork-feat", levels = [6], by = ["informed-hunch"] },
  { replaces = "Teamwork feat granted at 12th", feature = "teamwork-feat", levels = [12], by = ["greater-detect-magic"] },
  { replaces = "Teamwork feat granted at 18th level", feature = "teamwork-feat", levels = [18], by = ["final-sway"] },
  { alters = "Class skills" },
]
+++

Royal accusers serve the prince of Ustalav, cutting through the nation's baroque politics and
quietly facing its many threats.

## Class Skills {#class-skills}

A royal accuser adds Knowledge (local) to his list of class skills, instead of Knowledge (nature).

This alters the inquisitor's class skills.

## Meticulous Inspection (Ex) {#meticulous-inspection}

A royal accuser gains a morale bonus equal to 1/2 his inquisitor level on all Perception checks
(minimum +1).

This ability replaces stern gaze.

## Detect Monsters and Secrets (Sp) {#detect-monsters-and-secrets}

At 2nd level, a royal accuser can use _[detect aberration](ref/spell/detect-aberration)_,
_[detect secret doors](ref/spell/detect-secret-doors)_, and
_[detect undead](ref/spell/detect-undead)_ at will. He can only use one of these at any given time.

This ability replaces detect alignment.

## Favored Enemy (Ex) {#favored-enemy}

At 3rd level, a royal accuser gains [favored enemy](ref/ability/favored-enemy), as the
[ranger](ref/class/ranger) class feature. He must choose his favored enemy from the following list:
aberration, dragon, humanoid (orc), humanoid (shapechanger), and undead. He gains another favored
enemy at 9th and 15th levels.

This replaces solo tactics and the teamwork feats gained at 3rd, 9th, and 15th levels.

## Informed Hunch (Su) {#informed-hunch}

At 6th level, once per day, a royal accuser can contemplate an ongoing investigation he is involved
in and potentially know whether his hunches are on the right track.

This functions as _[augury](ref/spell/augury)_, except if it succeeds, the royal accuser gets one of
the following results in place of weal, woe, or weal and woe. The royal accuser treats his
inquisitor level as his caster level.

- Correct (if the hunch is the exact truth, such as if a particular individual is responsible for a
  crime, or if a particular organization is behind a series of events).

- Incorrect (if the hunch is entirely off base, such as if a suspected individual had nothing to do
  with a crime, or a suspected organization had no interest or hand in a series of events).

- On the right track (if the hunch is partially correct, such as if a suspected individual
  participated in a criminal conspiracy or had foreknowledge of the crime in question, or if a
  suspected organization directly profited from and knew about but did not entirely orchestrate a
  series of events).

This replaces the teamwork feat granted at 6th level.

## Greater Detect Magic (Sp) {#greater-detect-magic}

At 12th level, a royal accuser can use [greater detect magic](ref/spell/detect-magic-greater) at
will.

This ability replaces the teamwork feat granted at 12th.

## Final Sway (Ex) {#final-sway}

At 18th level, a royal accuser's word and intuition are greatly trusted and valued. Once per day,
when using the [influence system](ref/rule/influence) and interacting with an individual or
organization with whom he has at least minor sway or is respected (rank 2), the royal accuser can
treat his influence as two steps higher for the purposes of making a single request of that
individual or organization. Alternatively, he can treat an individual's attitude toward him as up to
two steps higher for the purpose of such a request.

This replaces the teamwork feat granted at 18th level.
