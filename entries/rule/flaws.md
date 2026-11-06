+++
id = "ref/rule/flaws"
kind = "rule"
title = "Flaws"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flaws", path = "json/rules_opt_magic01.json" },
]

[fields]
kind = "none"
+++

**Sources:** Pathfinder Unchained pg 190

Flaws are adjustments to an item that are detrimental in nature. Most are similar to curses, but not
nearly as damaging or restrictive to the bearer. Whenever a challenge would add a flaw to an item,
roll on the following table. In general, the more harmful flaws have higher numbers on the table.
Reroll duplicates and flaws that do not fit the item. Feel free to invent your own flaws or simply
choose an appropriate one.

**Accumulating Flaws:** The more flaws the item has, the more likely it is to become cursed. For
each flaw beyond the first, add a cumulative +5 modifier to the d% roll until the item gains a curse
(after which the +5 modifiers no longer apply). When you decide to create a new flaw or choose an
appropriate one rather than rolling, you should still roll first to determine whether the item gains
a curse instead.

|d%|Flaw|
| --- | --- |
|01-04|Heavy|
|05-08|Fragile|
|09-12|Vulnerable|
|13-16|Energy weakened|
|17-20|Pungent|
|21-24|Faerie-lit|
|25-28|Singing|
|29-32|Vindictive|
|33-36|Anomalous|
|37-40|Extremely infested|
|41-44|Addictive|
|45-48|Gluttonous|
|49-52|Slothful|
|53-56|Hallucinogenic|
|57-60|Obedient|
|61-64|Uncivilized|
|65-68|Allergic|
|69-72|Zealous|
|73-76|Impotent|
|77-80|Pacifistic|
|81-84|Backlashing|
|85-87|Wrathful|
|88-90|Proud|
|91-93|Slippery|
|94-96|Enticing|
|97-99|Paranoid|
|100+|Cursed|

**Addictive:** The owner does not want to give up the item under any circumstances, and suffers the
effects of [severe addiction](ref/rule/addiction) when denied access to the item.

**Allergic:** The item is especially sensitive to the presence of a particular type of creature, and
ceases all magical functions whenever it is within 30 feet of such a creature. To determine the
creature type, roll randomly or choose an appropriate type on the [ranger's](ref/class/ranger)
favored enemy list.

**Anomalous:** The item is instead another random magic item of the same type or slot and the same
or similar cost as the intended item.

**Backlashing:** When attacking with or activating the item, the user takes 1d6 points of damage
from magical energy backlash.

**Cursed:** The item gains a curse. Roll on [Table 15-27](ref/rule/common-cursed-item-effects) to
determine the curse, or choose an appropriate curse.

**Energy Weakened:** The item is particularly vulnerable to one random energy type. That energy type
ignores the item's [hardness](ref/umr/hardness) and deals double damage to the item (but not to the
item's bearer). Determine the energy type randomly, or choose one thematically tied to the challenge
that caused the item to have the weakness.

**Enticing:** Others covet the item and seek to possess it. Upon touching or examining the item, any
creature that does not possess the item must succeed at a DC 20 Will save or covet the item, seeking
to gain it by whatever means is most expedient and advantageous, though it need not do so
immediately. After one attempt to gain the item (or a successful save), a creature is immune to the
item's enticing effect for 24 hours.

**Extremely Infested:** As the infested quirk, but the vermin or other creatures crawl over the
bearer, requiring her to succeed at [concentration](ref/rule/concentration) checks (DC = 15 + the
spell's level) to cast spells or use other abilities that require concentration.

**Faerie-Lit:** The bearer is constantly surrounded by colorful light, as if affected by a
[faerie fire](ref/spell/faerie-fire) spell.

**Fragile:** The item has half as many hit points as normal.

**Gluttonous:** The bearer must gorge upon 10 times as much food as normal or suffer the effects of
starvation, ignoring effects that reduce the amount of food required (such as ring of sustenance).

**Hallucinogenic:** The bearer sees and hears mild hallucinations. While readily discernible as
such, these hallucinations still impose a -2 penalty on Perception and initiative checks.

**Heavy:** The item weighs twice as much as normal.

**Impotent:** The item's caster level is 1 lower than intended. If this would cause a wand or staff
to fall below the minimum required caster level, reroll this flaw.

**Obedient:** The bearer takes a -2 penalty on all Will saves against effects that exercise mental
control. This includes all mind-affecting charm or compulsion effects, as well as any effect the GM
deems appropriate.

**Pacifistic:** When using this weapon, the wielder can only choose to deal nonlethal damage (in
most cases imposing a -4 penalty on attack rolls), except against constructs and
undead.^[1](ref/rule/flaws#footnote-1)^

**Paranoid:** The bearer no longer trusts anyone and must attempt saving throws against all
abilities and spells but her own, even those that are harmless.

**Proud:** The bearer can't grant or gain any benefit from the aid another action.

**Pungent:** The item emits a foul and obvious odor. No mundane means can remove the stench, which
overcomes even magical effects such as negate aroma.

**Singing:** The item constantly sings in a loud belting soprano or tenor.
[Silence](ref/spell/silence) and other such spells can suppress the sound as normal.

**Slippery:** The creature holding the item must succeed at a DC 15 Reflex save each round or drop
the item.^[2](ref/rule/flaws#footnote-3)^

**Slothful:** The bearer must rest for 12 hours each day to gain the benefits of a full night's
rest, ignoring effects that reduce the amount of sleep needed (such as
[ring of sustenance](ref/magic-ring/ring-of-sustenance)). This can affect the bearer's ability to
prepare spells or regain spell slots.

**Uncivilized:** The item doesn't function in any area that would count as urban terrain.

**Vindictive:** When using this weapon, the wielder can only choose to deal lethal damage, not
nonlethal damage. If the item can normally deal only nonlethal damage, this flaw overrides that
restriction.^[1](ref/rule/flaws#footnote-1)^

**Vulnerable:** The item has a [hardness](ref/umr/hardness) that is 5 lower than usual (to a minimum
of 0).

**Wrathful:** In combat, the bearer's mind is clouded by rage, and she must succeed at a DC 20 Will
save to use any ability that can't be used during a barbarian rage. This doesn't allow a barbarian
to use those abilities when she is in a rage.

**Zealous:** The item functions only for worshipers of the creator's patron deity. If more than one
creator qualifies, roll randomly between their patron deities.^[3](ref/rule/flaws#footnote-2)^

###### ^1^ {#footnote-1}

Item must be a weapon.

###### ^3^ {#footnote-2}

Creator must have levels in a divine spellcasting class and have a patron deity.

###### ^2^ {#footnote-3}

Item must be a held item.
