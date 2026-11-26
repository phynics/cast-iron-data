+++
id = "ref/arc-paladin/virtuous-bravo"
kind = "archetype"
title = "Virtuous Bravo"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Virtuous%20Bravo"
source_ids = ["heroes-of-the-high-court"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "virtuous_bravo", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "heroes-of-the-high-court"
page = "12"

[fields]
kind = "archetype"
features = [
  { anchor = "bravo-s-finesse" },
  { anchor = "bravo-s-smite" },
  { anchor = "nimble", level = 3 },
  { anchor = "panache-and-deeds", level = 4 },
  { anchor = "advanced-deeds", level = 11 },
  { anchor = "bravo-s-holy-strike", level = 20 },
]
trades = [
  { replaces = "Mercy", feature = "mercy", by = ["nimble"] },
  { replaces = "Spellcasting", feature = "spells", by = ["panache-and-deeds"] },
  { replaces = "Aura of justice", feature = "aura-of-justice", by = ["advanced-deeds"] },
  { replaces = "Holy champion", feature = "holy-champion", by = ["bravo-s-holy-strike"] },
  { alters = "Armor proficiency", feature = "weapon-and-armor-proficiencies", power = "armor" },
  { alters = "Smite evil", feature = "smite-evil", by = ["bravo-s-smite"] },
]
+++

Although no less a beacon of hope and justice than other paladins, virtuous bravos rely on their wit
and grace rather than might and strong armor.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

Virtuous bravos aren't proficient with heavy armor or shields (except for
[bucklers](ref/eq-armor/buckler)).

This ability alters the paladin's armor proficiency.

## Bravo's Finesse (Ex) {#bravo-s-finesse}

A virtuous bravo can use her Dexterity modifier instead of her Strength modifier on attack rolls
with light or one-handed piercing melee weapons (though if she carries a shield, she applies its
armor check penalty to such attack rolls), and she can use her Charisma score in place of her
Intelligence score to meet prerequisites of combat feats. This ability counts as having the
[Weapon Finesse](ref/feat/weapon-finesse) feat for the purpose of meeting feat prerequisites.

## Bravo's Smite (Su) {#bravo-s-smite}

When using smite evil, a virtuous bravo doesn't gain a deflection bonus to AC.

This ability alters smite evil.

## Nimble (Ex) {#nimble}

At 3rd level, a virtuous bravo gains a +1 dodge bonus to AC while wearing light armor or no armor.

Anything that causes the virtuous bravo to lose her Dexterity bonus to AC also causes her to lose
this dodge bonus. This bonus increases by 1 for every 4 paladin levels beyond 3rd (to a maximum of
+5 at 19th level).

This ability replaces mercy.

## Panache and Deeds (Ex) {#panache-and-deeds}

At 4th level, a virtuous bravo gains the [swashbuckler's](ref/class/swashbuckler) panache class
feature along with the following swashbuckler deeds:
[dodging panache](ref/swashdeed/dodging-panache),
[menacing swordplay](ref/swashdeed/menacing-swordplay),
[opportune parry and riposte](ref/swashdeed/opportune-parry-and-riposte),
[precise strike](ref/swashdeed/precise-strike), and
[swashbuckler initiative](ref/swashdeed/swashbuckler-initiative). The virtuous bravo's paladin
levels stack with any swashbuckler levels when using these deeds.

This ability replaces the paladin's spellcasting.

## Advanced Deeds (Ex) {#advanced-deeds}

At 11th level, a virtuous bravo gains the following swashbuckler deeds:
[bleeding wound](ref/swashdeed/bleeding-wound), [evasive](ref/swashdeed/evasive),
[subtle blade](ref/swashdeed/subtle-blade), [superior feint](ref/swashdeed/superior-feint),
[swashbuckler's grace](ref/swashdeed/swashbucklers-grace), and targeted strike.

This ability replaces aura of justice.

## Bravo's Holy Strike (Su) {#bravo-s-holy-strike}

At 20th level, a virtuous bravo becomes a master at dispensing holy justice with her blade. When the
virtuous bravo confirms a critical hit with a light or one-handed piercing melee weapon, she can
choose one of the following three effects in addition to dealing damage: the target is rendered
[unconscious](ref/misc/unconscious) for 1d4 hours, the target is [paralyzed](ref/rule/paralyzed) for
2d6 rounds, or the target is slain. Regardless of the effect chosen, the target can attempt a
Fortitude save. On a success, the target is instead [stunned](ref/misc/stunned) for 1 round (it
still takes damage). The DC of this save is equal to 10 + 1/2 the virtuous bravo's paladin level +
her Charisma modifier. Once a creature has been the target of a bravo's holy strike, regardless of
whether or not it succeeds at the save, that creature is immune to that bravo's holy strike for 24
hours. Creatures that are immune to critical hits are also immune to this ability.

This ability replaces holy champion.
