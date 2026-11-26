+++
id = "ref/arc-samurai/ward-speaker"
kind = "archetype"
title = "Ward Speaker"
aon = "ArchetypeDisplay.aspx?FixedName=Samurai%20Ward%20Speaker"
source_ids = ["disciples-doctrine"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ward_speaker", path = "json/archetypes_samurai.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/samurai" },
]
[[sources]]
publication = "disciples-doctrine"
page = "26"

[fields]
kind = "archetype"
features = [
  { anchor = "propitiation", level = 1 },
  { anchor = "jinushigami" },
  { anchor = "kodama" },
  { anchor = "shikigami" },
  { anchor = "toshigami" },
  { anchor = "zuishin" },
  { anchor = "resilient-stand", level = 11 },
]
trades = [
  { replaces = "Resolve", feature = "resolve", by = ["propitiation"] },
  { replaces = "greater resolve", feature = "greater-resolve", by = ["propitiation"] },
  { replaces = "true resolve", feature = "true-resolve", by = ["propitiation"] },
  { alters = "Honorable stand", feature = "honorable-stand", by = ["resilient-stand"] },
  { alters = "Alignment" },
]
+++

The ward speaker draws power from simple rituals to honor the spirits found throughout the world so
that he might better protect those entrusted to his care.

## Alignment {#alignment}

A ward speaker must be of a nonevil alignment.

This alters the samurai's alignment.

## Propitiation (Ex, Su, Sp) {#propitiation}

A ward speaker can perform a special ritual to propitiate [kami](ref/family/kami) and gain a sliver
of their power. This ritual must be performed at a shrine or a location warded by a specific type of
kami. The propitiation takes 1 minute and involves clapping, ringing bells, bowing, and token
offerings of coins, food, incense, or other gifts. The ward speaker's propitiation must be performed
uninterrupted to receive any benefits from it. At the end of this ritual, the ward speaker
immediately gains a fortune depending on the type of kami he sought to propitiate. Common kami are
presented beginning on page 159 of _Bestiary 3_, and the fortunes each of those kami grant are
listed below.

As an immediate action, the ward speaker can dismiss the fortune to reroll one d20 roll before the
results of the roll are revealed; he must use the result of the second roll, even if it's worse. If
not dismissed, a fortune remains in effect until the ward speaker regains the use of his daily
abilities, at which point the fortune and its benefits end. If a ward speaker dismisses a fortune to
receive a benefit based on the specific kami he propitiated (see below), he does not also gain the
reroll described here.

The ward speaker can perform this ritual once per day at 1st level, plus one additional time per day
for every 3 levels beyond 1st, to a maximum of seven times per day at 19th level. He can maintain
only one fortune at a time; performing a propitiation while he already has a fortune active ends the
previous fortune and its benefits.

This replaces resolve, greater resolve, and true resolve.

## Jinushigami (Ex, Sp) {#jinushigami}

The ward speaker (and his mount, if he has one) gains a 10-foot enhancement bonus to base speed. At
9th level, this enhancement bonus increases to 20 feet. At 17th level, once per day, he can dismiss
this fortune as an immediate action to cast _[earthquake](ref/spell/earthquake)_ as a
[spell-like ability](ref/umr/spell-like-abilities), using his samurai level as his caster level.

## Kodama (Su) {#kodama}

As a standard action, the ward speaker can afflict one target that can see him with a distracting
[gaze](ref/umr/gaze). If the target fails a Will save (DC = 10 + half the ward speaker's samurai
level), it is [staggered](ref/misc/staggered) for 1d4 rounds. At 9th level, it is instead staggered
for 2d4 rounds. At 17th level, it is instead staggered for 1 minute. Once a creature has been
targeted by this ability, it cannot be targeted by it again for 24 hours.

## Shikigami (Ex) {#shikigami}

The ward speaker gains [Catch Off-Guard](ref/feat/catch-off-guard) and
[Throw Anything](ref/feat/throw-anything) as bonus feats. At 9th level, he gains
[Toughness](ref/feat/toughness) and [Step Up](ref/feat/step-up). At 17th level, he gains
[Following Step](ref/feat/following-step) and [Step Up and Strike](ref/feat/step-up-and-strike),
even if he does not meet the prerequisites.

## Toshigami (Sp) {#toshigami}

The ward speaker can [speak with plants](ref/spell/speak-with-plants), as the _speak with plants_
spell. At 9th level, the ward speaker can dismiss this fortune as an immediate action to cast
_[haste](ref/spell/haste)_ as a [spell-like ability](ref/umr/spell-like-abilities). Once per day at
17th level, the ward speaker can instead dismiss this fortune to cast
_[temporal stasis](ref/spell/temporal-stasis)_ as a
[spell-like ability](ref/umr/spell-like-abilities). The ward speaker's caster level for these
[spell-like abilities](ref/umr/spell-like-abilities) is equal to his samurai level.

## Zuishin (Sp) {#zuishin}

As an immediate action, the ward speaker can dismiss this fortune to cast
_[cure light wounds](ref/spell/cure-light-wounds)_ as a
[spell-like ability](ref/umr/spell-like-abilities). At 9th level, the ward speaker can dismiss this
fortune to cast _[cure serious wounds](ref/spell/cure-serious-wounds),
[lesser restoration](ref/spell/restoration-lesser), [remove curse](ref/spell/remove-curse),_ or
_[remove disease](ref/spell/remove-disease)_; at 17th level, he also adds
_[breath of life](ref/spell/breath-of-life)_ and _[heal](ref/spell/heal)_ to this list. The ward
speaker's caster level for these [spell-like abilities](ref/umr/spell-like-abilities) is equal to
his samurai level.

## Resilient Stand (Ex) {#resilient-stand}

At 11th level, the spirits can bolster a ward speaker's willpower and resolve, granting him an inner
reservoir he can use when he needs it most. If a ward speaker has not expended his daily uses of
propitiation, he can call upon the spirits to reroll a saving throw during an honorable stand
instead of expending a use of resolve to do so. He must take the result of the second roll, even if
it is worse. This expends a daily use of propitiation.

This alters honorable stand.
