+++
id = "ref/arc-ninja/mask-of-the-living-god"
kind = "archetype"
title = "Mask of the Living God"
aon = "ArchetypeDisplay.aspx?FixedName=Ninja%20Mask%20of%20the%20Living%20God"
source_ids = ["disciples-doctrine"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mask_of_the_living_god", path = "json/archetypes_ninja.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ninja" },
]
[[sources]]
publication = "disciples-doctrine"
page = "20"

[fields]
kind = "archetype"
features = [
  { anchor = "mask" },
  { anchor = "undercover-faith", level = 1 },
  { anchor = "expurgate", level = 2 },
  { anchor = "stern-gaze", level = 3 },
]
trades = [
  { replaces = "Poison use", feature = "poison-use", by = ["undercover-faith"] },
  { replaces = "Spend ki to make an additional attack", by = ["expurgate"] },
  { replaces = "No trace", feature = "no-trace", by = ["stern-gaze"] },
  { alters = "The mask of the Living God's weapon and armor proficiency", feature = "weapon-and-armor-proficiencies" },
  { alters = "Ki pool", feature = "ki-pool", by = ["expurgate"] },
]
+++

When the Living God needs to silence the voices of those heretics who question too loudly, these
enforcers are the tools he employs.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

In addition to having the ninja's normal weapon and armor proficiencies, the mask of the Living God
is proficient with [bolas](ref/eq-weapon/bolas), [saps](ref/eq-weapon/sap), and
[whips](ref/eq-weapon/whip).

This alters the mask of the Living God's weapon and armor proficiency.

## Mask (Ex) {#mask}

A mask of the Living God has a mask that is a symbol of his faith and the myriad powers invested in
him. Abilities granted by this class other than undercover faith function only while the mask of the
Living God is wearing his mask. Putting on or removing this mask is a move action.

## Undercover Faith (Ex) {#undercover-faith}

At 1st level, when not wearing his mask, a mask of the Living God can take on an utterly mundane
identity as if he were a [vigilante](ref/class/vigilante) with the
[many guises](ref/soctalent/many-guises) social talent. While in a mundane identity, the mask of the
Living God cannot wear his mask; putting it on while in a mundane identity immediately ends the
mundane identity and its effects. Changing into this mundane identity takes 1 minute and must be
done out of sight to preserve the mask of the Living God's secret. The time it takes the mask of the
Living God to change into a mundane identity cannot be decreased.

This replaces poison use.

## Expurgate (Sp) {#expurgate}

The role of a mask of the Living God is to silence heretics and blasphemers, and he is an expert at
rendering even the most glib of his foes into babbling fools. At 2nd level, when he deals damage to
a target, he can expend 1 point from his ki pool to affect that target as if he had cast
_[fumbletongue](ref/spell/fumbletongue)_, using his ninja level as his caster level. The target can
attempt a Will saving throw (DC = 10 + half the ninja's level + his Charisma modifier) to negate
this effect. At 6th level, the target of this ability is instead struck entirely mute for 1d4 rounds
unless it succeeds at a Will saving throw. The mask of the Living God cannot spend a point from his
ki pool to make an additional attack.

This alters ki pool.

## Stern Gaze (Ex) {#stern-gaze}

A mask of the Living God is trained to sense deception and strike fear into the hearts of his foes.
At 3rd level, he gains a morale bonus equal to [half](ref/misc/fractions-and-rounding) his ninja
level on Intimidate and Sense Motive checks.

This replaces no trace.

## Ninja Tricks {#ninja-tricks}

The following ninja tricks complement the mask of the Living God archetype:
[forgotten trick](ref/ninjatrick/forgotten-trick), [kamikaze](ref/ninjatrick/kamikaze),
[unarmed combat training](ref/ninjatrick/unarmed-combat-training),
[vanishing trick](ref/ninjatrick/vanishing-trick),
[weapon training](ref/ninjatrick/weapon-training).

## Master Tricks {#master-tricks}

The following master tricks complement the mask of the Living God:
[ghost step](ref/ninjatrick/ghost-step), [see the unseen](ref/ninjatrick/see-the-unseen), and
[shadow split](ref/ninjatrick/shadow-split).
