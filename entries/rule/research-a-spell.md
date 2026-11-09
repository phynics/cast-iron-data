+++
id = "ref/rule/research-a-spell"
kind = "rule"
title = "Research a Spell"
source_ids = ["ultimate-campaign"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "research_a_spell", path = "json/rules_subsystems02.json" },
]
[[sources]]
publication = "ultimate-campaign"
page = "86"

[fields]
kind = "none"
+++

The Core Rulebook allows you to perform spell research, either to create a new spell or learn an
existing spell from another source. In the downtime system, the steps for spell research each day
are as follows.

1. Pay 100 gp × the spell's level for research costs and rare ingredients. You may
  [spend Goods or Magic](ref/rule/spend-capital-to-boost-checks) toward this cost.
1. Determine the total days of progress required to complete the research, which is 7 × the spell
  level.
1. Determine the spell research DC, which is 10 + twice the spell's level.
1. Attempt a Spellcraft check and a Knowledge check (arcana for an arcane spell, religion for a
  divine spell) against the spell research DC. You can't take 10 on these checks. You may spend
  Magic to modify a check result, with 1 point of Magic adding 2 to your total (maximum +10). If
  both checks succeed, you make 1 day's progress toward completing the spell. When your days of
  progress equal the total number of days needed, the spell is completed and added to your spellbook
  or list of spells known.

If either or both spell research checks fail by 4 or less, you make no progress. For each check that
fails by 5 or more, your research has led to poor results and you lose a day of progress toward
completing the spell.

If you're an alchemist, you can use this downtime option to research a new extract formula. Instead
of a Spellcraft check, attempt a Craft (alchemy) check. For Knowledge (arcana) checks, you may
attempt a Knowledge (nature) check instead.
