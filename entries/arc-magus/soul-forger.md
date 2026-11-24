+++
id = "ref/arc-magus/soul-forger"
kind = "archetype"
title = "Soul Forger"
aon = "ArchetypeDisplay.aspx?FixedName=Magus%20Soul%20Forger"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "soul_forger", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]
[[sources]]
publication = "ultimate-combat"
page = "57"

[fields]
kind = "archetype"
features = [
  { anchor = "diminished-spellcasting" },
  { anchor = "arcane-bond", level = 1 },
  { anchor = "spell-combat" },
  { anchor = "spellstrike" },
  { anchor = "master-smith" },
  { anchor = "fortify-bond", level = 4 },
  { anchor = "reforge", level = 11 },
  { anchor = "destructive-counterstrike", level = 16 },
  { anchor = "instantaneous-reconstruction", level = 19 },
]
trades = [
  { replaces = "Knowledge pool", feature = "knowledge-pool", by = ["master-smith"] },
  { replaces = "Spell recall", feature = "spell-recall", by = ["fortify-bond"] },
  { replaces = "Improved spell recall", feature = "improved-spell-recall", by = ["reforge"] },
  { replaces = "Counterstrike", feature = "counterstrike", by = ["destructive-counterstrike"] },
  { replaces = "Greater spell access", feature = "greater-spell-access", by = ["instantaneous-reconstruction"] },
  { alters = "Spell combat", feature = "spell-combat", by = ["spell-combat"] },
  { alters = "Spellstrike", feature = "spellstrike", by = ["spellstrike"] },
]
+++

The soul forger has learned the skill of infusing the raw magical essence of his soul into armaments
of surpassing power, combining the mystic arts with the arts of war in a unity of steely perfection.

## Diminished Spellcasting {#diminished-spellcasting}

A soul forger casts one fewer spell of each level than normal. If this reduces the number to 0, he
may cast spells of that level only if his Intelligence allows
[bonus spells](ref/rule/determine-bonuses) of that level.

## Arcane Bond (Su) {#arcane-bond}

At 1st level, a soul forger gains a weapon as an arcane bond item. This is identical to the
[wizard](ref/class/wizard) class ability, but the soul forger must select a weapon.

## Spell Combat (Su) {#spell-combat}

A soul forger may use this ability only when wielding his bonded weapon.

## Spellstrike (Su) {#spellstrike}

A soul forger may use this ability only when wielding his bonded weapon.

## Master Smith (Ex) {#master-smith}

A soul forger adds his magus class level on [Craft](ref/skill/craft-any) checks to manufacture
armor, shields, and weapons. This bonus applies on skill checks required when using
[Craft Magic Arms and Armor](ref/feat/craft-magic-arms-and-armor).

At 7th level, a soul forger uses the 1/10 gp value of armor, shields, and weapons to determine how
much time it takes to craft mundane items, and he requires only half the normal amount of time to
enchant magical arms and armor. This ability replaces knowledge pool.

## Fortify Bond (Su) {#fortify-bond}

At 4th level, a soul forger may spend 1 point from his arcane pool to increase the
[hardness](ref/umr/hardness) and hit points of his bonded item by an amount equal to his magus
level. These hit points last until expended or until the soul forger next prepares spells. Multiple
uses of this ability overlap and do not stack. This ability replaces spell recall.

## Reforge (Su) {#reforge}

At 11th level, as a standard action, a soul forger can restore a number of hit points equal to his
magus level to a damaged object by touching it and spending 1 point from his arcane pool. Repairing
a destroyed object takes 1 minute and materials equal to 1/4 the item's sale value, and restores the
object to 1 hit point.

Restoring the enchantments of a destroyed magical item requires additional points from the soul
forger's arcane pool equal to the item's caster level. The soul forger gains one temporary
[negative level](ref/rule/energy-drain-and-negative-levels) if the item's caster level is lower than
his own, two negative levels if equal or greater (or none if the item is his bonded weapon); the
save DC to remove these negative levels is equal to 10 + the item's caster level. This ability
replaces improved spell recall.

## Destructive Counterstrike (Su) {#destructive-counterstrike}

At 16th level, an opponent who activates a magical item while threatened by a soul forger provokes
an attack of opportunity, either against the target or to [sunder](ref/rule/sunder) the item. If the
item is destroyed, its effects are negated. This ability replaces counterstrike.

## Instantaneous Reconstruction (Su) {#instantaneous-reconstruction}

At 19th level, a soul forger can reforge a destroyed item by touch as a standard action that does
not provoke attacks of opportunity. This ability replaces greater spell access.

## Magus Arcana {#magus-arcana}

The following magus arcana complement the soul forger archetype:
[arcane accuracy](ref/arcana/arcane-accuracy), [bane blade](ref/arcana/bane-blade),
[devoted blade](ref/arcana/devoted-blade), [dispelling strike](ref/arcana/dispelling-strike),
[enduring blade](ref/arcana/enduring-blade), and [ghost blade](ref/arcana/ghost-blade).
