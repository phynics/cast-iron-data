+++
id = "ref/arc-vigilante/darklantern"
kind = "archetype"
title = "Darklantern"
aon = "ArchetypeDisplay.aspx?FixedName=Vigilante%20Darklantern"
source_ids = ["heroes-of-the-darklands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "darklantern", path = "json/archetypes_vigilante.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/vigilante" },
]
[[sources]]
publication = "heroes-of-the-darklands"
page = "11"

[fields]
kind = "archetype"
features = [
  { anchor = "dark-identity", level = 1 },
  { anchor = "drow-magic", level = 1 },
  { anchor = "drow-paragon", level = 4 },
]
trades = [
  { replaces = "Social talent that the darklantern gains at 1st level", feature = "social-talent", levels = [1], by = ["drow-magic"] },
  { replaces = "Vigilante talent gained at 4th level", feature = "vigilante-talent", levels = [4], by = ["drow-paragon"] },
  { alters = "Dual identity", feature = "dual-identity", by = ["dark-identity"] },
]
+++

The [Lantern Bearers](ref/rule/aff-lights) are an elite group of elves dedicated to the containment
and eradication of the drow. However, some Lantern Bearers are tasked with the unthinkable
assignment of infiltrating drow society so as to relay information to the Winter Council—a secret
cabal tasked with keeping the existence of drow a secret—about activities in the Darklands and drow
cities. In order to accomplish this task, select members of the Lantern Bearers undergo a horrific
ritual allowing them to temporarily experience the dark transformation into a drow, but at the cost
of their sanity.

## Elven Ancestry {#elven-ancestry}

A darklantern must be a creature with the elf subtype.

## Dark Identity (Su) {#dark-identity}

At 1st level, a darklantern can transform into her vigilante identity as a full-round action. When a
darklantern switches to her vigilante identity, she undergoes a horrifying transformation from an
elf into a [drow](ref/race/drow). After the transformation is complete, the darklantern takes on the
appearance of a drow (but otherwise retains her normal facial features and voice) and gains a +2
bonus to Dexterity and Charisma, [darkvision](ref/rule/darkvision) with a range of up to 60 feet,
and the [light blindness](ref/umr/light-blindness) universal monster ability. While in her vigilante
identity, the darklantern counts as a drow for the purpose of any ability, spell, or magic item
targeting drow. A darklantern's vigilante identity must be chaotic evil, but her social identity can
be more than one step removed from this alignment.

Transforming back into the darklantern's social identity requires a move action. However, a
darklantern must succeed at a Will save (DC = 10 + the number of hours she has been in her vigilante
identity) in order to successfully transform back into her social identity; otherwise, the move
action is wasted and the action cannot be attempted for 1 minute. Each time a darklantern fails this
check, she takes 1 point of [Wisdom damage](ref/rule/ability-damage-drain) and the DC for the save
decreases by 2.

This ability alters dual identity.

## Drow Magic (Sp) {#drow-magic}

At 1st level, when in her vigilante identity, a darklantern can cast
_[dancing lights](ref/spell/dancing-lights)_, _[darkness](ref/spell/darkness)_, and
_[faerie fire](ref/spell/faerie-fire)_, once each per day, using her vigilante level as her caster
level.

This replaces the social talent that the darklantern gains at 1st level.

## Drow Paragon (Su) {#drow-paragon}

At 4th level, the darklantern gains [Spell Resistance](ref/rule/spell-resistance) equal to 6 + her
vigilante level, and the range of her [darkvision](ref/rule/darkvision) increases to 120 feet while
in her vigilante identity.

This replaces the vigilante talent gained at 4th level.
