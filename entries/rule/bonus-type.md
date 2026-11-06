+++
id = "ref/rule/bonus-type"
kind = "rule"
title = "Bonus Type"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bonus_type", path = "json/rules_adv_magic01.json" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Magic pg 134

There are many types of bonuses in the game. It's tempting to look at that list of bonuses, find
"holes" in the spell list that don't have spells for certain bonus types, and create a new spell
that adds one of those unused bonus types to your favorite statistic or roll. Resist this
temptation. Not all bonus types are equal within the game, and many bonus types are only meant for
certain things. See Table 2-7: Bonus Types and Effects.

A dash entry (-) in the table indicates there are no common examples of items or spells that grant
that kind of bonus. If you're designing an item or spell and want to include a certain type of bonus
to a particular ability or statistic, check Table 2-7 first; if the bonus type doesn't say it can
affect that ability or statistic, use one that does instead. One reason for this table is that some
bonuses are better than others (deflection bonuses work against incorporeal creatures and when you
are flat-footed, natural armor bonuses do not). A second reason is that allowing any kind of bonus
on any roll or statistic makes it really easy to stack many small bonuses more cheaply than a larger
bonus, which makes powerful magic items like a ring of protection +5 much less interesting. A third
reason is that some of these combinations just don't make sense, like a deflection bonus to Strength
or a shield bonus on Knowledge checks.

### Table 2-7: Bonus Types and Effects

|Bonus Type|Can Affect|Sample Item|Sample Spell|
| --- | --- | --- | --- |
|Alchemical|Ability scores, saves|Antitoxin|-|
|Armor|AC|[Bracers of armor](ref/magic-wondrous/bracers-of-armor)|[Mage armor](ref/spell/mage-armor)|
|Circumstance|Attacks, checks|[Robe of blending](ref/magic-wondrous/robe-of-blending)|-|
|Competence|Attacks, checks, saves|[Boots of elvenkind](ref/magic-wondrous/boots-of-elvenkind)|[Guidance](ref/spell/guidance)|
|Deflection|AC|[Ring of protection](ref/magic-ring/ring-of-protection)|-|
|Dodge|AC|Never\*|Never\*|
|Enhancement|Ability scores, AC, attacks, damage, speed|[Belt of giant strength](ref/magic-wondrous/belt-of-giant-strength)|[Magic weapon](ref/spell/magic-weapon)|
|Inherent|Ability scores|[Manual of bodily health](ref/magic-wondrous/manual-of-bodily-health)|[Wish](ref/spell/wish)|
|Insight|AC, attacks, checks, saves|[Dusty rose prism ioun stone](ref/magic-ioun/dusty-rose-prism)|[True strike](ref/spell/true-strike)|
|Luck|AC, attacks, checks, damage, saves|[Stone of good luck](ref/magic-wondrous/stone-of-good-luck-luckstone)|[Divine favor](ref/spell/divine-favor)|
|Morale|Attacks, checks, damage, saves, Str, Con, Dex|[Candle of invocation](ref/magic-wondrous/candle-of-invocation)|[Bless](ref/spell/bless)|
|Natural armor|AC|[Amulet of natural armor](ref/magic-wondrous/amulet-of-natural-armor)|[Barkskin](ref/spell/barkskin)|
|Profane|AC, checks, damage, DCs, saves|-|[Desecrate](ref/spell/desecrate)|
|Resistance|Saves|[Cloak of resistance](ref/magic-wondrous/cloak-of-resistance)|[Mind blank](ref/spell/mind-blank)|
|Sacred|AC, checks, damage, DCs, saves|-|[Consecrate](ref/spell/consecrate)|
|Shield|AC|[Ring of force shield](ref/magic-ring/ring-of-force-shield)|[Shield](ref/spell/shield)|
|Size|Ability scores, attacks, AC|-|[Enlarge person](ref/spell/enlarge-person)|

\* Spells and magic items should never grant dodge bonuses because dodge bonuses always stack, and
it would be a simple matter achieving that AC using the armor, deflection, enhancement, and natural
armor bonuses in the game.
