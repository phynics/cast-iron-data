+++
id = "ref/arc-cavalier/daring-champion"
kind = "archetype"
title = "Daring Champion"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Daring%20Champion"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "daring_champion", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "advanced-class-guide"
page = "90"

[fields]
kind = "archetype"
features = [
  { anchor = "champion-s-finesse", level = 1 },
  { anchor = "nimble", level = 3 },
  { anchor = "panache-and-deeds", level = 4 },
  { anchor = "advanced-deeds", level = 11 },
  { anchor = "champion-s-weapon-mastery", level = 20 },
]
trades = [
  { replaces = "Weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies" },
  { replaces = "Mount", feature = "mount", by = ["champion-s-finesse"] },
  { replaces = "Cavalier's charge", feature = "cavalier-s-charge", by = ["nimble"] },
  { replaces = "Expert trainer", feature = "expert-trainer", by = ["panache-and-deeds"] },
  { replaces = "Mighty charge", feature = "mighty-charge", by = ["advanced-deeds"] },
  { replaces = "Supreme charge", feature = "supreme-charge", by = ["champion-s-weapon-mastery"] },
]
+++

While many cavaliers are the champions of old fighting forms, some younger, more daring cavaliers
mix a martial style influenced by the lighter armored and more flamboyant swashbuckler forms with
the dedication of cavalier orders.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

Daring champions are proficient with all simple and martial weapons, light and medium armor, and
bucklers. This replaces the cavalier's weapon and armor proficiencies.

## Champion's Finesse (Ex) {#champion-s-finesse}

At 1st level, a daring champion gains the benefits of the [Weapon Finesse](ref/feat/weapon-finesse)
feat with light or one-handed piercing melee weapons, and he can use Charisma in place of
Intelligence for the purpose of combat feats prerequisites. A daring champion also counts as having
the Weapon Finesse feat for the purpose of meeting feat requirements. This ability replaces mount.

## Nimble (Ex) {#nimble}

At 3rd level, a daring champion gains a +1 dodge bonus to AC when wearing light or no armor and
carrying no more than a light load. Anything that causes the daring champion to lose his Dexterity
bonus to AC also causes him to lose this dodge bonus. This bonus increases by 1 for every 4 levels
beyond 3rd (to a maximum of +5 at 19th level). This ability replaces cavalier's charge.

## Panache and Deeds (Ex) {#panache-and-deeds}

At 4th level, a daring champion gains the [swashbuckler's](ref/class/swashbuckler) panache class
feature, along with the following swashbuckler deeds:
[dodging panache](ref/swashdeed/dodging-panache), [precise strike](ref/swashdeed/precise-strike),
and [swashbuckler initiative](ref/swashdeed/swashbuckler-initiative). This ability replaces expert
trainer.

## Advanced Deeds (Ex) {#advanced-deeds}

At 11th level, a daring champion gains the following swashbuckler deeds:
[superior feint](ref/swashdeed/superior-feint), targeted strike,
[subtle blade](ref/swashdeed/subtle-blade), and [dizzying defense](ref/swashdeed/dizzying-defense).
This ability replaces mighty charge.

## Champion's Weapon Mastery (Ex) {#champion-s-weapon-mastery}

At 20th level, when a daring champion threatens a critical hit with a light or one-handed piercing
melee weapon, that critical is automatically confirmed. Furthermore, the critical modifier of those
weapons increases by 1 (×2 becomes ×3, for example). This ability replaces supreme charge.
