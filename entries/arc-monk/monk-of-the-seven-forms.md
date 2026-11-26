+++
id = "ref/arc-monk/monk-of-the-seven-forms"
kind = "archetype"
title = "Monk of the Seven Forms"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Monk%20of%20the%20Seven%20Forms"
source_ids = ["inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "monk_of_the_seven_forms", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "inner-sea-combat"
page = "40"

[fields]
kind = "archetype"
features = [
  { anchor = "lightning-finish", level = 1 },
  { anchor = "endurance", level = 3 },
  { anchor = "sirocco-fury", level = 11 },
]
trades = [
  { replaces = "Stunning fist", feature = "stunning-fist", by = ["lightning-finish"] },
  { replaces = "Maneuver training", feature = "maneuver-training", by = ["endurance"] },
  { replaces = "Abundant step", feature = "abundant-step", by = ["sirocco-fury"] },
  { replaces = "quivering palm", feature = "quivering-palm", by = ["sirocco-fury"] },
]
+++

When Tian monks founded the Monastery of the Seven Forms near the present border between Qadira and
Taldor, they did so as a challenge to prospective students to travel great distances and prove their
devotion before training within the monastery's walls. Over the centuries, the monastery has fallen
under Qadiran control many times, and the original seven forms for which the monastery was named
have been lost to history. In their place, the monks of the isolated sanctuary now teach a style
featuring lightning-fast strikes that mimic both dervish dances and the searing winds of the arid
desert, favoring mobility and endurance.

## Bonus Feats {#bonus-feats}

A monk of the seven forms loses the ability to take [Improved Disarm](ref/feat/improved-disarm),
[Improved Feint](ref/feat/improved-feint), [Improved Grapple](ref/feat/improved-grapple), and
[Improved Trip](ref/feat/improved-trip) as bonus feats. He adds
[Nimble Moves](ref/feat/nimble-moves) to his list of bonus feats. At 6th level, he also adds
[Acrobatic Steps](ref/feat/acrobatic-steps) and [Wind Stance](ref/feat/wind-stance) to his list of
bonus feats. At 10th level, he adds [Lightning Stance](ref/feat/lightning-stance) to his list of
bonus feats.

## Lightning Finish (Ex) {#lightning-finish}

At 1st level, as an immediate action, a monk of the seven forms can make a single attack with a
manufactured light or one-handed slashing weapon he is currently wielding against any target he has
successfully hit at least twice with his unarmed strike during his turn. This attack deals normal
damage but without the normal Strength bonus to damage.

At 4th level, he can take a 5-foot step before or after performing a lightning finish so long as he
ends adjacent to his target, though if he takes this step, he cannot perform a 5-foot step during
his next turn. At 8th level, he applies his full Strength bonus to his damage roll for the extra
attack, even if he made the attack with an off-hand weapon or with a weapon wielded in two hands. At
12th level, if he hit the target at least three times with his unarmed strike during his turn,
taking the 5-foot step granted by lightning finish does not prevent him from taking a 5-foot step
during his next turn.

A monk of the seven forms can use this ability a number of times per day equal to his monk level,
but no more than once per round. This ability replaces stunning fist.

## Endurance (Ex) {#endurance}

At 3rd level, a monk of the seven forms gains [Endurance](ref/feat/endurance) as a bonus feat. This
ability replaces maneuver training.

## Sirocco Fury (Su) {#sirocco-fury}

At 11th level, a monk of the seven forms can spend 2 ki points as a full-round action to enter a
meditative trance that replicates the spell
_[dance of a hundred cuts](ref/spell/dance-of-a-hundred-cuts)_, using his monk level as his caster
level. Unlike the spell, a monk of the seven forms must both move 10 feet and make a melee attack
each round after he begins this trance to prevent the effect from ending. At 15th level, he can
instead spend 3 ki points when using this ability to make his trance replicate
_[dance of a thousand cuts](ref/spell/dance-of-a-thousand-cuts)_ with the same limitations. This
ability replaces abundant step and quivering palm.
