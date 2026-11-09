+++
id = "ref/arc-antipaladin/blighted-myrmidon"
kind = "archetype"
title = "Blighted Myrmidon"
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
replaces = ["10th-level use of smite good", "Aura of vengeance", "The cruelty gained at 15th level"]
alters = ["Smite good", "Fiendish boon", "Unholy champion"]
+++

Blighted myrmidons carry the seed of rot in their black hearts and sap life from the natural world.

**Smite Nature (Su)**

**Alters:** Smite good

**Flavor:** A blighted myrmidon can drain the life from a creature tied to nature.

**Gained:** At 1st Level

**Swift:** The blighted myrmidon chooses one target within sight to smite. Regardless of its
alignment, if the target is an animal, plant, or vermin, the blighted myrmidon adds her Charisma
bonus (if any) on her attack rolls and adds her blighted myrmidon level on damage rolls against the
target of her _smite._ If the target of _smite nature_ is an elemental, a fey, or a creature with
levels of druid, hunter, ranger, or shifter, the bonus on damage on the first successful attack
increases to 2 points of damage per class level the blighted myrmidon has. This ability otherwise
functions as smite good.

**Corrupted Companion (Sp)**

**Ability:** When the blighted myrmidon chooses the second _fiendish boon_ option, it functions as a
[summon nature's ally](ref/spell/summon-natures-ally) spell of the appropriate level. This ability
otherwise functions as the standard fiendish boon antipaladin class feature.

**Alters:** Fiendish boon

**Flavor:** A blighted myrmidon can call upon a corrupted servant of nature.

**Gained:** At 5th Level

**Feed on Decay (Ex)**

**Flavor:** A blighted myrmidon draws strength from corrupting the natural world.

**Gained:** At 10th Level

**Passive:** When the blighted myrmidon damages a creature with her _smite nature_ ability, she
gains a +1 morale bonus on attack rolls, damage rolls, and saving throws for 1 round.

**Replaces:** 10th-level use of smite good

**Aura of Decay (Su)**

**Free:** A blighted myrmidon can expend two uses of her _smite nature_ ability to generate an aura
of decay with a range of 10 feet for 1 minute. Living foes of the blighted myrmidon within the aura
take 3d6 points of damage unless they succeed at a Fortitude save (DC =
[half](ref/misc/fractions-and-rounding) the blighted myrmidon's level + her Charisma modifier) for
half damage. If an elemental, a fey, or a creature with levels in druid, hunter, ranger, or shifter
takes damage from aura of decay, the blighted myrmidon regains a number of hit points equal to half
the amount of damage the creature takes; this doesn't stack if multiple such creatures are in the
aura.

**Gained:** At 11th Level

**Replaces:** Aura of vengeance

**Enervating Touch (Su)**

**Gained:** At 15th Level

**Passive:** When she damages a creature with her _touch of corruption,_ a blighted myrmidon can
suppress the vital force of her target for 1 round per level. While affected, when the target
regains hit points, it regains only half the number of hit points it would otherwise receive, and it
can't gain [temporary hit points](ref/rule/temporary-hit-points). The target can attempt a Fortitude
save (DC = half the blighted myrmidon's level + her Charisma modifier) to negate this effect.

**Replaces:** The cruelty gained at 15th level

**Unnatural Champion (Ex)**

**Alters:** Unholy champion

**Gained:** At 20th Level

**Passive:** When a blighted myrmidon uses _smite nature_ and strikes an elemental or fey creature
with the [extraplanar](ref/subtype/extraplanar) subtype, the target is also subject to the effects
of a [banishment](ref/spell/banishment) spell, using her blighted myrmidon level as her caster
level, and her weapon and unholy symbol automatically count as objects that the subject hates. This
ability otherwise functions as _unholy champion._
