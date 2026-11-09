+++
id = "ref/rule/battle-phase"
kind = "rule"
title = "Battle Phase"
source_ids = ["pathfinder-59-the-price-of-infamy"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "battle_phase", path = "json/rules_campaign_types10.json" },
]
[[sources]]
publication = "pathfinder-59-the-price-of-infamy"
page = "67"

[fields]
kind = "none"
+++

At the start of a battle phase, each fleet's admiral makes a
[Profession (sailor)](ref/skill/profession-any) check to determine initiative. The admiral whose
result is higher gains the upper hand in that battle phase, which grants all of his squadrons a +1
bonus on attack rolls. This Profession (sailor) check is made at the start of each battle phase.

Each fleet then takes turns making attacks with their squadrons. The winner of the initiative roll
gets to make the first attack, using any one of his squadrons. The other fleet then makes its first
attack, using any one of its squadrons. Attacks with squadrons go back and forth during the battle
phase until all squadrons able to attack have done so - a single squadron can only attack once per
battle phase. If one fleet has more squadrons than the other, the additional squadrons attack at the
end of the battle phase after the other fleet has used up all of its attacks for that round.

**Attacking:** When you attack with a squadron, pick one of the enemy fleet's squadrons as your
target. Roll 1d20 and add that squadron's attack value. If the result equals or exceeds the enemy
squadron's Defense Value, you deal damage as appropriate for your squadron. If you miss, you still
deal 1d4-1 points of damage (damage from a miss can never be increased by any other effect). This
damage is an abstract combination of siege weapons, ramming, spellcasting, missile fire, and even
boarding actions against enemy crews.

**Assigning Damage:** The damaged fleet normally gets to assign its damage by marking (either by
crossing out of by placing a marker such as a die, penny, or some other counter) the amount of
damage on the targeted squadron. This damage doesn't all have to be on the same ship - you can
spread it out in any way you wish among all of the nonsunken ships in your squadron.

**Critical Hits and Fumbles:** A natural 20 on an attack roll always hits and allows you to assign
damage to the enemy as you wish, rather than allowing the defender to allocate it (you do not deal
double damage with a critical hit, though). A natural 1 always misses entirely (and results in no
damage at all to the enemy fleet). Every time a squadron scores a critical hit, its morale score
increases by 1; each time it rolls a fumble, its morale score decreases by 1.

**Effects of Damage:** Each point of damage reduces a squadron's total hits. When a particular ship
takes an amount of damage equal to its hits, it becomes disabled. A disabled ship does not count
toward its squadron's damage rolls, and increases that squadron's loss count by +1. A ship that
takes damage while it is disabled sinks and is removed entirely from the fleet, increasing that
squadron's loss count by +1.

**Losing a Squadron:** Each time you lose an entire squadron (as a result of either damage or
mutiny), increase the loss count for each surviving squadron by +1.

**Abandoning Ship:** For simplicity's sake, you can assume that a commodore's ship is the last to
sink in any squadron. Note that not all characters on a sinking ship automatically perish.
Typically, a ship sinks slowly enough that officers and crew can abandon ship, and there's usually
ship's boats and other pieces of wreckage to grab onto. Once a battle is over, you can assume that
any significant characters who were on a sinking ship survive, either by escaping in a boat, by
clinging to flotsam, or by fleeing via magical means. The ultimate fate of a significant character
on a sunken ship depends more on the results of the actual battle itself. If the imperiled
character's fleet wins, she can be rescued after the battle, but if her fleet loses, the best she
may be able to look forward to is capture by the enemy - more often, such victims are merely left to
perish via the countless methods the sea presents for death.
