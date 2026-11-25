+++
id = "ref/arc-summoner/wild-caller-arg"
kind = "archetype"
title = "Wild Caller (ARG)"
aon = "ArchetypeDisplay.aspx?FixedName=Summoner%20Wild%20Caller%20%28ARG%29"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wild_caller_arg", path = "json/archetypes_summoner.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/summoner" },
]
[[sources]]
publication = "advanced-race-guide"
page = "44"

[fields]
kind = "archetype"
features = [
  { anchor = "spells" },
  { anchor = "eidolon" },
  { anchor = "summon-nature-s-ally-i", level = 1 },
]
trades = [
  { replaces = "Summon monster I", feature = "summon-monster-i", by = ["summon-nature-s-ally-i"] },
  { alters = "Spell list of the summoner", feature = "spells", power = "spell list", by = ["spells"] },
  { alters = "Eidolon", feature = "eidolon", by = ["eidolon"] },
]
+++

Often a half-elf's ties to nature and elven heritage are so strong that they can dramatically affect
the nature of his summonings. The wild caller calls eidolons that take more natural and savage forms
and summons from nature rather than the Great Beyond. A wild caller has the following class
features.

## Spells {#spells}

A wild caller does not have access to _[summon monster](ref/spell/summon-monster)_ spells. Instead,
he swaps out those spells on his spell list with
_[summon nature's ally](ref/spell/summon-natures-ally)_ spells of the same level. This ability
alters the normal spell list of the summoner.

## Eidolon {#eidolon}

The eidolon of a wild caller tends to take more natural and more savage forms than other summoners'
eidolons. A wild caller gains 1/4 his class level as bonus evolution points in his eidolon's
evolution pool, but his eidolon cannot take the following evolutions:

_Advanced Player's Guide_—_1-point evolutions_: magic attacks, [skilled](ref/evolution/skilled)
(while the eidolon can select this evolution, it can only do so with the following skills:
Acrobatics, Climb, Escape Artist, Fly, Intimidate, Perception, Survival, and Swim); _2-point
evolutions_: energy attacks, immunity, weapon training; _3-point evolutions_:
[damage reduction](ref/rule/damage-reduction), frightful presence; _4-point evolutions_: breath
weapon, [spell resistance](ref/rule/spell-resistance).

_Ultimate Magic_—_1-point evolutions_: basic magic, unnatural aura; _2-point evolutions_:
[channel resistance](ref/rule/channel-resistance), head, minor magic, undead appearance; _3-point
evolutions_: major magic; _4-point evolutions_: dimension door, incorporeal form, lifesense, no
breath, ultimate magic.

This ability alters the normal summoner's eidolon class feature, but is otherwise identical to that
class feature.

## Summon Nature's Ally I (Sp) {#summon-nature-s-ally-i}

Starting at 1st level, a wild caller can cast _summon nature's ally_ a number of times per day equal
to 3 + his Charisma modifier. At 3rd level and every 2 levels thereafter, the power of this ability
increases by one spell level, allowing him to summon more powerful creatures (to a maximum of
_summon nature's ally IX_ at 17th level). Furthermore, at 19th level, the wild caller cannot use
_[gate](ref/spell/gate)_ as a [spell-like ability](ref/umr/spell-like-abilities), but can use either
_[summon elder worm](ref/spell/summon-elder-worm)_ or
_[summon froghemoth](ref/spell/summon-froghemoth)_ instead. This ability otherwise functions like
the standard summoner's _[summon monster I](ref/spell/summon-monster-1)_ ability and replaces that
ability.
