+++
id = "ref/arc-bard/solacer"
kind = "archetype"
title = "Solacer"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Solacer"
source_ids = ["healers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "solacer", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "healers-handbook"
page = "18"

[fields]
kind = "archetype"
features = [
  { anchor = "learned-physician", level = 1 },
  { anchor = "inspire-tenacity", level = 1 },
  { anchor = "creative-treatment", level = 2 },
  { anchor = "invigorating-artistry", level = 10 },
]
trades = [
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["learned-physician"] },
  { replaces = "lore master", feature = "lore-master", by = ["learned-physician"] },
  { replaces = "Countersong", feature = "bardic-performance", power = "countersong", by = ["inspire-tenacity"] },
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["creative-treatment"] },
  { replaces = "Jack-of-all-trades", feature = "jack-of-all-trades", by = ["invigorating-artistry"] },
  { alters = "Class skills" },
]
+++

Solacers are experts in the healing arts as well as creators of performances that console the
distraught, rally the stricken, raise spirits, and vanquish sorrow.

## Class Skills {#class-skills}

A solacer adds Heal to his list of class skills instead of Appraise.

This alters the bard's class skills.

## Learned Physician (Ex) {#learned-physician}

A solacer adds 1/2 his class level (minimum 1) on Heal checks and can attempt Knowledge checks
untrained.

At 5th level, a solacer can take 10 on checks with any Knowledge skill he has ranks in. The solacer
can choose not to take 10 and can instead roll normally. In addition, once per day, the solacer can
take 20 on any Heal check, though this does not affect the time it takes to perform the task
attempted. He can use this ability one additional time per day for every 6 bard levels he has beyond
5th, to a maximum of three times per day at 17th level.

This ability replaces bardic knowledge and lore master.

## Inspire Tenacity (Su) {#inspire-tenacity}

At 1st level, a solacer can use his bardic performances to bolster his allies' mental endurance when
they need it most. All allies within 30 feet automatically stabilize if they are
[dying](ref/misc/dying) and gain a +2 morale bonus on saving throws against mind-affecting effects,
poisons, and disease. This performance relies on audible components.

This bardic performance replaces countersong.

## Creative Treatment (Su) {#creative-treatment}

Beginning at 2nd level, once per day when a solacer attempts a Heal check and fails, he can
immediately reroll the check and take the better result. He can use this ability one additional time
per day at 6th level and every 4 bard levels thereafter (to a maximum of five times per day at 18th
level).

Additionally, when acting as a confidante (or any other type of advisor) to
[reduce sanity damage with rest](ref/rule/reducing-sanity-damage), the solacer can attempt a
Charisma check instead of an Intelligence or Wisdom check and add his Charisma modifier to the
amount of sanity damage removed instead of his Intelligence or Wisdom modifier. When acting as a
confidante (or any other type of advisor) to reduce a [madness's](ref/rule/madness) DC with rest
(_Horror Adventures_ 182), the solacer can attempt a Charisma check instead of an Intelligence or
Wisdom check and reduce the madness's DC by 1/2 his Charisma modifier instead of 1/2 his
Intelligence or Wisdom modifier.

This ability replaces versatile performance.

## Invigorating Artistry (Su) {#invigorating-artistry}

At 10th level, a solacer can use his performances to protect and heal a target's soul. The solacer
can perform for 1 hour (this requires no skill check) and grant several benefits for 24 hours to the
creatures that can hear or see his performance, or both, depending on whether the performance has
audible or visual components. Affected creatures gain a +3 bonus on saving throws against curses,
possession spells and effects (such as _[magic jar](ref/spell/magic-jar)),_ and domination and mind
control spells and effects (such as _[dominate person](ref/spell/dominate-person)_). If the target
is suffering any or multiple such effects, it immediately can attempt a new saving throw against
each; the effect ends if the saving throw is successful. Only one such extra saving throw can be
granted against each condition in any 24-hour period. If a creature benefits from the daily
performance between saving throws against a [corruption](ref/rule/corruption) progressing, it gains
a +3 bonus on the next saving throw against that corruption.

The amount of this bonus increases by 1 at 16th and 19th levels (maximum +5 at 19th level).

This ability replaces jack-of-all-trades.
