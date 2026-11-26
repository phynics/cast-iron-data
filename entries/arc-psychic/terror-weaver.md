+++
id = "ref/arc-psychic/terror-weaver"
kind = "archetype"
title = "Terror Weaver"
aon = "ArchetypeDisplay.aspx?FixedName=Psychic%20Terror%20Weaver"
source_ids = ["heroes-from-the-fringe"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "terror_weaver", path = "json/archetypes_psychic.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/psychic" },
]
[[sources]]
publication = "heroes-from-the-fringe"
page = "26"

[fields]
kind = "archetype"
features = [
  { anchor = "manipulation", level = 2 },
  { anchor = "aura-of-intimidation", level = 9 },
  { anchor = "persistent-nightmare", level = 15 },
]
trades = [
  { replaces = "Detect thoughts", feature = "detect-thoughts", by = ["manipulation"] },
  { replaces = "Telepathic bond", feature = "telepathic-bond", by = ["aura-of-intimidation"] },
  { replaces = "Phrenic amplifications gained at 11th and 19th levels", feature = "phrenic-amplifications", levels = [11, 19], by = ["aura-of-intimidation"] },
  { replaces = "Phrenic amplification gained at 15th level", feature = "phrenic-amplifications", levels = [15], by = ["persistent-nightmare"] },
]
+++

A number of exceptional Darklands half-orcs have developed potent psychic abilities, unlocked by
generations of exposure to a specific combination of mind-altering fungi and radiation. Powerful
half-orc manipulators often rule smaller Darklands tribes from the shadows, but with few orcs able
to match their mental acuity, their only limit is their own ambition.

## Manipulation (Sp) {#manipulation}

At 2nd level, a terror weaver can cast _[charm person](ref/spell/charm-person)_ once per day as a
[spell-like ability](ref/umr/spell-like-abilities). He can also expend any unused spell slot of 1st
level or higher to cast _[charm person](ref/spell/charm-person)_. If he does so, he uses the level
of the spell slot expended to determine the save DC. When a terror weaver gains this ability, if he
already knows _[charm person](ref/spell/charm-person),_ he can learn a different 1st-level spell in
place of _[charm person](ref/spell/charm-person)_, losing the old spell in exchange for the new one.

This replaces detect thoughts.

## Aura of Intimidation (Sp) {#aura-of-intimidation}

Because he lacks the physical prowess of most orcs, a terror weaver seeks to end fights before they
start. At 9th level, he can cast _[aura of doom](ref/spell/aura-of-doom)_ as a
[spell-like ability](ref/umr/spell-like-abilities) once per day. He can also expend any unused spell
slot of 4th level or higher to cast _[aura of doom](ref/spell/aura-of-doom)_. Casting the spell
using a higher-level spell slot gives no benefit on its own, but the terror weaver can apply
metamagic feats that would increase the spell level to the appropriate level. At 11th level, a
terror weaver's _[aura of doom](ref/spell/aura-of-doom)_ causes enemies to become
[frightened](ref/misc/frightened) instead of [shaken](ref/misc/shaken). At 19th level, it causes
enemies to become [panicked](ref/misc/panicked).

This replaces telepathic bond and the phrenic amplifications gained at 11th and 19th levels.

## Persistent Nightmare (Sp) {#persistent-nightmare}

Gloomkin often suffer from lifetimes of cruelty and abuse, and a terror weaver repays that suffering
back onto his tormentors. At 15th level, when he successfully casts a mind-affecting spell on a
target, he can spend 2 points from his phrenic pool to afflict the target with a
_[nightmare](ref/spell/nightmare)_ spell the next time it goes to sleep. The day after
_[nightmare](ref/spell/nightmare)_ has taken effect, regardless of the victim's saving throw, the
target takes a -2 penalty on Will saves against the terror weaver's mind-affecting spells and
abilities for 24 hours.

This ability replaces the phrenic amplification gained at 15th level.
