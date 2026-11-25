+++
id = "ref/arc-skald/fated-champion"
kind = "archetype"
title = "Fated Champion"
aon = "ArchetypeDisplay.aspx?FixedName=Skald%20Fated%20Champion"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fated_champion", path = "json/archetypes_skald.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/skald" },
]
[[sources]]
publication = "advanced-class-guide"
page = "114"

[fields]
kind = "archetype"
features = [
  { anchor = "watcher-of-the-weave", level = 2 },
  { anchor = "far-seer", level = 5 },
  { anchor = "shield-of-foresight", level = 10 },
  { anchor = "not-this-day", level = 20 },
]
trades = [
  { replaces = "Well-versed", feature = "well-versed", by = ["watcher-of-the-weave"] },
  { replaces = "Dirge of doom raging song", feature = "dirge-of-doom", by = ["shield-of-foresight"] },
  { replaces = "Master skald", feature = "master-skald", by = ["not-this-day"] },
  { alters = "Spell kenning", feature = "spell-kenning", by = ["far-seer"] },
]
+++

Many cultures see fate as a limit that is both stifling and unwanted, regardless of the destiny that
lurks in the days and years ahead. Among cultures where skalds are the keepers of lore and wisdom,
there are those who learn to read the winds of fate and take up the mantle of the fated champion,
knowing and embracing their destined paths with strength borne of conviction.

## Watcher of the Weave (Ex) {#watcher-of-the-weave}

At 2nd level, a fated champion learns to see the tapestry of events moments before it is woven. He
gains an insight bonus on initiative checks equal to 1/2 his skald level. This ability replaces
well-versed.

## Far Seer (Su) {#far-seer}

At 5th level, a fated champion learns a method of spell kenning that is especially suited for
divining and understanding the future, but not for directly harming opponents. For the purpose of
determining what level spell slot he expends when using spell kenning, the skald treats the spell
level of spells that predict the future (such as _[augury](ref/spell/augury)_ and
_[divination](ref/spell/divination)_) as one spell level lower (minimum spell level 1st), and treats
the spell level of spells that deal damage as one spell level higher. This alters the spell kenning
class feature.

## Shield of Foresight (Su) {#shield-of-foresight}

At 10th level, a fated champion's certainty of his own fate grants him the ability to stare down
fear and remain unbowed. When using raging song, he is immune to fear effects, and allies affected
by his raging song gain a +5 bonus on saves attempted against fear effects. This ability replaces
the dirge of doom raging song.

## Not This Day (Su) {#not-this-day}

At 20th level, the fated champion gains the ability to reweave the strands of fate. As an immediate
action, he can expend 10 rounds of raging song to either reroll a saving throw or force an opponent
to reroll an attack roll. The decision to use this ability must be made before the results of the
initial roll are revealed, and the champion or his opponent must take the result of the reroll. This
ability replaces master skald.

## Rage Powers {#rage-powers}

The following rage powers complement the fated champion archetype: boasting taunt, clear mind, eater
of magic, fierce fortitude, flesh wound, guarded life, intimidating glare, linnorm death curse
(cairn, tarn), and renewed vitality. (Those with asterisks \[\*\] are listed in the rage powers
section on the previous page.)
