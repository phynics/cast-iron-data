+++
id = "ref/arc-cleric/stoic-caregiver"
kind = "archetype"
title = "Stoic Caregiver"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Stoic%20Caregiver"
source_ids = ["healers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "stoic_caregiver", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "healers-handbook"
page = "6"

[fields]
kind = "archetype"
features = [
  { anchor = "positive-channeler", level = 1 },
  { anchor = "domains", level = 1 },
  { anchor = "midwife-training" },
  { anchor = "fated-cures" },
  { anchor = "three-aspect-channel", level = 6 },
]
trades = [
  { alters = "Channel energy", feature = "channel-energy", by = ["positive-channeler"] },
  { alters = "Domains", feature = "domains", by = ["domains"] },
]
+++

Stoic caregivers are champions of life in defiance of untimely death as well as undeath. Stoic
caregivers are sent to protect and help those who find themselves in dangerous situations,
especially children and expectant mothers, and they provide aid and comfort to individuals acting to
fulfill prophecy.

## Positive Channeler (Su) {#positive-channeler}

A stoic caregiver must choose to channel positive energy, even if she worships a deity who is
neutral or if she is not devoted to a particular deity. A stoic caregiver cannot worship a deity who
is evil.

This ability alters channel energy.

## Domains {#domains}

A stoic caregiver chooses only one domain.

This ability alters domains.

## Midwife Training (Su) {#midwife-training}

A stoic caregiver is an expert at caring for lives that are in the process of being formed as well
as the bodies of those who expect to usher new life into the world. The stoic caregiver gains a +2
bonus on Heal checks to treat expectant mothers and children. Any Heal check by the stoic caregiver
that deals damage to the patient always deals the minimum amount of damage.

Whenever a stoic caregiver stops bleeding with the Heal skill or magical healing, or restores hit
points with a healing spell or channeled positive energy, the healed creature gains partial
resistance to bleed damage and negative energy for a number of minutes equal to 1/2 the stoic
caregiver's cleric level. Any bleed damage a target takes during that time is halved. Additionally,
when protected creatures take negative energy damage (such as from an evil cleric's or an
antipaladin's negative channeled energy, or spells such as
_[inflict light wounds](ref/spell/inflict-light-wounds)_), the amount of that damage is reduced
by 5.

## Fated Cures (Su) {#fated-cures}

Creatures must roll twice and take the lower result when they make any saving throws against a stoic
caregiver's spells of the healing subschool.

## Three-Aspect Channel (Su) {#three-aspect-channel}

At 6th level, a stoic caregiver can channel positive energy to heal and harm simultaneously. When
she does so, she restores only 1/2 the usual amount of hit points and deals only 1/2 the usual
number of points of damage (or 1/4 on a successful saving throw).
