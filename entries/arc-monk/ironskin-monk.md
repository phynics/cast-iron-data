+++
id = "ref/arc-monk/ironskin-monk"
kind = "archetype"
title = "Ironskin Monk"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Ironskin%20Monk"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ironskin_monk", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "advanced-race-guide"
page = "122"

[fields]
kind = "archetype"
features = [
  { anchor = "iron-skin", level = 1 },
  { anchor = "bonus-feat", level = 1 },
  { anchor = "resilience", level = 2 },
  { anchor = "ki-pool", level = 4 },
  { anchor = "staggering-blow", level = 5 },
  { anchor = "tough-as-nails", level = 6 },
  { anchor = "evasion", level = 9 },
  { anchor = "surefooted", level = 17 },
  { anchor = "unbreakable", level = 20 },
]
trades = [
  { replaces = "AC bonus", feature = "ac-bonus", by = ["iron-skin"] },
  { replaces = "the ability to add his Wisdom bonus to his AC", by = ["iron-skin"] },
  { replaces = "Dodge", by = ["bonus-feat"] },
  { replaces = "Mobility", by = ["bonus-feat"] },
  { replaces = "Spring Attack on his bonus feat list", by = ["bonus-feat"] },
  { replaces = "Evasion", feature = "evasion", by = ["resilience"] },
  { replaces = "The ability to increase speed with ki", by = ["ki-pool"] },
  { replaces = "High jump", feature = "high-jump", by = ["staggering-blow"] },
  { replaces = "Fast movement", feature = "fast-movement", by = ["tough-as-nails"] },
  { replaces = "slow fall", feature = "slow-fall", by = ["tough-as-nails"] },
  { replaces = "Improved evasion", feature = "improved-evasion", by = ["evasion"] },
  { replaces = "Tongue of the sun and moon", feature = "tongue-of-the-sun-and-moon", by = ["surefooted"] },
  { replaces = "Perfect self", feature = "perfect-self", by = ["unbreakable"] },
]
+++

Through discipline and training, an ironskin monk hardens his body to withstand punishing blows.

Though slow on his feet, his calloused hands and feet can shatter stone and stagger foes.

## Iron Skin (Ex) {#iron-skin}

At 1st level, an ironskin monk gains a +1 bonus to his natural armor. This bonus stacks with any
existing natural armor the ironskin monk already has. At 4th level, and every 4 levels thereafter,
this bonus increases by +1. This ability replaces the monk's AC bonus ability and the ability to add
his Wisdom bonus to his AC.

## Bonus Feat {#bonus-feat}

At 1st level, an ironskin monk adds [Power Attack](ref/feat/power-attack) to his list of bonus
feats. At 6th level, he adds [Improved Sunder](ref/feat/improved-sunder) to the list. At 10th level,
he adds [Greater Sunder](ref/feat/greater-sunder) to the list. These bonus feat choices replace
Dodge, Mobility, and Spring Attack on his bonus feat list.

## Resilience (Ex) {#resilience}

At 2nd level, an ironskin monk can shake off the physical effects of certain attacks. If he makes a
Fortitude saving throw against an attack that has a reduced effect on a successful save, he instead
avoids the effect entirely. This ability can be used only if the monk is wearing light armor or no
armor. A helpless monk does not gain the benefits of resilience. This ability replaces evasion.

## Ki Pool (Su) {#ki-pool}

At 4th level, an ironskin monk can spend 1 point from his ki pool to gain a damage bonus equal to
1/2 his level against objects and constructs for 1 round. This replaces the ability to increase
speed with ki.

## Staggering Blow (Ex) {#staggering-blow}

At 5th level, an ironskin monk attacking with an unarmed strike can spend 1 point from his ki pool
as a free action after a successful critical hit to [stagger](ref/misc/staggered) the creature
struck for 1 round (Fort DC 10 + 1/2 the ironskin monk's level + the ironskin monk's Wisdom modifier
negates). This ability replaces high jump.

## Tough as Nails (Ex) {#tough-as-nails}

At 6th level, an ironskin monk gains [DR](ref/rule/damage-reduction) 1/—. Subtract 1 point from the
damage the ironskin monk takes each time he is dealt damage from a weapon or a natural attack. This
damage reduction increases by 1 point at 9th level and every 3 levels thereafter. Damage reduction
can reduce damage to 0 but not below 0. This ability replaces fast movement and slow fall.

## Evasion (Ex) {#evasion}

At 9th level, an ironskin monk gains [evasion](ref/ability/evasion). This ability replaces improved
evasion.

## Surefooted (Ex) {#surefooted}

At 17th level, an ironskin monk's speed is not reduced by
[difficult terrain](ref/rule/terrain-and-obstacles). This ability replaces tongue of the sun and
moon.

## Unbreakable (Ex) {#unbreakable}

At 20th level, an ironskin monk sets aside many of the frailties of mortal flesh. He becomes immune
to death effects and stunning. He is not subject to
[ability damage or ability drain](ref/rule/ability-damage-drain), and has a 75% chance of ignoring
the extra damage dealt by critical hits and sneak attacks. This ability replaces perfect self.
