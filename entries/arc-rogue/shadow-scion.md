+++
id = "ref/arc-rogue/shadow-scion"
kind = "archetype"
title = "Shadow Scion"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Shadow%20Scion"
source_ids = ["legacy-of-the-first-world"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadow_scion", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "legacy-of-the-first-world"
page = "15"

[fields]
kind = "archetype"
features = [
  { anchor = "shadow-dweller", level = 1 },
  { anchor = "shadow-strike", level = 2 },
  { anchor = "shadow-step", level = 8 },
  { anchor = "shadow-speaker", level = 14 },
  { anchor = "shadow-master", level = 20 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["shadow-dweller"] },
  { replaces = "Rogue talent gained at 2nd level", feature = "rogue-talents", levels = [2], by = ["shadow-strike"] },
  { replaces = "Rogue talent gained at 8th level", feature = "rogue-talents", levels = [8], by = ["shadow-step"] },
  { replaces = "Rogue talent gained at 14th level", feature = "rogue-talents", levels = [14], by = ["shadow-speaker"] },
  { replaces = "Master strike", feature = "master-strike", by = ["shadow-master"] },
]
+++

[Count Ranalc](ref/faith/count-ranalc)'s worshipers congregate in the places between dark and light,
searching for secrets that might one day free their patron from his mysterious exile. Shadow scions
have learned some of these secrets and draw power from the shadows themselves. Many shadow scions
are dedicated [fetchling](ref/race/fetchling) or [wayang](ref/race/wayang) devotees of Count Ranalc.

## Shadow Dweller (Ex) {#shadow-dweller}

A shadow scion gains [darkvision](ref/rule/darkvision) with a range of 30 feet and a +1 competence
bonus on Stealth checks in [dim light](ref/rule/vision-and-light) and darkness. If she already has
[darkvision](ref/rule/darkvision), the range of her [darkvision](ref/rule/darkvision) increases by
10 feet. At 3rd level, and every 2 levels thereafter, the range of her
[darkvision](ref/rule/darkvision) increases by 10 feet and her bonus on Stealth checks increases
by 1.

This ability replaces trapfinding.

## Shadow Strike {#shadow-strike}

At 2nd level, a shadow scion gains [Shadow Strike](ref/feat/shadow-strike) as a bonus feat. A
character using the unchained rogue class from _Pathfinder RPG Pathfinder Unchained_ instead gains
[Blind-Fight](ref/feat/blind-fight) as a bonus feat.

This ability replaces the rogue talent gained at 2nd level.

## Shadow Step (Sp) {#shadow-step}

At 8th level, a shadow scion can walk through the Shadow Plane and reappear elsewhere on the
Material Plane as a standard action. The shadow scion can travel up to 30 feet per rogue level per
day in this fashion, either in a single round or broken up across multiple shadow steps. This
movement must be used in increments of at least 5 feet and does not provoke attacks of opportunity.
Travel through the Shadow Plane is imprecise; when the shadow scion arrives back on the Material
Plane, she reenters 1 square off target, as per the rules for
[thrown splash weapons](ref/rule/throw-splash-weapon). If this would place her in an occupied
square, she instead arrives in the nearest safe location. When the shadow scion arrives on the
Material Plane, she is cloaked in shadow and gains [concealment](ref/rule/concealment) as per the
_[blur](ref/spell/blur)_ spell for 1 round.

This ability replaces the rogue talent gained at 8th level.

## Shadow Speaker (Sp) {#shadow-speaker}

At 14th level, a shadow scion can spend 1 minute meditating within a patch of dim light or darkness;
at the end of the time, she can draw information from the shadows. This functions as
_[commune with nature](ref/spell/commune-with-nature)_, except that it functions in any terrain to a
radius of 100 feet per rogue level, and it cannot reveal information about any object or subject
that is not currently in dim light or darkness. The shadow scion can use this ability once per day
at 14th level and twice per day at 19th level.

This ability replaces the rogue talent gained at 14th level.

## Shadow Master (Su) {#shadow-master}

At 20th level, whenever a shadow scion is in an area of dim light, she gains DR 10/cold iron and a
+2 luck bonus on all saving throws. In addition, whenever she confirms a critical hit against a foe
that is in an area of dim light, that foe is [blinded](ref/misc/blinded) for 1d6 rounds.

This ability replaces master strike.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the shadow scion archetype: false friend, fast stealth, slow
reactions, surprise attack, and underhanded.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the shadow scion archetype: hide in plain sight,
improved evasion, slippery mind, and unwitting ally.
