+++
id = "ref/arc-cavalier/disciple-of-the-pike"
kind = "archetype"
title = "Disciple of the Pike"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Disciple%20of%20the%20Pike"
source_ids = ["monster-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "disciple_of_the_pike", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "monster-hunters-handbook"
page = "13"

[fields]
kind = "archetype"
features = [
  { anchor = "bigger-they-are", level = 1 },
  { anchor = "pike-charge", level = 3 },
  { anchor = "monster-hunter", level = 4 },
  { anchor = "weapon-training", level = 5 },
  { anchor = "agile-charger", level = 11 },
  { anchor = "deadly-charge", level = 20 },
]
trades = [
  { replaces = "Mount", feature = "mount", by = ["bigger-they-are"] },
  { replaces = "Cavalier's charge", feature = "cavalier-s-charge", by = ["pike-charge"] },
  { replaces = "Expert trainer", feature = "expert-trainer", by = ["monster-hunter"] },
  { replaces = "Banner", feature = "banner", by = ["weapon-training"] },
  { replaces = "greater banner", feature = "greater-banner", by = ["weapon-training"] },
  { replaces = "Mighty charge", feature = "mighty-charge", by = ["agile-charger"] },
  { replaces = "Supreme charge", feature = "supreme-charge", by = ["deadly-charge"] },
]
+++

The [Hellknight](ref/rule/aff-lawknights)
[Order of the Pike](ref/hkorder/order-of-the-pike-minor-order) are renowned monster hunters, taking
on large game using ancient weapon arts combined with modern equipment.

## Bigger They Are (Ex) {#bigger-they-are}

A disciple of the pike gains a +1 dodge bonus to AC against creatures larger than he is. This bonus
increases by 1 if the creature is two size categories larger. At 6th level, the bonus increases to
+3 against a creature three size categories larger, and at 12th level, the bonus increases to +4
against creatures four size categories larger.

This ability replaces mount.

## Pike Charge (Ex) {#pike-charge}

At 3rd level, a disciple of the pike learns to make more accurate [charge](ref/rule/charge) attacks
with weapons from the polearms or spears [fighter weapon group](ref/ability/weapon-groups). He
receives a +4 bonus on melee attacks when charging with a polearm or spear (instead of the normal
+2). In addition, the disciple of the pike takes no penalty to his AC after making a charge attack
with a polearm or spear.

This ability replaces cavalier's charge.

## Monster Hunter (Ex) {#monster-hunter}

At 4th level, a disciple of the pike has an uncanny ability to identify monsters. He can attempt
Knowledge checks untrained to identify monsters and their weaknesses, and gains a bonus equal to
[half](ref/misc/fractions-and-rounding) of his cavalier level on Knowledge checks to identify
monsters.

This ability replaces expert trainer.

## Weapon Training (Ex) {#weapon-training}

At 5th level, a disciple of the pike gains weapon training, just like a
[fighter](ref/class/fighter). He must select polearms or spears as his
[weapon group](ref/ability/weapon-groups), and never gains another weapon group. His bonuses with
the selected group otherwise progress as though his fighter level were equal to his cavalier level.

This ability replaces banner and greater banner.

## Agile Charger (Ex) {#agile-charger}

At 11th level, a disciple of the pike takes no penalties caused by
[difficult terrain](ref/rule/terrain-and-obstacles) while charging. His movement is still hampered
by obstacles, poor visibility, and other conditions. This ability doesn't allow him to move through
impassible terrain.

This ability replaces mighty charge.

## Deadly Charge (Ex) {#deadly-charge}

At 20th level, whenever a disciple of the pike makes a charge attack with a polearm or spear, he
deals double the normal amount of damage. In addition, if he confirms a critical hit on a deadly
charge, the target is [stunned](ref/misc/stunned) for 1d4 rounds. If the target succeeds at a Will
save (DC = 10 + the cavalier's base attack bonus), it is instead [staggered](ref/misc/staggered) for
1d4 rounds.

This ability replaces supreme charge.
