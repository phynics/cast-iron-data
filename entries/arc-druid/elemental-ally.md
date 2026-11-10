+++
id = "ref/arc-druid/elemental-ally"
kind = "archetype"
title = "Elemental Ally"
source_ids = ["monster-summoners-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "elemental_ally", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "monster-summoners-handbook"
page = "16"

[fields]
kind = "archetype"
replaces = ["Nature's bond", "wild shape", "Wild empathy", "Resist nature's lure"]
replaces_features = ["wild-shape", "wild-empathy", "resist-nature-s-lure"]
+++

An elemental ally is a druid who has crafted powerful bonds of trust and friendship with one ally
from each of the four primary elemental planes. Elemental allies are most common in Qadira, where
they are considered similar to genie-binders.

**Elemental Eidolons**

**Action:** Ability

**Gained:** At 1st Level

**Replaces:** Nature's bond, wild shape

An elemental ally has four elemental eidolons she can summon, one each for the elements of air,
earth, fire, and water. Their abilities and statistics are determined using the rules for
[elemental](ref/eidolon/elemental) eidolons for the
[unchained summoner](ref/class/unchained-summoner) class, as if the elemental ally were a summoner
of her druid level, except they gain no additional evolution pool (just those evolutions from their
base form and base evolutions from their subtype).

Each of the four elementals has its own base form, skills, and feats. The elemental ally can summon
one of these elementals with the same 1-minute ritual a summoner normally uses to do so. The
elemental ally can't summon an eidolon or cast [summon nature's ally](ref/spell/summon-natures-ally)
if she currently has an eidolon summoned. She also can't summon an eidolon if she currently has a
creature summoned through other means. If one of the elemental ally's eidolons is killed, she cannot
summon any eidolons for 24 hours. The elemental ally can dismiss her eidolon as a **standard
action**.

As the elemental ally gains levels, her elemental eidolons' base statistics and base evolutions
increase as if her druid level were her summoner level. The eidolons gain the _darkvision, link,
share spells, evasion, ability score increase, devotion, multiattack,_ and _improved evasion_
abilities at the appropriate levels, but never gain an evolution pool. Abilities and spells that
grant additional evolution points to eidolons do not function for elemental eidolons, though any
ability that would grant evolution points to an animal companion does work. The elemental ally does
not gain _life link_ or any other class features a summoner gains in relation to her eidolon.

**Elemental Empathy (Ex)**

**Action:** Ability

**Replaces:** Wild empathy

An elemental ally can improve the attitude of a creature of the elemental subtype. This ability
functions just like a Diplomacy check to improve the attitude of a person. The elemental ally rolls
1d20 and adds her druid level and her Charisma modifier to determine the _elemental empathy_ check
result.

To use _elemental empathy,_ the elemental ally and the elemental must be able to study each other,
which means that they must be within 30 feet of one another under normal conditions. Generally,
influencing an elemental in this way takes 1 minute, but as with influencing people, it might take
more or less time.

An elemental ally can also use this ability to influence a non-elemental outsider with the air,
earth, fire, or water subtype, but she takes a -4 penalty on the check.

**Elemental Magic**

**Passive:** The elemental ally can target elementals (including her elemental eidolons) with any
spell she casts that targets animals, even though elementals can't normally be targeted by such
spells.

**Elemental Resistance (Ex)**

**Gained:** At 4th Level

**Passive:** An elemental ally gains [resist](ref/umr/resistance) acid, cold, electricity, and
fire 5.

**Replaces:** Resist nature's lure
