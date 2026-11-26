+++
id = "ref/arc-fighter/unbreakable"
kind = "archetype"
title = "Unbreakable"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Unbreakable"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unbreakable", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "ultimate-combat"
page = "49"

[fields]
kind = "archetype"
features = [
  { anchor = "tough-as-nails", level = 1 },
  { anchor = "unflinching", level = 2 },
  { anchor = "heroic-recovery", level = 5 },
  { anchor = "heroic-defiance", level = 9 },
  { anchor = "quick-recovery", level = 11 },
  { anchor = "stalwart", level = 13 },
  { anchor = "unlimited-endurance", level = 15 },
  { anchor = "miraculous-recovery", level = 17 },
  { anchor = "unbreakable-mind", level = 20 },
]
trades = [
  { replaces = "The fighter's 1st-level bonus feat", feature = "bonus-feats", levels = [1], by = ["tough-as-nails"] },
  { replaces = "Bravery", feature = "bravery", by = ["unflinching"] },
  { replaces = "Weapon training 1", feature = "weapon-training", levels = [5], by = ["heroic-recovery"] },
  { replaces = "Weapon training 2", feature = "weapon-training", levels = [9], by = ["heroic-defiance"] },
  { replaces = "Armor training 3", feature = "armor-training", levels = [11], by = ["quick-recovery"] },
  { replaces = "Weapon training 3", feature = "weapon-training", levels = [13], by = ["stalwart"] },
  { replaces = "Armor training 4", feature = "armor-training", levels = [15], by = ["unlimited-endurance"] },
  { replaces = "Weapon training 4", feature = "weapon-training", levels = [17], by = ["miraculous-recovery"] },
  { replaces = "Weapon mastery", feature = "weapon-mastery", by = ["unbreakable-mind"] },
]
+++

The unbreakable is a warrior of indomitable will, unstoppable and implacable once he has set his
mind upon a course of action. The unbreakable endures any trial to do what must be done, and when
his mind is set toward a goal, nothing can stop him from achieving it, though many may try. He is a
juggernaut and a zealot, supremely confident in his own abilities.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

An unbreakable is not proficient with tower shields.

## Tough as Nails {#tough-as-nails}

An unbreakable gains [Endurance](ref/feat/endurance) and [Diehard](ref/feat/diehard) as bonus feats.
This ability replaces the fighter's 1st-level bonus feat.

## Unflinching (Ex) {#unflinching}

At 2nd level, an unbreakable gains a +1 bonus on Will saves against mind-affecting effects. This
bonus increases by +1 for every four levels after 2nd level (to a maximum of +5 at 18th level). This
ability replaces bravery.

## Heroic Recovery (Ex) {#heroic-recovery}

At 5th level, an unbreakable gains the [Heroic Recovery](ref/feat/heroic-recovery) feat (_Advanced
Player's Guide_ 162) as a bonus feat, if he does not have it already. If he already has this feat,
the unbreakable can choose any combat feat instead. In addition, he may use this feat one additional
time per day for every four levels after 5th (to a maximum of 4 times per day at 17th level). This
ability replaces weapon training 1.

## Heroic Defiance (Ex) {#heroic-defiance}

At 9th level, an unbreakable gains the [Heroic Defiance](ref/feat/heroic-defiance) feat (_Advanced
Player's Guide_ 162) as a bonus feat, if he does not have it already. If he already has this feat,
the unbreakable can choose any combat feat instead. In addition, he may use this feat one additional
time per day for every four levels after 9th (to a maximum of 3 times per day at 19th level). This
ability replaces weapon training 2.

## Quick Recovery (Ex) {#quick-recovery}

At 11th level, an unbreakable needs only 15 minutes of rest or to be subject to a healing spell or
effect to recover from the [fatigued](ref/misc/fatigued) condition. This ability replaces armor
training 3.

## Stalwart (Ex) {#stalwart}

At 13th level, when an unbreakable succeeds on a Fortitude or Will save against a spell or
[spell-like ability](ref/umr/spell-like-abilities) that has a partial effect even on a successful
save, he is completely unaffected by it. This ability replaces weapon training 3.

## Unlimited Endurance (Ex) {#unlimited-endurance}

At 15th level, when an unbreakable is [exhausted](ref/misc/exhausted), he only suffers the effects
of the fatigued condition instead, but does require 1 hour of rest to reduce this condition to the
actual fatigued condition. This ability replaces armor training 4.

## Miraculous Recovery (Ex) {#miraculous-recovery}

At 17th level, when an unbreakable makes a saving throw to recover from an ongoing effect, he may
roll twice and choose the better roll. This ability replaces weapon training 4.

## Unbreakable Mind (Ex) {#unbreakable-mind}

At 20th level, an unbreakable becomes nearly impossible to sway with honeyed words or magic. He
gains immunity to mind-affecting effects. This ability replaces weapon mastery.
