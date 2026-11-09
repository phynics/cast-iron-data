+++
id = "ref/rule/magic-item-gold-piece-values"
kind = "rule"
title = "Magic Item Gold Piece Values"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "magic_item_gold_piece_values", path = "json/rules_basics04.json" },
]
[[sources]]
publication = "core-rulebook"
page = "549"

[fields]
kind = "none"
+++

Many factors must be considered when determining the price of new magic items. The easiest way to
come up with a price is to compare the new item to an item that is already priced, using that price
as a guide. Otherwise, use the guidelines summarized on the table below.

**Multiple Similar Abilities:** For items with multiple similar abilities that don't take up space
on a character's body, use the following formula: Calculate the price of the single most costly
ability, then add 75% of the value of the next most costly ability, plus 1/2 the value of any other
abilities.

**Multiple Different Abilities:** Abilities such as an attack roll bonus or saving throw bonus and a
spell-like function are not similar, and their values are simply added together to determine the
cost. For items that take up a space on a character's body, each additional power not only has no
discount but instead has a 50% increase in price.

**0-Level Spells:** When multiplying spell levels to determine value, 0-level spells should be
treated as 1/2 level.

**Other Considerations:** Once you have a cost figure, reduce that number if either of the following
conditions applies:

**Item Requires Skill to Use:** Some items require a specific skill to get them to function. This
factor should reduce the cost about 10%.

**Item Requires Specific Class or Alignment to Use:** Even more restrictive than requiring a skill,
this limitation cuts the price by 30%.

Prices presented in the magic item descriptions (the gold piece value following the item's slot) are
the market value, which is generally twice what it costs the creator to make the item. Since
different classes get access to certain spells at different levels, the prices for two characters to
make the same item might actually be different. An item is only worth two times what the caster of
the lowest possible level can make it for. Calculate the market price based on the lowest possible
level caster, no matter who makes the item.

Not all items adhere to these formulas. First and foremost, these few formulas aren't enough to
truly gauge the exact differences between items. The price of a magic item may be modified based on
its actual worth. The formulas only provide a starting point. The pricing of scrolls assumes that,
whenever possible, a wizard or cleric created it. Potions and wands follow the formulas exactly.
Staves follow the formulas closely, and other items require at least some judgment calls.

> **Also See:** [Magic Item Creation (Advanced Magic Topics)](ref/rule/magic-item-creation-ucp)

### Estimating Magic Item Gold Piece Values

|Effect|Base Price|Example|
| --- | --- | --- |
|Ability bonus (enhancement)|Bonus squared × 1,000 gp|Belt of incredible dexterity +2|
|Armor bonus (enhancement)|Bonus squared × 1,000 gp|+1 chainmail|
|Bonus spell|Spell level squared × 1,000 gp|Pearl of power|
|AC bonus (deflection)|bonus squared × 2,000 gp|Ring of protection +3|
|AC bonus (other)^[1](ref/rule/magic-item-gold-piece-values#footnote-1)^|bonus squared × 2,500 gp|Ioun stone (dusty rose prism)|
|Natural armor bonus (enhancement)|bonus squared × 2,000 gp|Amulet of natural armor +1|
|Save bonus (resistance)|bonus squared × 1,000 gp|Cloak of resistance +5|
|Save bonus (other)^[1](ref/rule/magic-item-gold-piece-values#footnote-1)^|bonus squared × 2,000 gp|Stone of good luck|
|Skill bonus (competence)|bonus squared × 100 gp|Cloak of elvenkind|
|[Spell resistance](ref/rule/spell-resistance)|10,000 gp per point over SR 12; SR 13 minimum|Mantle of [spell resistance](ref/rule/spell-resistance)|
|Weapon bonus (enhancement)|bonus squared × 2,000 gp|+1 longsword|

### Estimating by Spell Effect

|Spell Effect|Base Price|Example|
| --- | --- | --- |
|Single use, spell completion|Spell level × caster level × 25 gp|Scroll of haste|
|Single use, use-activated|Spell level × caster level × 50 gp|Potion of cure light wounds|
|50 charges, spell trigger|Spell level × caster level × 750 gp|Wand of fireball|
|Command word|Spell level × caster level × 1,800 gp|Cape of the mountebank|
|Use-activated or continuous|Spell level × caster level × 2,000 gp^[2](ref/rule/magic-item-gold-piece-values#footnote-2)^|Lantern of revealing|

### Estimating by Other Variables

|Special|Base Price Adjustment|Example|
| --- | --- | --- |
|Charges per day|Divide by (5 divided by charges per day)|Boots of teleportation|
|No space limitation^[3](ref/rule/magic-item-gold-piece-values#footnote-3)^|Multiply entire cost by 2|Ioun stone|
|Multiple different abilities|Multiply lower item cost by 1.5|Helm of brilliance|
|Charged (50 charges)|1/2 unlimited use base price|Ring of the ram|
|Component|Extra Cost|Example|
|Armor, shield, or weapon|Add cost of masterwork item|+1 composite longbow|
|Spell has material component cost|Add directly into price of item per charge^[4](ref/rule/magic-item-gold-piece-values#footnote-4)^|Wand of stoneskin|

**Spell Level:** A 0-level spell is half the value of a 1st-level spell for determining price.

###### ^1^ {#footnote-1}

Such as a luck, insight, sacred, or profane bonus.

###### ^2^ {#footnote-2}

If a continuous item has an effect based on a spell with a duration measured in rounds, multiply the
cost by 4. If the duration of the spell is 1 minute/level, multiply the cost by 2, and if the
duration is 10 minutes/level, multiply the cost by 1.5. If the spell has a 24-hour duration or
greater, divide the cost in half.

###### ^3^ {#footnote-3}

An item that does not take up one of the spaces on a body costs double.

###### ^4^ {#footnote-4}

If item is continuous or unlimited, not charged, determine cost as if it had 100 charges. If it has
some daily limit, determine as if it had 50 charges.
