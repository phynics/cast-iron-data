+++
id = "ref/arc-cavalier/qabarat-outrider"
kind = "archetype"
title = "Qabarat Outrider"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Qabarat%20Outrider"
source_ids = ["people-of-the-stars"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "qabarat_outrider", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "people-of-the-stars"
page = "11"

[fields]
kind = "archetype"
features = [
  { anchor = "combat-expertise", level = 1 },
  { anchor = "maneuver-tactics", level = 1 },
  { anchor = "mindlink", level = 5 },
  { anchor = "mindlink-pulse", level = 14 },
]
trades = [
  { replaces = "Tactician", feature = "tactician", by = ["maneuver-tactics"] },
  { replaces = "greater tactician", feature = "greater-tactician", by = ["maneuver-tactics"] },
  { replaces = "master tactician", feature = "master-tactician", by = ["maneuver-tactics"] },
  { replaces = "Banner", feature = "banner", by = ["mindlink"] },
  { replaces = "Greater banner", feature = "greater-banner", by = ["mindlink-pulse"] },
]
+++

The war colleges of the Castrovelian city-state of Qabarat produce a distinctive breed of cavalier
known as the Qabarat outrider. In defense of the lashunta city-states, outriders lead small units of
regular troops, the members of which can link minds with one another to form bonds in battle few can
match.

## Armor Proficiency {#armor-proficiency}

A Qabarat outrider does not gain proficiency with heavy armor.

## Combat Expertise {#combat-expertise}

At 1st level, a Qabarat outrider gains [Combat Expertise](ref/feat/combat-expertise) as a bonus
feat, even if he does not meet the prerequisites.

## Maneuver Tactics (Ex) {#maneuver-tactics}

At 1st level, a Qabarat outrider receives an Improved combat maneuver feat (such as
[Improved Feint](ref/feat/improved-feint)) as a bonus feat. He must meet the prerequisites for this
feat. As a standard action, a Qabarat outrider can grant this feat to all allies within 30 feet,
regardless of whether they can see or hear him or they meet the feat's prerequisites. Allies retain
this bonus feat for 3 rounds, plus 1 round for every 2 levels the Qabarat outrider possesses. An
outrider can use this ability once per day at 1st level, plus one additional time per day at 5th
level and for every 5 levels thereafter.

At 9th level, a Qabarat outrider gains an Improved or Greater combat maneuver feat (such as
[Greater Overrun](ref/feat/greater-overrun)) for which he meets the prerequisites as a bonus feat.
The outrider can grant this feat to his allies using the maneuver tactics ability. Using the
maneuver tactics ability becomes a swift action.

At 17th level, a Qabarat outrider gains an Improved, Greater, or Strike combat maneuver feat (such
as [Tripping Strike](ref/feat/tripping-strike); see Chapter 3 of the _Pathfinder RPG Advanced
Player's Guide_ for more details) as a bonus feat. He must meet the prerequisites for this feat. An
outrider can grant this feat to his allies using the maneuver tactics ability.

This ability replaces tactician, greater tactician, and master tactician.

## Mindlink (Su) {#mindlink}

At 5th level, a Qabarat outrider's innate telepathy develops into a mindlink, allowing contact
between himself and his allies and companions. As long as the Qabarat outrider is conscious, all
allies within range of his limited telepathy racial ability (30 feet for most Qabarat outriders)
receive a +2 morale bonus on saving throws against charm and compulsion effects and a +1 morale
bonus on attack rolls made while [flanking](ref/rule/flanking). At 10th level and every 5 levels
thereafter, these bonuses increase by 1. This ability replaces banner.

## Mindlink Pulse (Su) {#mindlink-pulse}

At 14th level, a Qabarat outrider can send a pulse of psychic energy through the minds of allies
within range of his limited telepathy as a standard action. If he does so during a surprise round,
any allies not normally able to act in the surprise round can act. If an ally would normally be
denied the ability to act in the surprise round, that ally's initiative is equal to her initiative
roll, or to the initiative of the outrider - 1, whichever is lower.

Whether or not it is a surprise round, when the outrider uses this ability, allies within range are
no longer flat-footed (assuming they were to begin with). This ability replaces greater banner.
