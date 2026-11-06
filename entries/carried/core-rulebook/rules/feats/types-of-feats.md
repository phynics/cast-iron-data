+++
id = "ref/carried/core-rulebook/rules/feats/types-of-feats"
kind = "rule"
title = "Types of Feats"
source_ids = ["core-rulebook"]
section = ["Rules", "Feats"]
parent = "ref/rule/feats"
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Rules/Feats/Types of Feats", path = "core_rulebook/rules/feats.json" },
]

[fields]
kind = "none"
+++

Some feats are general, meaning that no special rules govern them as a group. Others are item
creation feats, which allow characters to create magic items of all sorts. A metamagic feat lets a
spellcaster prepare and cast a spell with greater effect, albeit as if the spell were of a higher
spell level than it actually is.

## Combat Feats {#combat-feats}

Any feat designated as a combat feat can be selected as a fighter's bonus feat. This designation
does not restrict characters of other classes from selecting these feats, assuming that they meet
the prerequisites.

## Critical Feats {#critical-feats}

Critical feats modify the effects of a critical hit by inflicting an additional condition on the
victim of the critical hit. Characters without the Critical Mastery feat can only apply the effects
of one critical feat to an individual critical hit. Characters with multiple critical feats can
decide which feat to apply after the critical hit has been confirmed.

## Item Creation Feats {#item-creation-feats}

An item creation feat lets a character create a magic item of a certain type. Regardless of the type
of item each involves, the various item creation feats all have certain features in common.

### Raw Materials Cost {#raw-materials-cost}

The cost of creating a magic item equals half the base price of the item.

Using an item creation feat also requires access to a laboratory or magical workshop, special tools,
and so on. A character generally has access to what he needs unless unusual circumstances apply.

### Time {#time}

The time to create a magic item depends on the feat and the cost of the item.

### Item Cost {#item-cost}

Brew Potion, Craft Staff, Craft Wand, and Scribe Scroll create items that directly reproduce spell
effects, and the power of these items depends on their caster level—that is, a spell from such an
item has the power it would have if cast by a spellcaster of that level. The price of these items
(and thus the cost of the raw materials) also depends on the caster level. The caster level must be
low enough that the spellcaster creating the item can cast the spell at that level. To find the
final price in each case, multiply the caster level by the spell level, then multiply the result by
a constant, as shown below:

**_Scrolls:_ Base price = spell level × caster level × 25 gp.****_Potions:_ Base price = spell level
× caster level × 50 gp.****_Wands:_ Base price = spell level × caster level × 750 gp.****_Staves:_
The price for staves is calculated using more complex formulas (see Magic Items).**

A 0-level spell is considered to have a spell level of 1/2 for the purpose of this calculation.

### Extra Costs {#extra-costs}

Any potion, scroll, or wand that stores a spell with a costly material component also carries a
commensurate cost. For potions and scrolls, the creator must expend the material component cost when
creating the item. For a wand, the creator must expend 50 units of the material component. Some
magic items similarly incur extra costs in material components, as noted in their descriptions.

### Skill Check {#skill-check}

Successfully creating a magic item requires a Spellcraft check with a DC equal to 5 + the item's
caster level. Alternatively, you can use an associated Craft or Profession skill to attempt this
check instead, depending upon the item being crafted. See Magic Item Creation for more details on
which Craft and Profession checks may be substituted in this manner. The DC of this check can
increase if the crafter is rushed or does not meet all of the prerequisites. A failed check ruins
the materials used, while a check that fails by 5 or more results in a cursed item. See Magic Items
for more details.

## Metamagic Feats {#metamagic-feats}

As a spellcaster's knowledge of magic grows, he can learn to cast spells in ways slightly different
from the norm. Preparing and casting a spell in such a way is harder than normal but, thanks to
metamagic feats, is at least possible. Spells modified by a metamagic feat use a spell slot higher
than normal. This does not change the level of the spell, so the DC for saving throws against it
does not go up. Metamagic feats do not affect [spell-like abilities](ref/umr/spell-like-abilities).

### Wizards and Divine Spellcasters {#wizards-and-divine-spellcasters}

Wizards and divine spellcasters must prepare their spells in advance. During preparation, the
character chooses which spells to prepare with metamagic feats (and thus which ones take up
higher-level spell slots than normal).

### Sorcerers and Bards {#sorcerers-and-bards}

Sorcerers and bards choose spells as they cast them. They can choose when they cast their spells
whether to apply their metamagic feats to improve them. As with other spellcasters, the improved
spell uses up a higher-level spell slot. Because the sorcerer or bard has not prepared the spell in
a metamagic form in advance, he must apply the metamagic feat on the spot. Therefore, such a
character must also take more time to cast a metamagic spell (one enhanced by a metamagic feat) than
he does to cast a regular spell. If the spell's normal casting time is a standard action, casting a
metamagic version is a full-round action for a sorcerer or bard. (This isn't the same as a 1-round
casting time.) The only exception is for spells modified by the Quicken Spell metamagic feat, which
can be cast as normal using the feat.

For a spell with a longer casting time, it takes an extra full-round action to cast the spell.

### Spontaneous Casting and Metamagic Feats {#spontaneous-casting-and-metamagic-feats}

A cleric spontaneously casting a cure or inflict spell, or a druid spontaneously casting a
_[summon nature's ally](ref/spell/summon-natures-ally)_ spell, can cast a metamagic version of it
instead. Extra time is also required in this case. Casting a standard action metamagic spell
spontaneously is a full-round action, and a spell with a longer casting time takes an extra
full-round action to cast. The only exception is for spells modified by the Quicken Spell feat,
which can be cast as a swift action.

### Effects of Metamagic Feats on a Spell {#effects-of-metamagic-feats-on-a-spell}

In all ways, a metamagic spell operates at its original spell level, even though it is prepared and
cast using a higher-level spell slot. Saving throw modifications are not changed unless stated
otherwise in the feat description.

The modifications made by these feats only apply to spells cast directly by the feat user. A
spellcaster can't use a metamagic feat to alter a spell being cast from a wand, scroll, or other
device.

Metamagic feats that eliminate components of a spell don't eliminate the attack of opportunity
provoked by casting a spell while threatened. Casting a spell modified by Quicken Spell does not
provoke an attack of opportunity.

Metamagic feats cannot be used with all spells. See the specific feat descriptions for the spells
that a particular feat can't modify.

### Multiple Metamagic Feats on a Spell {#multiple-metamagic-feats-on-a-spell}

A spellcaster can apply multiple metamagic feats to a single spell. Changes to its level are
cumulative. You can't apply the same metamagic feat more than once to a single spell.

### Magic Items and Metamagic Spells {#magic-items-and-metamagic-spells}

With the right item creation feat, you can store a metamagic version of a spell in a scroll, potion,
or wand. Level limits for potions and wands apply to the spell's higher spell level (after the
application of the metamagic feat). A character doesn't need the metamagic feat to activate an item
storing a metamagic version of a spell.

### Counterspelling Metamagic Spells {#counterspelling-metamagic-spells}

Whether or not a spell has been enhanced by a metamagic feat does not affect its vulnerability to
counterspelling or its ability to counterspell another spell (see Magic).
