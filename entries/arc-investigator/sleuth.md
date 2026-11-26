+++
id = "ref/arc-investigator/sleuth"
kind = "archetype"
title = "Sleuth"
aon = "ArchetypeDisplay.aspx?FixedName=Investigator%20Sleuth"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sleuth", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "advanced-class-guide"
page = "101"

[fields]
kind = "archetype"
features = [
  { anchor = "sleuth-s-luck", level = 1 },
  { anchor = "deeds", level = 1 },
  { anchor = "daring", level = 1 },
  { anchor = "opportunistic-evasion", level = 1 },
  { anchor = "sleuth-s-initiative", level = 1 },
  { anchor = "make-it-count" },
  { anchor = "run-like-hell", level = 4 },
  { anchor = "second-chance", level = 4 },
]
trades = [
  { replaces = "Alchemy", feature = "alchemy", by = ["sleuth-s-luck"] },
  { replaces = "Swift alchemy", feature = "swift-alchemy", by = ["sleuth-s-initiative"] },
]
+++

A sleuth is an investigator who relies on good fortune and guile rather than alchemy. Having no
mystical energy intrinsic to her, she must forgo the more magical aspects of alchemy to solve her
mysteries with wits, gumption, and the fickle consideration of luck.

## Sleuth's Luck (Ex) {#sleuth-s-luck}

At 1st level, a sleuth gains a fluctuating pool of luck, measuring her ability to get out of
scrapes. At the start of each day, a sleuth has a number of luck points equal to her Charisma
modifier (minimum 1). Her luck goes up or down throughout the day, but usually cannot go higher than
her Charisma modifier (minimum 1), though feats, magic items, and spells that grant either
[grit](ref/class/gunslinger) or [panache](ref/class/swashbuckler) points can also grant a sleuth
luck points equal to the amount of grit or panache they grant. A sleuth spends luck to accomplish
deeds (see below), and regains luck in the following ways.

_Rolling a Natural 20 on a Knowledge or Sense Motive Check_: While on an investigation, a sleuth
regains luck by uncovering secrets. Rolling a natural 20 on these skill checks while actively
investigating causes the sleuth to regain 1 luck point. Such skill checks made for more mundane
reasons (such as normal research or using Sense Motive to gain information during normal bargaining
or while gambling) do not regain luck for the sleuth. Determining which skill checks qualify is up
to the GM.

_Rolling a 6 or Higher on an Inspiration Roll_: When a sleuth rolls an inspiration die while on an
investigation and the die comes up a 6 or higher, she regains 1 luck point. (If she rolls multiple
inspiration dice at a time, she regains 1 luck point if the total is 6 or higher.) Like regaining
luck via a natural 20 on a qualifying skill check, inspiration checks made for more mundane reasons
don't qualify for regaining luck. The GM is the final arbitrator for what rolls qualify. It's
possible for an investigator to regain 2 luck points on the same Skill check, if both the qualifying
skill check is a natural 20 and any inspiration roll made is a 6 or higher.

This and the 1st-level deeds below replace alchemy. A sleuth cannot take the
[alchemist discovery](ref/invtalent/alchemist-discovery) talent or any investigator talent that
affects alchemy.

## Grit, Luck, and Panache {#grit-luck-and-panache}

Grit, luck, and panache represent three different means by which heroes can gain access to the same
heroic pool, using it to accomplish fantastic feats. For characters with a mix of grit, luck, and
panache, they pool the three resources together into a combined pool. (Those who use panache and
luck do not gain twice their Charisma bonus in their pool.) For feats, magic items, and other
effects, a panache user can spend and gain luck points in place of grit or panache points, and vice
versa.

A luck user does not count as a grit or panache user to satisfy feat prerequisites.

## Deeds {#deeds}

Sleuths spend luck points to accomplish deeds. Most deeds grant a sleuth some momentary bonus or
effect, but there are some that provide longer-lasting effects. Some deeds stay in effect as long as
a sleuth has at least 1 luck point.

At 1st level, a sleuth gains the following deeds.

## Daring (Ex) {#daring}

At 1st level, a sleuth can spend 1 luck point when he makes an Acrobatics, Climb, Escape Artist,
Fly, Ride, or Swim check to roll d6 and add the result to the check. He can choose to add this die
after he rolls. If the d6 roll is a natural 6, he rolls another d6 and adds it to the check. He can
continue to do this as long as he rolls natural 6s, up to a number of times equal to his
Intelligence modifier (minimum 1).

## Opportunistic Evasion (Ex) {#opportunistic-evasion}

At 1st level, when a sleuth succeeds at a Reflex saving throw against an effect that still deals
damage on a successful save, he can spend 1 luck point as an immediate action to instead take no
damage for that effect.

## Sleuth's Initiative (Ex) {#sleuth-s-initiative}

At 1st level, as long as the sleuth has at least 1 luck point, he gains a +2 bonus on initiative
checks. Furthermore, if he has the [Quick Draw](ref/feat/quick-draw) feat, his hands are free and
unrestrained, and the weapon is not hidden, he can draw a single light or one-handed melee weapon as
part of the initiative check. (Unlike with swashbuckler deeds, this does not have to be a piercing
weapon.)

At 4th level, a sleuth gains the following deeds. These abilities replace swift alchemy.

## Make It Count (Ex) {#make-it-count}

When a sleuth uses studied strike, he can spend 1 luck point to apply an investigator talent that he
doesn't already know and which affects studied strike to his studied strike. He must be able to
fulfill that talent's prerequisites.

## Run Like Hell (Ex) {#run-like-hell}

At 4th level, a sleuth can spend 1 luck point to gain a +20-foot bonus to his speed for 1 minute.
Furthermore, while under the effect of this bonus, if he moves more than his normal speed in a
round, he gains a +4 bonus to AC until the start of his next turn.

## Second Chance (Ex) {#second-chance}

At 4th level, when a sleuth rolls an inspiration die or uses daring deed, he can spend 1 luck point
to reroll either the inspiration or the daring deed die. If he rolls a 6 or higher on this reroll,
he does not regain a luck point, and no matter what he rolls on either roll, he must keep the reroll
result, even if it is lower.

## Investigator Talents {#investigator-talents}

The following investigator talents complement the sleuth archetype:
[amazing inspiration](ref/invtalent/amazing-inspiration),
[combat inspiration](ref/invtalent/combat-inspiration),
[device talent](ref/invtalent/device-talent), [effortless aid](ref/invtalent/effortless-aid),
[expanded inspiration](ref/invtalent/expanded-inspiration),
[hidden agendas](ref/invtalent/hidden-agendas),
[inspirational expertise](ref/invtalent/inspirational-expertise),
[inspired alertness](ref/invtalent/inspired-alertness),
[inspired intimidator](ref/invtalent/inspired-intimidator),
[perceptive tracking](ref/invtalent/perceptive-tracking), [quick study](ref/invtalent/quick-study),
[rogue talent](ref/invtalent/rogue-talent),
[tenacious inspiration](ref/invtalent/tenacious-inspiration), and
[underworld inspiration](ref/invtalent/underworld-inspiration).
