+++
id = "ref/arc-paladin/divine-guardian"
kind = "archetype"
title = "Divine Guardian"
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
replaces = ["Detect evil"]
alters = ["Lay on hands", "Aura of courage"]
replaces_features = ["detect-evil"]
alters_features = ["lay-on-hands", "aura-of-courage"]
+++

The divine guardian devotes herself to the protection and guardianship of one creature at a time, be
that her liege lord, an allied cleric, or an innocent facing overwhelming danger at the hands of
evil.

**Martial Focus**

**Info:** The divine guardian devotes herself to the concerns of the material world, eschewing some
divine studies. She does not gain access to divine spellcasting and cannot use
[spell-completion](ref/misc/spell-completion) magic items.

**Divine Troth (Sp)**

**Ability:** Once per day the divine guardian pledges her protection to a willing creature for the
day. This is done at the same time she prepares her spells. When the paladin first selects a
creature for _divine troth,_ that creature must be present and agree to receive the paladin's
protection, but if the paladin already has a creature selected for _divine troth,_ she can maintain
that selection each day without her charge being present.

**Ability2:** Once per day, the divine guardian can cast
[locate creature](ref/spell/locate-creature) to find the current target of her _divine troth._

**Replaces:** Detect evil

**Guarding Hands (Su)**

**Alters:** Lay on hands

**Info:** The paladin can use _lay on hands_ to heal herself or her _divine troth_ as a **move
action**, but cannot use _lay on hands_ to heal herself as a swift action. The divine guardian
cannot use _lay on hands_ more than once per round.

**Courageous Defense (Ex)**

**Ability:** A divine guardian can intercept attacks directed at the target of her _divine troth_ as
if she had the [Bodyguard](ref/feat/bodyguard) and [In Harm's Way](ref/feat/in-harms-way) feats.

**Alters:** Aura of courage

**Info:** The divine guardian's _aura of courage_ does not grant a bonus to allies within 10 feet,
but still grants her immunity to fear effects.

**Gained:** At 3rd Level

**Bonus Feat**

**At 10th Level:** She gains a second bonus feat from the list above.

**At 13th Level:** She gains a third feat from the list above.

**At 7th Level:** A divine guardian gains a bonus feat, chosen from the following list:
[Diehard](ref/feat/diehard), [Endurance](ref/feat/endurance),
[Greater Shield Focus](ref/feat/greater-shield-focus),
[Greater Shield Specialization](ref/feat/greater-shield-specialization),
[Heroic Defiance](ref/feat/heroic-defiance), [Heroic Recovery](ref/feat/heroic-recovery),
[Missile Shield](ref/feat/missile-shield), [Ray Shield](ref/feat/ray-shield),
[Saving Shield](ref/feat/saving-shield), [Shield Focus](ref/feat/shield-focus),
[Shield Specialization](ref/feat/shield-specialization), or
[Tower Shield Proficiency](ref/feat/tower-shield-proficiency).

**Special:** She must meet these feats' prerequisites, but for purposes of meeting the prerequisites
of these bonus feats, she treats her paladin level as her fighter level, may use her Charisma score
as her Dexterity score, and is considered to have the [Spellbreaker](ref/feat/spellbreaker) feat.
