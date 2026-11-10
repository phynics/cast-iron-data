+++
id = "ref/arc-samurai/ward-speaker"
kind = "archetype"
title = "Ward Speaker"
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
replaces = ["Resolve", "greater resolve", "true resolve"]
alters = ["Honorable stand"]
replaces_features = ["resolve", "greater-resolve", "true-resolve"]
alters_features = ["honorable-stand"]
+++

The ward speaker draws power from simple rituals to honor the spirits found throughout the world so
that he might better protect those entrusted to his care.

**Prerequisites:** Nonevil alignment

**Propitiation (Ex, Su, Sp)**

**Ability:** A ward speaker can perform a special ritual to _propitiate_ [kami](ref/family/kami) and
gain a sliver of their power. This ritual must be performed at a shrine or a location warded by a
specific type of kami. The _propitiation_ takes 1 minute and involves clapping, ringing bells,
bowing, and token offerings of coins, food, incense, or other gifts. The ward speaker's
_propitiation_ must be performed uninterrupted to receive any benefits from it. At the end of this
ritual, the ward speaker immediately gains a _fortune_ depending on the type of kami he sought to
_propitiate._

**Immediate:** The ward speaker can dismiss the _fortune_ to reroll one d20 roll before the results
of the roll are revealed; he must use the result of the second roll, even if it's worse.

**Replaces:** Resolve, greater resolve, true resolve

**Special:** If not dismissed, a _fortune_ remains in effect until the ward speaker regains the use
of his daily abilities, at which point the _fortune_ and its benefits end. If a ward speaker
dismisses a _fortune_ to receive a benefit based on the specific kami he _propitiated_ (see below),
he does not also gain the reroll described here. He can maintain only one _fortune_ at a time;
performing a _propitiation_ while he already has a _fortune_ active ends the previous _fortune_ and
its benefits.

**Usage:** 1 time/day + 1 per 3 samurai levels beyond 1st

**Jinushigami (Ex, Sp)**

**At 17th Level:** Once per day, he can dismiss this _fortune_ as an **immediate action** to cast
[earthquake](ref/spell/earthquake) as a [spell-like ability](ref/umr/spell-like-abilities), using
his samurai level as his caster level.

**At 9th Level:** This enhancement bonus increases to 20 feet.

**Passive:** The ward speaker (and his mount, if he has one) gains a 10-foot enhancement bonus to
base speed.

**Kodama (Su)**

**At 17th Level:** It is instead staggered for 1 minute.

**At 9th Level:** It is instead staggered for 2d4 rounds.

**Special:** Once a creature has been targeted by this ability, it cannot be targeted by it again
for 24 hours

**Standard:** The ward speaker can afflict one target that can see him with a distracting
[gaze](ref/umr/gaze). If the target fails a Will save (DC = 10 + half the ward speaker's samurai
level), it is [staggered](ref/misc/staggered) for 1d4 rounds.

**Shikigami (Ex)**

**Ability:** The ward speaker gains [Catch Off-Guard](ref/feat/catch-off-guard) and
[Throw Anything](ref/feat/throw-anything) as bonus feats.

**At 17th Level:** He gains [Following Step](ref/feat/following-step) and
[Step Up and Strike](ref/feat/step-up-and-strike), even if he does not meet the prerequisites.

**At 9th Level:** He gains [Toughness](ref/feat/toughness) and [Step Up](ref/feat/step-up).

**Toshigami (Sp)**

**Ability:** The ward speaker can speak with plants, as the
[speak with plants](ref/spell/speak-with-plants) spell.

**At 17th Level:** Once per day, the ward speaker can instead dismiss this _fortune_ to cast
[temporal stasis](ref/spell/temporal-stasis) as a
[spell-like ability](ref/umr/spell-like-abilities).

**At 9th Level:** The ward speaker can dismiss this _fortune_ as an **immediate action** to cast
[haste](ref/spell/haste) as a [spell-like ability](ref/umr/spell-like-abilities).

**Special:** The ward speaker's caster level for these
[spell-like abilities](ref/umr/spell-like-abilities) is equal to his samurai level.

**Zuishin (Sp)**

**Immediate:** The ward speaker can dismiss this _fortune_ to cast
[cure light wounds](ref/spell/cure-light-wounds) as a
[spell-like ability](ref/umr/spell-like-abilities).

**At 17th Level:** He also adds [breath of life](ref/spell/breath-of-life) and
[heal](ref/spell/heal) to this list.

**At 9th Level:** The ward speaker can dismiss this _fortune_ to cast
[cure serious wounds](ref/spell/cure-serious-wounds),
[lesser restoration](ref/spell/restoration-lesser), [remove curse](ref/spell/remove-curse), or
[remove disease](ref/spell/remove-disease).

**Special:** The ward speaker's caster level for these
[spell-like abilities](ref/umr/spell-like-abilities) is equal to his samurai level.

**Resilient Stand (Ex)**

**Ability:** If a ward speaker has not expended his daily uses of _propitiation,_ he can call upon
the spirits to reroll a saving throw during an _honorable stand_ instead of expending a use of
_resolve_ to do so. He must take the result of the second roll, even if it is worse. This expends a
daily use of _propitiation._

**Alters:** Honorable stand

**Flavor:** The spirits can bolster a ward speaker's willpower and resolve, granting him an inner
reservoir he can use when he needs it most.

**Gained:** At 11th Level
