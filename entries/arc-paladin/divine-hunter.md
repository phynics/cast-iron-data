+++
id = "ref/arc-paladin/divine-hunter"
kind = "archetype"
title = "Divine Hunter"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Divine%20Hunter"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "divine_hunter", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "ultimate-combat"
page = "62"

[fields]
kind = "archetype"
features = [
  { anchor = "precise-shot", level = 1 },
  { anchor = "shared-precision", level = 3 },
  { anchor = "divine-bond", level = 5 },
  { anchor = "distant-mercy", level = 6 },
  { anchor = "aura-of-care", level = 8 },
  { anchor = "hunter-s-blessing", level = 11 },
  { anchor = "righteous-hunter", level = 14 },
]
trades = [
  { replaces = "Heavy Armor Proficiency", feature = "weapon-and-armor-proficiencies", power = "heavy armor", by = ["precise-shot"] },
  { replaces = "Aura of courage", feature = "aura-of-courage", by = ["shared-precision"] },
  { replaces = "Divine bond", feature = "divine-bond", by = ["divine-bond"] },
  { replaces = "6th-level mercy", feature = "mercy", levels = [6], by = ["distant-mercy"] },
  { replaces = "Aura of resolve", feature = "aura-of-resolve", by = ["aura-of-care"] },
  { replaces = "Aura of justice", feature = "aura-of-justice", by = ["hunter-s-blessing"] },
  { replaces = "Aura of faith", feature = "aura-of-faith", by = ["righteous-hunter"] },
]
+++

Most paladins rush into battle, meeting evil toe-to-toe. The divine hunter prefers to engage evil
from afar, striking down her foes before they can threaten her allies.

## Precise Shot {#precise-shot}

A divine hunter gains [Precise Shot](ref/feat/precise-shot) as a bonus feat at 1st level, even if
she doesn't meet the prerequisites. This ability replaces her Heavy Armor Proficiency.

## Shared Precision (Su) {#shared-precision}

At 3rd level, when a divine hunter hits a creature with a ranged attack, she grants her allies
within 10 feet of her the benefit of the Precise Shot feat against that target until the start of
her next turn. Her allies must remain within 10 feet of her, and must be able both to see and hear
the divine hunter to gain this benefit. This ability replaces aura of courage.

## Divine Bond (Su) {#divine-bond}

At 5th level, a divine hunter forms a bond with her deity. This functions as the paladin's divine
bond ability, except the bond must always take the form of a ranged or throwing weapon (excluding
ammunition). In addition to the listed abilities, a divine hunter can add the
_[distance](ref/magic-enh/distance)_, _[returning](ref/magic-enh/returning)_, or
_[seeking](ref/magic-enh/seeking)_ special abilities to her weapon, but she cannot add the
_defending_ or _disruption_ special abilities. Special abilities added to throwing weapons function
normally when the weapon is used in melee. This ability replaces the standard paladin's divine bond.

## Distant Mercy (Sp) {#distant-mercy}

At 6th level, a divine hunter can expend two uses of her lay on hand abilities to use her lay on
hands ability on a target within 5 feet per paladin level. Distant mercy has no effect on creatures
harmed by positive energy, such as undead. This ability replaces the paladin's 6th-level mercy.

## Aura of Care (Su) {#aura-of-care}

At 8th level, a divine hunter and her allies gain a preternatural awareness of each other's position
in battle. She and any allies within 10 feet of her no longer provide [cover](ref/rule/cover)
against each other's ranged attacks unless they wish to. Allies who cannot move or otherwise take
actions still provide cover, as do [flat-footed](ref/rule/flat-footed) allies. The divine hunter and
her allies must be able to see or hear each other to use this ability. This ability replaces aura of
resolve.

## Hunter's Blessing (Su) {#hunter-s-blessing}

At 11th level, a divine hunter can expend a use of her smite evil ability as a swift action to grant
herself and all allies within 10 feet the [Deadly Aim](ref/feat/deadly-aim), Precise Shot, and
[Improved Precise Shot](ref/feat/improved-precise-shot) feats, even if they lack the prerequisites.
The effects last for 1 minute. Evil creatures gain no benefit from this ability. This ability
replaces aura of justice.

## Righteous Hunter (Su) {#righteous-hunter}

At 14th level, a divine hunter's ranged weapons are treated as good-aligned for the purposes of
overcoming [damage reduction](ref/rule/damage-reduction). Any ranged attacks made by an ally within
10 feet of her are likewise treated as good-aligned for the purposes of overcoming damage reduction.

This ability functions only while the divine hunter is conscious. This ability replaces aura of
faith.
