+++
id = "ref/rule/sanity-score-edge-and-thresholds"
kind = "rule"
title = "Sanity Score, Edge, and Thresholds"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sanity_score_edge_and_thresholds", path = "json/rules_campaign_types02.json" },
]

[fields]
kind = "none"
+++

**Sources:** Horror Adventures pg 12

Each creature has a sanity score, along with a sanity edge and a sanity threshold. These values
depend on the creature's current ability scores and ability damage. Increases and penalties to
ability scores (even temporary increases and penalties) adjust these numbers. Each discrete instance
in which a creature takes 1 or more points of sanity damage is called a sanity attack, regardless of
what caused the sanity damage.

Since effects that deal sanity damage are always mind-affecting effects, mindless creatures are
immune, and do not have a sanity score, sanity edge, or sanity threshold.

**Sanity Score:** Your sanity score is equal to the sum of your mental ability scores (Charisma,
Intelligence, and Wisdom) minus any ability damage taken to those ability scores.

**Sanity Threshold:** Your sanity threshold is equal to the bonus of your highest mental ability
score minus any ability damage to that score (minimum 0). When you experience a sanity attack, if
the sanity damage from that attack equals or exceeds your sanity threshold, you gain a
[madness](ref/rule/madness), either lesser or greater depending on the relation of your current
sanity damage and your sanity edge (see below).

If your sanity threshold is 0, you always suffer a madness upon taking 1 or more points of sanity
damage.

**Sanity Edge:** Your sanity edge is equal to 1/2 your sanity score. When you experience a sanity
attack that causes you to gain a madness (see Sanity Threshold above), compare your total amount of
sanity damage to your edge to determine the potency of the madness. If your current sanity damage is
less than your sanity edge, then you manifest a lesser madness. If your current sanity damage is
equal to or greater than your sanity edge, you manifest a greater madness instead. More information
on madness, both greater and lesser, can be found in its section. Furthermore, when you accrue total
sanity damage equal to or greater than your edge, any dormant lesser madnesses you have manifest
again.
