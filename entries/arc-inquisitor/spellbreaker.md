+++
id = "ref/arc-inquisitor/spellbreaker"
kind = "archetype"
title = "Spellbreaker"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Spellbreaker"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spellbreaker", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "ultimate-combat"
page = "52"

[fields]
kind = "archetype"
features = [
  { anchor = "strong-willed", level = 1 },
  { anchor = "defense-against-magic", level = 3 },
  { anchor = "foil-casting", level = 3 },
  { anchor = "impervious", level = 20 },
]
trades = [
  { replaces = "Monster lore", feature = "monster-lore", by = ["strong-willed"] },
  { replaces = "Bonus teamwork feats", feature = "teamwork-feat", by = ["defense-against-magic"] },
  { replaces = "Solo tactics", feature = "solo-tactics", by = ["foil-casting"] },
  { replaces = "True judgment", feature = "true-judgment", by = ["impervious"] },
]
+++

The world is full of dangerous magic, and many recoil in the face of such power. The spellbreaker,
by contrast, learns to recognize and resist certain types of magic, wading through waves of magic to
reach her foes.

## Strong-Willed (Ex) {#strong-willed}

At 1st level, a spellbreaker is able to stand strong against magical effects that seek to control,
compel, or persuade her. The spellbreaker rolls twice and takes the best result when making a Will
saving throw against a mind-affecting effect. This ability replaces monster lore.

## Defense against Magic (Ex) {#defense-against-magic}

At 3rd level, a spellbreaker picks a single [wizard school](ref/ability/arcane-schools). She gains a
+1 bonus on saving throws against arcane spells of that school. Every four levels beyond 3rd, the
spellbreaker picks a new school and gains this bonus against arcane spells of that school (to a
maximum of five schools of magic at 19th level). Furthermore, each time the spellbreaker picks a new
school, the bonuses for the schools she has already chosen increase by 1. This ability replaces all
bonus teamwork feats.

## Foil Casting (Su) {#foil-casting}

At 3rd level, when an opponent tries to cast an arcane spell within a spellbreaker's threatened
area, the DC for that caster to cast defensively increases by 2. This increase stacks with the
effects of the [Disruptive](ref/feat/disruptive) feat (see page 112 of the _Core Rulebook_).
Furthermore, the spellbreaker knows where to hit foes to foil casting from a distance. Each time she
hits an arcane spellcaster or a creature that uses
[spell-like abilities](ref/umr/spell-like-abilities) with a ranged weapon attack, the DC of any
[Concentration](ref/rule/concentration) checks the caster makes increases by 2 for 1 round. This
ability replaces solo tactics.

## Impervious (Ex) {#impervious}

At 20th level, a spellbreaker becomes immune to the effects of a single school of arcane magic. That
school of magic must be the first one she picked for defense against magic (see above). Neither
harmful nor helpful arcane spells of that school have an effect on the spellbreaker. If a spell of
that school is an area of effect spell, the spell goes off as normal, but the spellbreaker is
untouched by its effects. Once per day, as a swift action, the spellbreaker can grant this
imperviousness to all allies in a 60-foot [burst](ref/misc/burst) for 1 minute. This ability
replaces true judgment.
