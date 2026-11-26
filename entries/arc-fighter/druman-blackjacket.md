+++
id = "ref/arc-fighter/druman-blackjacket"
kind = "archetype"
title = "Druman Blackjacket"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Druman%20Blackjacket"
source_ids = ["inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "druman_blackjacket", path = "json/archetypes_fighter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "inner-sea-combat"
page = "36"

[fields]
kind = "archetype"
features = [
  { anchor = "well-paid-loyalty", level = 2 },
  { anchor = "blackjacket-tactics", level = 4 },
  { anchor = "amateurs", level = 8 },
  { anchor = "superior-tactics", level = 12 },
  { anchor = "esprit-de-corps", level = 16 },
]
trades = [
  { replaces = "Bravery", feature = "bravery", by = ["well-paid-loyalty"] },
  { replaces = "The bonus feat gained at 4th level", feature = "bonus-feats", levels = [4], by = ["blackjacket-tactics"] },
  { replaces = "The bonus feat gained at 8th level", feature = "bonus-feats", levels = [8], by = ["amateurs"] },
  { replaces = "The bonus feat gained at 12th level", feature = "bonus-feats", levels = [12], by = ["superior-tactics"] },
  { replaces = "The bonus feat gained at 16th level", feature = "bonus-feats", levels = [16], by = ["esprit-de-corps"] },
]
+++

Known as the Blackjackets, the elite soldiers of Druma are and always have been mercenaries rather
than a standing army. Still, gold buys loyalty, and the Kalistocrats pay best of all. As a result,
the Blackjackets are well equipped and dedicate themselves to training in small-unit tactics,
quickly communicating strategies and tricks to handle any threat to their charges.

## Bonus Feats {#bonus-feats}

In addition to combat feats, a Druman Blackjacket can choose
[Improved Iron Will](ref/feat/improved-iron-will), [Iron Will](ref/feat/iron-will), or any teamwork
feat as bonus feats.

## Well-Paid Loyalty (Ex) {#well-paid-loyalty}

At 2nd level, a Druman Blackjacket gains a +1 bonus on Will saves against compulsion spells,
[spell-like abilities](ref/umr/spell-like-abilities), and effects. This bonus increases by 1 for
every 4 levels the Blackjacket possesses beyond 2nd. This ability replaces bravery.

## Blackjacket Tactics (Ex) {#blackjacket-tactics}

At 4th level, two or more Druman Blackjackets can spend 1 minute discussing strategy, then choose a
single teamwork feat (_Advanced Player's Guide_ 150) possessed by at least one of them. For a number
of hours equal to the class level of the highest-level Blackjacket, the participants each gain the
benefits of the selected feat even if they do not meet the feat's prerequisites. If a creature
benefiting from this ability moves more than 30 feet away from any other participant, it loses all
benefits of this ability until it is again within 30 feet. Creatures that do not have levels in this
archetype can't benefit from this ability, and no creature can benefit from this ability more than
once at any given time. This ability replaces the bonus feat gained at 4th level.

## Amateurs! (Ex) {#amateurs}

At 8th level, when using the Blackjacket tactics ability, a Druman Blackjacket can include one or
more creatures without levels in this archetype, but doing so reduces the duration of the effect to
a number of minutes equal to the class level of the highest-level Blackjacket instead of a number of
hours per level. If only Blackjackets are included in the effect, all Druman Blackjackets affected
gain a +1 morale bonus on skill checks and saving throws for the duration of the effect. This
ability replaces the bonus feat gained at 8th level.

## Superior Tactics (Ex) {#superior-tactics}

At 12th level, a Druman Blackjacket who uses the Blackjacket tactics ability can allow all affected
Blackjackets to gain a second bonus teamwork feat possessed by at least one of the participants.
This ability replaces the bonus feat gained at 12th level.

## Esprit de Corps (Ex) {#esprit-de-corps}

At 16th level, a Druman Blackjacket grants all Blackjackets with whom he is sharing one or more
teamwork feats through the Blackjacket tactics ability a +2 morale bonus on attack rolls, ability
checks, skill checks, and saving throws. Each affected Blackjacket increases this bonus by 1 if
another affected Blackjacket has been reduced to 0 or fewer hit points since the beginning of his
last turn. This ability replaces the bonus feat gained at 16th level.
