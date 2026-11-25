+++
id = "ref/arc-bard/court-bard"
kind = "archetype"
title = "Court Bard"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Court%20Bard"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "court_bard", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "advanced-players-guide"
page = "81"

[fields]
kind = "archetype"
features = [
  { anchor = "bardic-performance" },
  { anchor = "satire", level = 1 },
  { anchor = "mockery" },
  { anchor = "glorious-epic" },
  { anchor = "scandal" },
  { anchor = "heraldic-expertise", level = 1 },
  { anchor = "wide-audience", level = 5 },
]
trades = [
  { replaces = "Inspire courage", feature = "bardic-performance", power = "inspire courage", by = ["satire"] },
  { replaces = "Inspire competence", feature = "bardic-performance", power = "inspire competence", by = ["mockery"] },
  { replaces = "Dirge of doom", feature = "bardic-performance", power = "dirge of doom", by = ["glorious-epic"] },
  { replaces = "Frightening tune", feature = "bardic-performance", power = "frightening tune", by = ["scandal"] },
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["heraldic-expertise"] },
  { replaces = "Lore master", feature = "lore-master", by = ["wide-audience"] },
  { replaces = "jack of all trades", feature = "jack-of-all-trades", by = ["wide-audience"] },
]
+++

Spending years studying all of the finer points of erudition and etiquette, the court bard takes up
the role of resplendent proclaimer and artist-in-residence at the hand of nobility, royalty, and the
well-moneyed elite who aspire to join their ranks.

## Bardic Performance {#bardic-performance}

A court bard gains the following types of bardic performance.

## Satire (Su) {#satire}

A court bard can use performance to undermine the confidence of enemies who hear it, causing them to
take a -1 penalty on attack and damage rolls (minimum 1) and a -1 penalty on saves against fear and
charm effects as long as the bard continues performing. This penalty increases by -1 at 5th level
and every six levels thereafter. Satire is a language-dependent, mind-affecting ability that uses
audible components. This performance replaces inspire courage.

## Mockery (Su) {#mockery}

A court bard of 3rd level or higher can subtly ridicule and defame a specific individual. The bard
selects one target who can hear his performance. That individual takes a -2 penalty on Charisma
checks and Charisma-related skill checks as long as the bard continues performing. This penalty
increases by -1 every four levels after 3rd. Mockery is a language-dependent, mind-affecting ability
that relies on audible components. This performance replaces inspire competence.

## Glorious Epic (Su) {#glorious-epic}

A court bard of 8th level or higher can weave captivating tales that engross those who hear them.
Enemies within 30 feet become [flat-footed](ref/rule/flat-footed) unless they succeed at a Will save
(DC 10 + 1/2 the bard's level + the bard's Cha modifier). A save renders them immune to this ability
for 24 hours. Glorious epic is a language-dependent, mind-affecting ability that uses audible
components. This performance replaces dirge of doom.

## Scandal (Su) {#scandal}

A court bard of 14th level or higher can combine salacious gossip and biting calumny to incite a
riot. Each enemy within 30 feet is affected as if by a
_[song of discord](ref/spell/song-of-discord)_ for as long as it can hear the performance. A
successful Will save (DC 10 + 1/2 the bard's level + the bard's Cha modifier) negates the effect,
and that creature is immune to this ability for 24 hours. Scandal is a language-dependent,
mind-affecting ability that uses audible components. This performance replaces frightening tune.

## Heraldic Expertise (Ex) {#heraldic-expertise}

A court bard gains a bonus equal to half his bard level on Diplomacy, Knowledge (history), Knowledge
(local), and Knowledge (nobility) checks (minimum +1). Once per day, the court bard can also reroll
a check against one of these skills, though he must take the result of the second roll even if it is
worse. He can reroll one additional time per day at 5th level and every five levels thereafter. This
ability replaces bardic knowledge.

## Wide Audience (Su) {#wide-audience}

At 5th level, a court bard can choose to affect a 60-foot cone instead of a 30-foot radius with
bardic performances that affect an area. In addition, for every five levels beyond 5th, the area of
such powers is increased by 10 feet (radius) or 20 feet (cone). If the power instead affects
multiple creatures, it affects one additional creature than normal for every five levels beyond 5th.
This does not affect powers that affect only a single creature. This ability replaces lore master
and jack of all trades.
