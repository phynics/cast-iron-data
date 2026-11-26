+++
id = "ref/arc-antipaladin/blighted-myrmidon"
kind = "archetype"
title = "Blighted Myrmidon"
aon = "ArchetypeDisplay.aspx?FixedName=Antipaladin%20Blighted%20Myrmidon"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blighted_myrmidon", path = "json/archetypes_antipaladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/antipaladin" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "91"

[fields]
kind = "archetype"
features = [
  { anchor = "smite-nature" },
  { anchor = "corrupted-companion", level = 5 },
  { anchor = "feed-on-decay", level = 10 },
  { anchor = "aura-of-decay", level = 11 },
  { anchor = "enervating-touch", level = 15 },
  { anchor = "unnatural-champion", level = 20 },
]
trades = [
  { replaces = "Use of smite good gained at 10th level", feature = "smite-good", levels = [10], by = ["feed-on-decay"] },
  { replaces = "Aura of vengeance", feature = "aura-of-vengeance", by = ["aura-of-decay"] },
  { replaces = "The cruelty gained at 15th level", feature = "cruelty", levels = [15], by = ["enervating-touch"] },
  { alters = "Smite good", feature = "smite-good", by = ["smite-nature"] },
  { alters = "Fiendish boon", feature = "fiendish-boon", by = ["corrupted-companion"] },
  { alters = "Unholy champion", feature = "unholy-champion", by = ["unnatural-champion"] },
]
+++

Blighted myrmidons carry the seed of rot in their black hearts and sap life from the natural world.

## Smite Nature (Su) {#smite-nature}

A blighted myrmidon can drain the life from a creature tied to nature. As a swift action, the
blighted myrmidon chooses one target within sight to smite. Regardless of its alignment, if the
target is an animal, plant, or vermin, the blighted myrmidon adds her Charisma bonus (if any) on her
attack rolls and adds her blighted myrmidon level on damage rolls against the target of her smite.
If the target of smite nature is an elemental, a fey, or a creature with levels of druid, hunter,
ranger, or shifter, the bonus on damage on the first successful attack increases to 2 points of
damage per class level the blighted myrmidon has. This ability otherwise functions as smite good.

This alters smite good.

## Corrupted Companion (Sp) {#corrupted-companion}

At 5th level, a blighted myrmidon can call upon a corrupted servant of nature. When the blighted
myrmidon chooses the second fiendish boon option, it functions as a
_[summon nature's ally](ref/spell/summon-natures-ally)_ spell of the appropriate level. This ability
otherwise functions as the standard fiendish boon antipaladin class feature.

This alters fiendish boon.

## Feed on Decay (Ex) {#feed-on-decay}

At 10th level, a blighted myrmidon draws strength from corrupting the natural world. When the
blighted myrmidon damages a creature with her smite nature ability, she gains a +1 morale bonus on
attack rolls, damage rolls, and saving throws for 1 round.

This replaces the use of smite good gained at 10th level.

## Aura of Decay (Su) {#aura-of-decay}

At 11th level, as a free action, a blighted myrmidon can expend two uses of her smite nature ability
to generate an aura of decay with a range of 10 feet for 1 minute. Living foes of the blighted
myrmidon within the aura take 3d6 points of damage unless they succeed at a Fortitude save (DC =
[half](ref/misc/fractions-and-rounding) the blighted myrmidon's level + her Charisma modifier) for
half damage. If an elemental, a fey, or a creature with levels in druid, hunter, ranger, or shifter
takes damage from aura of decay, the blighted myrmidon regains a number of hit points equal to half
the amount of damage the creature takes; this doesn't stack if multiple such creatures are in the
aura.

This replaces aura of vengeance.

## Enervating Touch (Su) {#enervating-touch}

At 15th level, when she damages a creature with her touch of corruption, a blighted myrmidon can
suppress the vital force of her target for 1 round per level. While affected, when the target
regains hit points, it regains only half the number of hit points it would otherwise receive, and it
can't gain [temporary hit points](ref/rule/temporary-hit-points). The target can attempt a Fortitude
save (DC = half the blighted myrmidon's level + her Charisma modifier) to negate this effect.

This replaces the cruelty gained at 15th level.

## Unnatural Champion (Ex) {#unnatural-champion}

At 20th level, when a blighted myrmidon uses smite nature and strikes an elemental or fey creature
with the [extraplanar](ref/subtype/extraplanar) subtype, the target is also subject to the effects
of a _[banishment](ref/spell/banishment)_ spell, using her blighted myrmidon level as her caster
level, and her weapon and unholy symbol automatically count as objects that the subject hates. This
ability otherwise functions as unholy champion.

This alters unholy champion.
