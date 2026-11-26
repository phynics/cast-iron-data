+++
id = "ref/arc-unchained-summoner/twinned-summoner"
kind = "archetype"
title = "Twinned Summoner"
aon = "ArchetypeDisplay.aspx?FixedName=Summoner%20%28Unchained%29%20Twinned%20Summoner"
source_ids = ["legacy-of-the-first-world"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "twinned_summoner", path = "json/archetypes_summoner_UC.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/unchained-summoner" },
]
[[sources]]
publication = "legacy-of-the-first-world"
page = "18"

[fields]
kind = "archetype"
features = [
  { anchor = "twinned-eidolon" },
  { anchor = "teamwork-feats", level = 4 },
  { anchor = "twinned-transposition", level = 6 },
  { anchor = "twin-summoner", level = 16 },
]
trades = [
  { replaces = "Shield ally", feature = "shield-ally", by = ["teamwork-feats"] },
  { replaces = "greater shield ally", feature = "greater-shield-ally", by = ["teamwork-feats"] },
  { replaces = "Maker's call", feature = "maker-s-call", by = ["twinned-transposition"] },
  { replaces = "transposition", feature = "transposition", by = ["twinned-transposition"] },
  { replaces = "Merge forms", feature = "merge-forms", by = ["twin-summoner"] },
]
+++

Reflecting the connected nature of Imbrex, a twinned summoner and his eidolon appear identical save
for any obvious differences, such as evolutions or equipment.

## Twinned Eidolon {#twinned-eidolon}

The [twinned](ref/eidolon/twinned) summoner's eidolon is restricted to the biped base form. An
unchained summoner's eidolon is instead restricted to the twinned eidolon subtype (see below). If
the summoner's natural size is smaller than Medium, the twinned summoner's eidolon must be Small.
This ability may require a different base form or subtype to match the twinned summoner's natural
form, at the GM's discretion, if the twinned summoner is not a bipedal creature.

## Teamwork Feats (Ex) {#teamwork-feats}

At 4th level and at 12th level, a twinned summoner gains a bonus teamwork feat. He must meet the
prerequisites of the selected teamwork feat. The twinned summoner automatically grants all of his
teamwork feats to his eidolon. The eidolon doesn't need to meet the prerequisites of these teamwork
feats.

This ability replaces shield ally and greater shield ally.

## Twinned Transposition (Su) {#twinned-transposition}

At 6th level, as a standard action, a twinned summoner can swap locations with his eidolon as if
each were using _[dimension door](ref/spell/dimension-door)_, using the twinned summoner's caster
level. If the eidolon is out of range, the ability is wasted. If either the twinned summoner or his
eidolon occupies more squares than the other, each must occupy one or more squares that were
occupied by the other if possible, or as close as possible if not. The twinned summoner can use this
ability once per day at 6th level, plus one additional time per day for every 4 levels beyond 6th.
At 8th level, he can use this ability as a swift action.

This ability replaces maker's call and transposition.

## Twin Summoner (Su) {#twin-summoner}

At 16th level, a twinned summoner can touch his eidolon as a standard action, enhancing its
similarity to the summoner. The eidolon loses any natural weapons or size increases gained from
evolutions, and its Intelligence, Wisdom, and Charisma scores change to match the base scores of the
summoner. The eidolon can cast any of the summoner's spells known using the summoner's caster level
and spell slots. It doesn't gain the benefit of any of the summoner's items, feats, or other effects
that affect spellcasting. The eidolon can keep this form for a number of minutes per day equal to
the summoner's class level. This duration does not need to be consecutive, but it must be spent in
1-minute increments. The summoner can end this effect as a free action.

This ability replaces the merge forms class feature.
