+++
id = "ref/arc-summoner/shaitan-binder"
kind = "archetype"
title = "Shaitan Binder"
aon = "ArchetypeDisplay.aspx?FixedName=Summoner%20Shaitan%20Binder"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shaitan_binder", path = "json/archetypes_summoner.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/summoner" },
]
[[sources]]
publication = "advanced-race-guide"
page = "146"

[fields]
kind = "archetype"
features = [
  { anchor = "base-form", level = 1 },
  { anchor = "shaitan-magic", level = 4 },
  { anchor = "earth-glide", level = 10 },
  { anchor = "stone-curse", level = 18 },
  { anchor = "noble-eidolon", level = 20 },
]
trades = [
  { replaces = "Shield ally", feature = "shield-ally", by = ["shaitan-magic"] },
  { replaces = "greater shield ally", feature = "greater-shield-ally", by = ["shaitan-magic"] },
  { replaces = "Aspect", feature = "aspect", by = ["earth-glide"] },
  { replaces = "Greater aspect", feature = "greater-aspect", by = ["stone-curse"] },
  { replaces = "Twin eidolon", feature = "twin-eidolon", by = ["noble-eidolon"] },
]
+++

Shaitan binders call upon a reflection of their genie ancestors to serve as their eidolons. A
shaitan binder has the following class features.

## Base Form {#base-form}

At 1st level, if a shaitan binder's eidolon has the biped base form, it gains a +2 bonus to one
ability score. The shaitan binder must make this choice at 1st level. If at any time the shaitan
binder's eidolon has another base form, it loses this bonus until it returns to biped form. A
shaitan binder's eidolon does not gain the share spells ability.

## Shaitan Magic (Su) {#shaitan-magic}

At 4th level, a shaitan binder's eidolon gains the [basic magic](ref/evolution/basic-magic)
evolution (_Ultimate Magic_) as a free evolution. At 6th level, it gains the
[minor magic](ref/evolution/minor-magic) evolution (_Ultimate Magic_).

At 8th level, it gains the [major magic](ref/evolution/major-magic) evolution (_Ultimate Magic_) as
a free evolution, and adds the following to the list of available spells for that evolution:
_[glitterdust](ref/spell/glitterdust)_ and
_[soften earth and stone](ref/spell/soften-earth-and-stone)_.

At 12th level, it gains the [ultimate magic](ref/evolution/ultimate-magic) evolution (_Ultimate
Magic_) as a free evolution, and adds the following to the list of available spells for that
evolution: _[meld into stone](ref/spell/meld-into-stone)_ and
_[stone shape](ref/spell/stone-shape)_.

Although the shaitan binder gains the standard versions of these evolutions for free, he must pay
the normal cost to upgrade them to the improved versions. This ability replaces shield ally and
greater shield ally.

## Earth Glide (Su) {#earth-glide}

At 10th level, if a shaitan binder's eidolon has the [burrow](ref/evolution/burrow) evolution, it
gains the [earth glide](ref/umr/earth-glide) universal monster ability and can use this ability to
travel at its full base speed. This ability replaces aspect.

## Stone Curse (Su) {#stone-curse}

At 18th level, a [shaitan](ref/monster/genie-shaitan) binder may select stone curse as a 4-point
evolution. This allows the eidolon to trap creatures in stone like the shaitan stone curse ability.
The DC to resist or break free of the stone curse is 10 + 1/2 the eidolon's Hit Dice + the eidolon's
Strength score. This ability replaces greater aspect.

## Noble Eidolon (Sp) {#noble-eidolon}

At 20th level, a shaitan binder's eidolon gains the ability to grant its summoner's wishes. Once per
day, the eidolon can cast _[limited wish](ref/spell/limited-wish)_ as a
[spell-like ability](ref/umr/spell-like-abilities). The eidolon's caster level is equal to its
level. The wish must be spoken aloud by the shaitan binder, beginning with the words "I wish," and
cannot duplicate a wish the eidolon has granted within the past 24 hours. If the eidolon uses this
ability to duplicate a spell with a costly material component, the shaitan binder must provide that
component. This ability replaces twin eidolon.
