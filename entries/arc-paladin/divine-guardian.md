+++
id = "ref/arc-paladin/divine-guardian"
kind = "archetype"
title = "Divine Guardian"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Divine%20Guardian"
source_ids = ["cohorts-and-companions"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "divine_guardian", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "cohorts-and-companions"
page = "23"

[fields]
kind = "archetype"
features = [
  { anchor = "martial-focus" },
  { anchor = "divine-troth", level = 1 },
  { anchor = "guarding-hands" },
  { anchor = "courageous-defense", level = 3 },
  { anchor = "bonus-feat" },
]
trades = [
  { replaces = "Detect evil", feature = "detect-evil", by = ["divine-troth"] },
  { alters = "Lay on hands", feature = "lay-on-hands", by = ["guarding-hands"] },
  { alters = "Aura of courage", feature = "aura-of-courage", by = ["courageous-defense"] },
]
+++

The divine guardian devotes herself to the protection and guardianship of one creature at a time, be
that her liege lord, an allied cleric, or an innocent facing overwhelming danger at the hands of
evil.

## Martial Focus {#martial-focus}

The divine guardian devotes herself to the concerns of the material world, eschewing some divine
studies. She does not gain access to divine spellcasting and cannot use
[spell-completion](ref/misc/spell-completion) magic items.

## Divine Troth (Sp) {#divine-troth}

Once per day the divine guardian pledges her protection to a willing creature for the day. This is
done at the same time she prepares her spells. When the paladin first selects a creature for divine
troth, that creature must be present and agree to receive the paladin's protection, but if the
paladin already has a creature selected for divine troth, she can maintain that selection each day
without her charge being present. Once per day, the divine guardian can cast
_[locate creature](ref/spell/locate-creature)_ to find the current target of her divine troth. This
ability replaces _detect evil_.

## Guarding Hands (Su) {#guarding-hands}

The paladin can use lay on hands to heal herself or her divine troth as a move action, but cannot
use lay on hands to heal herself as a swift action. The divine guardian cannot use lay on hands more
than once per round. This modifies lay on hands.

## Courageous Defense (Ex) {#courageous-defense}

At 3rd level a divine guardian can intercept attacks directed at the target of her divine troth as
if she had the [Bodyguard](ref/feat/bodyguard) and [In Harm's Way](ref/feat/in-harms-way) feats. The
divine guardian's aura of courage does not grant a bonus to allies within 10 feet, but still grants
her immunity to fear effects. This ability modifies aura of courage.

## Bonus Feat {#bonus-feat}

A divine guardian gains a bonus feat at 7th level, and additional bonus feats at 10th and 13th
level. These bonus feats must be chosen from the following list: [Diehard](ref/feat/diehard),
[Endurance](ref/feat/endurance), [Greater Shield Focus](ref/feat/greater-shield-focus),
[Greater Shield Specialization](ref/feat/greater-shield-specialization),
[Heroic Defiance](ref/feat/heroic-defiance), [Heroic Recovery](ref/feat/heroic-recovery),
[Missile Shield](ref/feat/missile-shield), [Ray Shield](ref/feat/ray-shield),
[Saving Shield](ref/feat/saving-shield), [Shield Focus](ref/feat/shield-focus),
[Shield Specialization](ref/feat/shield-specialization), or
[Tower Shield Proficiency](ref/feat/tower-shield-proficiency). She must meet these feats'
prerequisites, but for purposes of meeting the prerequisites of these bonus feats, she treats her
paladin level as her fighter level, may use her Charisma score as her Dexterity score, and is
considered to have the [Spellbreaker](ref/feat/spellbreaker) feat.
