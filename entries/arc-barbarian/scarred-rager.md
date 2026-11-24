+++
id = "ref/arc-barbarian/scarred-rager"
kind = "archetype"
title = "Scarred Rager"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Scarred%20Rager"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "scarred_rager", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "ultimate-combat"
page = "29"

[fields]
kind = "archetype"
features = [
  { anchor = "terrifying-visage", level = 1 },
  { anchor = "tolerance", level = 2 },
  { anchor = "scarification", level = 3 },
  { anchor = "improved-tolerance", level = 5 },
]
trades = [
  { replaces = "Fast movement", feature = "fast-movement", by = ["terrifying-visage"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["tolerance"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["scarification"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["improved-tolerance"] },
]
+++

Some barbarians wear marks of prowess and savagery upon their bodies. The scarred rager believes
each wound tells the tales of her prowess and bravery. She augments these ragged trophies with
brands and tattoos in order to win the notice and favor of her gods, ancestors, or totem spirits.
The scarred rager's gnarled and exotic appearance terrifies civilized onlookers, but is
awe-inspiring to her savage kin.

## Terrifying Visage (Ex) {#terrifying-visage}

A scarred rager adds 1/2 her barbarian level on Intimidate checks against humanoids who are not
members of barbarian tribes. When dealing with barbarians, the scarred rager may choose to add this
bonus on Diplomacy checks instead. The DC of any fear effect created by the scarred rager also
increases by 1. This ability replaces fast movement.

## Tolerance (Ex) {#tolerance}

At 2nd level, a scarred rager who fails a save against an effect that causes her to become
nauseated, sickened, fatigued, or exhausted can make a second save to negate the effect on the start
of her next turn. Only one additional save is allowed. If the effect does not allow a saving throw,
its duration is halved instead (minimum of 1 round). This ability replaces uncanny dodge.

## Scarification (Ex) {#scarification}

At 3rd level, a scarred rager can ignore 1 point of bleed damage per round. This amount increases by
1 every three levels beyond 3rd. At 15th level, a scarred rager can ignore 1 bleed effect each
round. This ability replaces trap sense.

## Improved Tolerance (Ex) {#improved-tolerance}

At 5th level, a scarred rager's tolerance ability also applies to effects that would cause her to
become dazed, frightened, shaken, or stunned. This replaces improved uncanny dodge.

## Rage Powers {#rage-powers}

The following rage powers complement the scarred rager archetype:
[auspicious mark](ref/ragepower/auspicious-mark), [body bludgeon](ref/ragepower/body-bludgeon),
[come and get me](ref/ragepower/come-and-get-me),
[increased damage reduction](ref/ragepower/increased-damage-reduction),
[inspire ferocity](ref/ragepower/inspire-ferocity),
[internal fortitude](ref/ragepower/internal-fortitude),
[intimidating glare](ref/ragepower/intimidating-glare),
[reckless abandon](ref/ragepower/reckless-abandon),
[regenerative vigor](ref/ragepower/regenerative-vigor), [renewed life](ref/ragepower/renewed-life),
[renewed vigor](ref/ragepower/renewed-vigor), [renewed vitality](ref/ragepower/renewed-vitality),
[roused anger](ref/ragepower/roused-anger), and [terrifying howl](ref/ragepower/terrifying-howl).
