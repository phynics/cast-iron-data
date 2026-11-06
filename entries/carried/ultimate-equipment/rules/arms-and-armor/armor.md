+++
id = "ref/carried/ultimate-equipment/rules/arms-and-armor/armor"
kind = "rule"
title = "Armor"
source_ids = ["ultimate-equipment"]
section = ["Rules", "Arms And Armor"]
parent = "ref/carried/ultimate-equipment/rules/arms-and-armor"
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Equipment/Rules/Arms And Armor/Armor", path = "ultimate_equipment/rules/arms_and_armor.json" },
]

[fields]
kind = "none"
+++

For most, armor is the simplest way to protect themselves in a world of rampant threats and dangers.
Many characters can wear only the simplest of armors, and only some can use shields.

The armor entries in the Armor and Shields table contain the following information.

## Cost {#cost}

The cost in gold pieces of the armor for Small or Medium humanoid creatures. See the Armor for
Unusual Creatures table for armor prices for other creatures.

## Armor/Shield Bonus {#armor-shield-bonus}

Each type of armor grants an armor bonus to armor class (AC), while shields grant a shield bonus to
AC. The armor bonus from a suit of armor doesn't stack with other effects or items that grant an
armor bonus. Similarly, the shield bonus from a shield doesn't stack with other effects that grant a
shield bonus. In each armor category (light, medium, or heavy), the armors are listed in order from
worst AC bonus to highest AC bonus.

## Maximum Dex Bonus {#maximum-dex-bonus}

This number is the maximum Dexterity bonus to AC that this type of armor allows. Dexterity bonuses
in excess of this number are reduced to this number for the purposes of determining the wearer's AC.
Heavier armors limit mobility, reducing the wearer's ability to dodge blows. This restriction
doesn't affect any other Dexterity-related abilities. A dash indicates the armor does not affect a
character's maximum Dexterity bonus.

Even if a character's Dexterity bonus to AC drops to 0 because of armor, this situation does not
count as losing his Dexterity bonus to AC.

A character's encumbrance (the amount of gear carried, including armor) may also restrict the
maximum Dexterity bonus that can be applied to his Armor Class.

### Shields {#shields}

Shields do not affect a character's maximum dexterity bonus, except for tower shields.

## Armor Check Penalty {#armor-check-penalty}

Any armor heavier than leather, as well as any shield, applies an armor check penalty to all
Dexterity- and Strength-based skill checks. A character's encumbrance may also incur an armor check
penalty.

### Shields {#shields-2}

If a character is wearing armor and using a shield, both armor check penalties apply.

### Nonproficient with Armor Worn {#nonproficient-with-armor-worn}

A character who wears armor and/or uses a shield with which he is not proficient takes the armor's
(and/or shield's) armor check penalty on attack rolls as well as on all dexterity- and
strength-based ability and skill checks. the penalty for nonproficiency with armor stacks with the
penalty for shields.

### Sleeping in Armor {#sleeping-in-armor}

A character who sleeps in medium or heavy armor is automatically fatigued the next day. He takes a
–2 penalty on strength and dexterity and can't charge or run. sleeping in light armor does not cause
fatigue.

## Arcane Spell Failure Chance {#arcane-spell-failure-chance}

Armor interferes with the gestures that a spellcaster must make to cast an arcane spell that has a
somatic component. Arcane spellcasters face the possibility of arcane spell failure if they're
wearing armor. Bards, magi, and summoners have class features which allow them to wear certain
armors or even shields without incurring any arcane spell failure chance for casting spells from
their class spell list.

### Casting an Arcane Spell in Armor {#casting-an-arcane-spell-in-armor}

A character who casts an arcane spell while wearing armor must usually make an arcane spell failure
check. The number in the arcane spell failure chance column in the Armor and Shields table is the
percentage chance that the spell fails and is ruined. if the spell lacks a somatic component,
however, it can be cast with no chance of arcane spell failure.

### Shields {#shields-3}

If a character is wearing armor and using a shield, add the two arcane spell failure chances
together to get a single arcane spell failure chance.

## Speed {#speed}

Medium or heavy armor slows the wearer down. The number in the Armor and Shields table is the
character's speed while wearing the armor. Humans, elves, half-elves, and half-orcs have an
unencumbered speed of 30 feet. They use the first column. Dwarves, gnomes, and halflings have an
unencumbered speed of 20 feet. They use the second column. Remember, however, that a dwarf's land
speed remains 20 feet even in medium or heavy armor or when carrying a medium or heavy load.

### Shields {#shields-4}

Shields do not affect a character's speed.

## Weight {#weight}

This column gives the weight of the armor sized for a Medium wearer. Armor fitted for Small
characters weighs half as much, and armor for Large characters weighs twice as much.

## Armor Special Features {#armor-special-features}

Some armors, particularly those made out of primitive materials, are inferior compared to standard
equipment. These armors have the fragile special feature.

### Fragile {#fragile}

Armor with the fragile quality falls apart when hit with heavy blows. if an attacker hits a creature
wearing fragile armor with an attack roll of a natural 20 and confirms the critical hit (even if the
creature is immune to critical hits), the armor gains the broken condition. if already broken, the
armor is destroyed instead. Fragile armor is broken or destroyed by only critical threats that are
generated by natural 20s.

Masterwork and magical fragile armor lacks these flaws unless otherwise noted in the item
description or the special material description.

If armor gains the broken condition in this way, that armor is considered to have taken damage equal
to half its hit points +1. This damage is repaired either by something that addresses the effect
that granted the armor the broken condition (like the Field Repair feat) or the repair methods
described in the broken condition. When an effect that grants the broken condition is removed, the
armor regains the hit points it lost when the broken condition was applied. Damage done by an attack
against armor (such as from a sunder combat maneuver) cannot be repaired by an effect that removes
the broken condition.

## Masterwork Armor {#masterwork-armor}

Just as with weapons, you can purchase or craft masterwork versions of armor or shields. Such a
well-made item functions like the normal version, except that its armor check penalty is lessened
by 1.

The _[masterwork transformation](ref/spell/masterwork-transformation)_ spell transforms a
non-masterwork weapon into a masterwork weapon. Without using magic, you can't add the masterwork
quality to armor or a shield after it is created; it must be crafted as a masterwork item (see the
Craft skill).

A masterwork suit of armor or shield costs an extra 150 gp over and above the normal price for that
type of armor or shield.

The masterwork quality of a suit of armor or shield never provides a bonus on attack or damage
rolls, even if the armor or shield is used as a weapon.

All magic armors and shields are automatically considered to be of masterwork quality.

Even though some types of armor and shields can be used as weapons, you can't create a masterwork
version of such an item that confers an enhancement bonus on attack rolls. However, you can create
masterwork armor spikes and shield spikes, which do confer their enhancement bonus on attack rolls
to attacks made with the spikes.

## Variant Rule: Armor as DR {#variant-rule-armor-as-dr}

The armor and Armor Class system is an abstraction where an attack roll that "misses" represents
actual misses as well as attacks that fail to hit the target hard or accurately enough to cause
harm. Some players and GMs may prefer a different system where a failed attack roll is an actual
miss, and armor absorbs points of damage from successful attacks.

A variant set of rules for this game mechanic is presented in _Ultimate Combat_. In this system, a
creature has a defense score instead of an armor class (representing how easy or difficult it is to
hit a creature), and the armor's armor class value indicates how many points of dr it grants against
incoming attacks. This increases the bookkeeping burden for creatures with armor, but may give more
satisfying results.

## Variant Rule: Piecemeal Armor {#variant-rule-piecemeal-armor}

All armor in the Pathfinder Roleplaying Game assumes you're dealing with a full suit of armor that
you're either wearing in its entirety or not wearing at all. However, sometimes you don't have time
to put on an entire suit of armor or don't have access to a complete suit, and must make do with
wearing only part of a complete set. A variant set of rules for this option is presented in
_Ultimate Combat_.

## Armor for Unusual Creatures {#armor-for-unusual-creatures}

Armor and shields for unusually big creatures, unusually little creatures, and non-humanoid
creatures (such as horses) have different prices and weights from those given in the Armor and
Shields table. Refer to the appropriate line on the table below and apply the multipliers to price
and weight for the armor type in question.

### Armor for Unusual Creatures {#armor-for-unusual-creatures-2}

::: table
caption = "Armor for Unusual Creatures"
head = [
  [
    { text = "Size", header = true },
    { text = "HumanoidPrice Weight", header = true, colspan = 2 },
    { text = "Non-HumanoidPrice Weight", header = true, colspan = 2 },
  ],
]
body = [
  [
    { text = "Tiny or smaller\\*" },
    { text = "×1/2" },
    { text = "×1/10" },
    { text = "×1" },
    { text = "×1/10" },
  ],
  [
    { text = "Small" },
    { text = "×1" },
    { text = "×1/2" },
    { text = "×2" },
    { text = "×1/2" },
  ],
  [
    { text = "Medium" },
    { text = "×1" },
    { text = "×1" },
    { text = "×2" },
    { text = "×1" },
  ],
  [
    { text = "Large" },
    { text = "×2" },
    { text = "×2" },
    { text = "×4" },
    { text = "×2" },
  ],
  [
    { text = "Huge" },
    { text = "×4" },
    { text = "×5" },
    { text = "×8" },
    { text = "×5" },
  ],
  [
    { text = "Gargantuan" },
    { text = "×8" },
    { text = "×8" },
    { text = "×16" },
    { text = "×8" },
  ],
  [
    { text = "Colossal" },
    { text = "×16" },
    { text = "×12" },
    { text = "×32" },
    { text = "×12" },
  ],
]
foot = [
  [
    { text = "\\*Divide armor bonus by 2.", colspan = 5 },
  ],
]
:::

## Getting Into and Out of Armor {#getting-into-and-out-of-armor}

Putting on or taking off armor is a sometimes complicated procedure. The time required to don armor
depends on its type; see the table below.

### Don {#don}

This column tells how long it takes a character to put the armor on. (One minute is 10 rounds.)
Readying (strapping on) a shield is only a move action.

### Don Hastily {#don-hastily}

This column tells how long it takes to put the armor on in a hurry. The armor check penalty and
armor bonus for hastily donned armor are each 1 point worse than normal.

### Remove {#remove}

This column tells how long it takes to get the armor off. Removing a shield from your arm and
dropping it is only a move action.

#### Donning Armor {#donning-armor}

::: table
caption = "Donning Armor"
head = [
  [
    { text = "Armor type", header = true },
    { text = "Don", header = true },
    { text = "Don Hastily", header = true },
    { text = "Remove", header = true },
  ],
]
body = [
  [
    { text = "Shield (any)" },
    { text = "1 move action" },
    { text = "N/A" },
    { text = "1 move action" },
  ],
  [
    { text = "Padded, leather, hide, studded leather, or chain shirt" },
    { text = "1 minute" },
    { text = "5 rounds" },
    { text = "1 minute^1^" },
  ],
  [
    { text = "Breastplate, scale mail, chainmail, banded mail, or splint mail" },
    { text = "4 minutes^1^" },
    { text = "1 minute" },
    { text = "1 minute^1^" },
  ],
  [
    { text = "Half-plate or full plate" },
    { text = "4 minutes^2^" },
    { text = "4 minutes^1^" },
    { text = "1d4+1 minutes^1^" },
  ],
]
foot = [
  [
    { text = "^1^ If the character has some help, cut this time in half. A single character doing nothing else can help one or two adjacent characters.Two characters can't help each other don armor at the same time.^2^ The wearer must have help to don this armor. Without help, it can only be donned hastily.", colspan = 4 },
  ],
]
:::

## Armor and Shields {#armor-and-shields}

### Armor and Shields {#armor-and-shields-2}

::: table
caption = "Armor and Shields"
head = [
  [
    { text = "Light Armor", header = true },
    { text = "Price", header = true },
    { text = "Armor/ShieldBonus", header = true },
    { text = "MaxDex Bonus", header = true },
    { text = "ArmorCheck Penalty", header = true },
    { text = "Arcane SpellFailure Chance", header = true },
    { text = "Speed30 ft. 20 ft.", header = true, colspan = 2 },
    { text = "Weight^1^", header = true },
  ],
  [
    { text = "Medium Armor", header = true },
    { text = "Price", header = true },
    { text = "Armor/ShieldBonus", header = true },
    { text = "MaxDex Bonus", header = true },
    { text = "ArmorCheck Penalty", header = true },
    { text = "Arcane SpellFailure Chance", header = true },
    { text = "Speed30 ft. 20 ft.", header = true, colspan = 2 },
    { text = "Weight^1^", header = true },
  ],
  [
    { text = "Heavy Armor", header = true },
    { text = "Price", header = true },
    { text = "Armor/ShieldBonus", header = true },
    { text = "MaxDex Bonus", header = true },
    { text = "ArmorCheck Penalty", header = true },
    { text = "Arcane SpellFailure Chance", header = true },
    { text = "Speed30 ft. 20 ft.", header = true, colspan = 2 },
    { text = "Weight^1^", header = true },
  ],
  [
    { text = "Shields", header = true },
    { text = "Price", header = true },
    { text = "Armor/ShieldBonus", header = true },
    { text = "MaxDex Bonus", header = true },
    { text = "ArmorCheck Penalty", header = true },
    { text = "Arcane SpellFailure Chance", header = true },
    { text = "Speed30 ft. 20 ft.", header = true, colspan = 2 },
    { text = "Weight^1^", header = true },
  ],
  [
    { text = "Extras", header = true },
    { text = "Price", header = true },
    { text = "Armor/ShieldBonus", header = true },
    { text = "MaxDex Bonus", header = true },
    { text = "ArmorCheck Penalty", header = true },
    { text = "Arcane SpellFailure Chance", header = true },
    { text = "Speed30 ft. 20 ft.", header = true, colspan = 2 },
    { text = "Weight^1^", header = true },
  ],
]
body = [
  [
    { text = "Haramaki" },
    { text = "3 gp" },
    { text = "+1" },
    { text = "—" },
    { text = "0" },
    { text = "0%" },
    { text = "30 ft." },
    { text = "20 ft." },
    { text = "1 lb." },
  ],
  [
    { text = "Padded" },
    { text = "5 gp" },
    { text = "+1" },
    { text = "+8" },
    { text = "0" },
    { text = "5%" },
    { text = "30 ft." },
    { text = "20 ft." },
    { text = "10 lbs." },
  ],
  [
    { text = "Quilted cloth" },
    { text = "100 gp" },
    { text = "+1" },
    { text = "+8" },
    { text = "0" },
    { text = "10%" },
    { text = "30 ft." },
    { text = "20 ft." },
    { text = "15 lbs." },
  ],
  [
    { text = "Silken ceremonial" },
    { text = "30 gp" },
    { text = "+1" },
    { text = "—" },
    { text = "0" },
    { text = "0%" },
    { text = "30 ft." },
    { text = "20 ft." },
    { text = "4 lbs." },
  ],
  [
    { text = "Lamellar cuirass" },
    { text = "15 gp" },
    { text = "+2" },
    { text = "+4" },
    { text = "0" },
    { text = "5%" },
    { text = "30 ft." },
    { text = "20 ft." },
    { text = "8 lbs." },
  ],
  [
    { text = "Leather" },
    { text = "10 gp" },
    { text = "+2" },
    { text = "+6" },
    { text = "0" },
    { text = "10%" },
    { text = "30 ft." },
    { text = "20 ft." },
    { text = "15 lbs." },
  ],
  [
    { text = "Parade" },
    { text = "25 gp" },
    { text = "+3" },
    { text = "+5" },
    { text = "–1" },
    { text = "15%" },
    { text = "30 ft." },
    { text = "20 ft." },
    { text = "20 lbs." },
  ],
  [
    { text = "Studded leather" },
    { text = "25 gp" },
    { text = "+3" },
    { text = "+5" },
    { text = "–1" },
    { text = "15%" },
    { text = "30 ft." },
    { text = "20 ft." },
    { text = "20 lbs" },
  ],
  [
    { text = "Wooden" },
    { text = "20 gp" },
    { text = "+3" },
    { text = "+3" },
    { text = "–1" },
    { text = "15%" },
    { text = "30 ft." },
    { text = "20 ft." },
    { text = "25 lbs." },
  ],
  [
    { text = "Chain shirt" },
    { text = "100 gp" },
    { text = "+4" },
    { text = "+4" },
    { text = "–2" },
    { text = "20%" },
    { text = "30 ft." },
    { text = "20 ft." },
    { text = "25 lbs." },
  ],
  [
    { text = "Lamellar (leather)" },
    { text = "60 gp" },
    { text = "+4" },
    { text = "+3" },
    { text = "–2" },
    { text = "20%" },
    { text = "30 ft." },
    { text = "20 ft." },
    { text = "25 lbs." },
  ],
  [
    { text = "Armored coat" },
    { text = "50 gp" },
    { text = "+4" },
    { text = "+3" },
    { text = "–2" },
    { text = "20%" },
    { text = "20 ft." },
    { text = "15 ft." },
    { text = "20 lbs." },
  ],
  [
    { text = "Hide" },
    { text = "15 gp" },
    { text = "+4" },
    { text = "+4" },
    { text = "–3" },
    { text = "20%" },
    { text = "20 ft." },
    { text = "15 ft." },
    { text = "25 lbs." },
  ],
  [
    { text = "Do-maru" },
    { text = "200 gp" },
    { text = "+5" },
    { text = "+4" },
    { text = "–4" },
    { text = "25%" },
    { text = "20 ft." },
    { text = "15 ft." },
    { text = "30 lbs." },
  ],
  [
    { text = "Kikko" },
    { text = "30 gp" },
    { text = "+5" },
    { text = "+4" },
    { text = "–3" },
    { text = "20%" },
    { text = "20 ft." },
    { text = "15 ft." },
    { text = "25 lbs." },
  ],
  [
    { text = "Lamellar (horn)" },
    { text = "100 gp" },
    { text = "+5" },
    { text = "+3" },
    { text = "–4" },
    { text = "25%" },
    { text = "20 ft." },
    { text = "15 ft." },
    { text = "30 lbs." },
  ],
  [
    { text = "Scale mail" },
    { text = "50 gp" },
    { text = "+5" },
    { text = "+3" },
    { text = "–4" },
    { text = "25%" },
    { text = "20 ft." },
    { text = "15 ft." },
    { text = "30 lbs." },
  ],
  [
    { text = "Agile breastplate" },
    { text = "400 gp" },
    { text = "+6" },
    { text = "+3" },
    { text = "–4" },
    { text = "25%" },
    { text = "20 ft." },
    { text = "15 ft." },
    { text = "25 lbs." },
  ],
  [
    { text = "Breastplate" },
    { text = "200 gp" },
    { text = "+6" },
    { text = "+3" },
    { text = "–4" },
    { text = "25%" },
    { text = "20 ft." },
    { text = "15 ft." },
    { text = "30 lbs." },
  ],
  [
    { text = "Chainmail" },
    { text = "150 gp" },
    { text = "+6" },
    { text = "+2" },
    { text = "–5" },
    { text = "30%" },
    { text = "20 ft." },
    { text = "15 ft." },
    { text = "40 lbs." },
  ],
  [
    { text = "Four-mirror" },
    { text = "45 gp" },
    { text = "+6" },
    { text = "+2" },
    { text = "–5" },
    { text = "30%" },
    { text = "20 ft." },
    { text = "15 ft." },
    { text = "45 lbs." },
  ],
  [
    { text = "Lamellar (steel)" },
    { text = "150 gp" },
    { text = "+6" },
    { text = "+3" },
    { text = "–5" },
    { text = "25%" },
    { text = "20 ft." },
    { text = "15 ft." },
    { text = "35 lbs." },
  ],
  [
    { text = "Mountain pattern" },
    { text = "250 gp" },
    { text = "+6" },
    { text = "+3" },
    { text = "–4" },
    { text = "30%" },
    { text = "20 ft." },
    { text = "15 ft." },
    { text = "40 lbs." },
  ],
  [
    { text = "Banded mail" },
    { text = "250 gp" },
    { text = "+7" },
    { text = "+1" },
    { text = "–6" },
    { text = "35%" },
    { text = "20 ft.^2^" },
    { text = "15 ft.^2^" },
    { text = "35 lbs." },
  ],
  [
    { text = "Kusari gusoku" },
    { text = "350 gp" },
    { text = "+7" },
    { text = "+1" },
    { text = "–7" },
    { text = "35%" },
    { text = "20 ft.^2^" },
    { text = "15 ft.^2^" },
    { text = "45 lbs." },
  ],
  [
    { text = "Lamellar (iron)" },
    { text = "200 gp" },
    { text = "+7" },
    { text = "+0" },
    { text = "–7" },
    { text = "40%" },
    { text = "20 ft.^2^" },
    { text = "15 ft.^2^" },
    { text = "50 lbs." },
  ],
  [
    { text = "Splint mail" },
    { text = "200 gp" },
    { text = "+7" },
    { text = "+0" },
    { text = "–7" },
    { text = "40%" },
    { text = "20 ft.^2^" },
    { text = "15 ft.^2^" },
    { text = "45 lbs." },
  ],
  [
    { text = "Tatami-do" },
    { text = "1,000 gp" },
    { text = "+7" },
    { text = "+3" },
    { text = "–6" },
    { text = "35%" },
    { text = "20 ft.^2^" },
    { text = "15 ft.^2^" },
    { text = "45 lbs." },
  ],
  [
    { text = "Agile half-plate" },
    { text = "850 gp" },
    { text = "+8" },
    { text = "+0" },
    { text = "–7" },
    { text = "40%" },
    { text = "20 ft.^3^" },
    { text = "15 ft.^3^" },
    { text = "55 lbs." },
  ],
  [
    { text = "Half-plate" },
    { text = "600 gp" },
    { text = "+8" },
    { text = "+0" },
    { text = "–7" },
    { text = "40%" },
    { text = "20 ft.^2^" },
    { text = "15 ft.^2^" },
    { text = "50 lbs." },
  ],
  [
    { text = "Lamellar (stone)" },
    { text = "500 gp" },
    { text = "+8" },
    { text = "+0" },
    { text = "–7" },
    { text = "40%" },
    { text = "20 ft.^2^" },
    { text = "15 ft.^2^" },
    { text = "45 lbs." },
  ],
  [
    { text = "O-yoroi" },
    { text = "1,700 gp" },
    { text = "+8" },
    { text = "+2" },
    { text = "–6" },
    { text = "35%" },
    { text = "20 ft.^2^" },
    { text = "15 ft.^2^" },
    { text = "45 lbs." },
  ],
  [
    { text = "Full plate" },
    { text = "1,500 gp" },
    { text = "+9" },
    { text = "+1" },
    { text = "–6" },
    { text = "35%" },
    { text = "20 ft.^2^" },
    { text = "15 ft.^2^" },
    { text = "50 lbs." },
  ],
  [
    { text = "Buckler" },
    { text = "5 gp" },
    { text = "+1" },
    { text = "—" },
    { text = "–1" },
    { text = "5%" },
    { text = "—" },
    { text = "—" },
    { text = "5 lbs." },
  ],
  [
    { text = "Klar" },
    { text = "12 gp" },
    { text = "+1" },
    { text = "—" },
    { text = "–1" },
    { text = "5%" },
    { text = "—" },
    { text = "—" },
    { text = "6 lbs." },
  ],
  [
    { text = "Light steel quickdraw" },
    { text = "59 gp" },
    { text = "+1" },
    { text = "—" },
    { text = "–2" },
    { text = "5%" },
    { text = "—" },
    { text = "—" },
    { text = "7 lbs." },
  ],
  [
    { text = "Light steel" },
    { text = "9 gp" },
    { text = "+1" },
    { text = "—" },
    { text = "–1" },
    { text = "5%" },
    { text = "—" },
    { text = "—" },
    { text = "6 lbs." },
  ],
  [
    { text = "Light wooden quickdraw" },
    { text = "53 gp" },
    { text = "+1" },
    { text = "—" },
    { text = "–2" },
    { text = "5%" },
    { text = "—" },
    { text = "—" },
    { text = "6 lbs." },
  ],
  [
    { text = "Light wooden" },
    { text = "3 gp" },
    { text = "+1" },
    { text = "—" },
    { text = "–1" },
    { text = "5%" },
    { text = "—" },
    { text = "—" },
    { text = "5 lbs." },
  ],
  [
    { text = "Madu (leather)" },
    { text = "40 gp" },
    { text = "+1" },
    { text = "—" },
    { text = "–2" },
    { text = "5%" },
    { text = "—" },
    { text = "—" },
    { text = "5 lbs." },
  ],
  [
    { text = "Madu (steel)" },
    { text = "50 gp" },
    { text = "+1" },
    { text = "—" },
    { text = "–2" },
    { text = "5%" },
    { text = "—" },
    { text = "—" },
    { text = "6 lbs." },
  ],
  [
    { text = "Heavy steel" },
    { text = "20 gp" },
    { text = "+2" },
    { text = "—" },
    { text = "–2" },
    { text = "15%" },
    { text = "—" },
    { text = "—" },
    { text = "15 lbs." },
  ],
  [
    { text = "Heavy wooden" },
    { text = "7 gp" },
    { text = "+2" },
    { text = "—" },
    { text = "–2" },
    { text = "15%" },
    { text = "—" },
    { text = "—" },
    { text = "10 lbs." },
  ],
  [
    { text = "Tower" },
    { text = "30 gp" },
    { text = "+4^4^" },
    { text = "+2" },
    { text = "–10" },
    { text = "50%" },
    { text = "—" },
    { text = "—" },
    { text = "45 lbs." },
  ],
  [
    { text = "Armor spikes" },
    { text = "+50 gp" },
    { text = "—" },
    { text = "—" },
    { text = "—" },
    { text = "—" },
    { text = "—" },
    { text = "—" },
    { text = "+10 lbs." },
  ],
  [
    { text = "Locked gauntlet" },
    { text = "+8 gp" },
    { text = "—" },
    { text = "—" },
    { text = "Special" },
    { text = "N/A^5^" },
    { text = "—" },
    { text = "—" },
    { text = "+5 lbs." },
  ],
  [
    { text = "Shield spikes" },
    { text = "+10 gp" },
    { text = "—" },
    { text = "—" },
    { text = "—" },
    { text = "—" },
    { text = "—" },
    { text = "—" },
    { text = "+5 lbs." },
  ],
]
foot = [
  [
    { text = "^1^ Weight figures are for armor sized to fit Medium characters. Armor fitted for Small characters weighs half as much, and armor fitted for Large characters weighs twice as much.^2^ When running in heavy armor, you move only triple your speed, not quadruple.^3^ When running in agile half-plate, you can still move quadruple your speed, instead of the normal triple speed for heavy armor. ^4^ A tower shield can instead grant you cover. See the description.^5^ Hand not free to cast spells.", colspan = 9 },
  ],
]
:::

::: entry-link
target = "ref/eq-armor/agile-breastplate"
title = "Agile Breastplate"
:::

::: entry-link
target = "ref/eq-armor/agile-half-plate"
title = "Agile Half-Plate"
:::

::: entry-link
target = "ref/eq-armorenh/armor-spikes"
title = "Armor Spikes"
:::

::: entry-link
target = "ref/eq-armor/armored-coat"
title = "Armored Coat"
:::

::: entry-link
target = "ref/eq-armor/banded-mail"
title = "Banded Mail"
:::

::: entry-link
target = "ref/eq-armor/breastplate"
title = "Breastplate"
:::

::: entry-link
target = "ref/eq-armor/buckler"
title = "Buckler"
:::

::: entry-link
target = "ref/eq-armor/chain-shirt"
title = "Chain Shirt"
:::

::: entry-link
target = "ref/eq-armor/chainmail"
title = "Chainmail"
:::

::: entry-link
target = "ref/eq-armor/do-maru"
title = "Do-Maru"
:::

::: entry-link
target = "ref/eq-armor/four-mirror"
title = "Four-Mirror"
:::

::: entry-link
target = "ref/eq-armor/full-plate"
title = "Full Plate"
:::

::: entry-link
target = "ref/eq-armor/half-plate"
title = "Half-Plate"
:::

::: entry-link
target = "ref/eq-armor/haramaki"
title = "Haramaki"
:::

::: entry-link
target = "ref/eq-armor/heavy-steel-shield"
title = "Heavy Steel Shield"
:::

::: entry-link
target = "ref/eq-armor/heavy-wooden-shield"
title = "Heavy Wooden Shield"
:::

::: entry-link
target = "ref/eq-armor/hide"
title = "Hide"
:::

::: entry-link
target = "ref/eq-armor/kikko"
title = "Kikko"
:::

::: entry-link
target = "ref/eq-armor/klar"
title = "Klar"
:::

::: entry-link
target = "ref/eq-armor/kusari-gusoku"
title = "Kusari Gusoku"
:::

::: entry-link
target = "ref/carried/ultimate-equipment/rules/arms-and-armor/armor/armor-and-shields/lamellar"
title = "Lamellar"
:::

::: entry-link
target = "ref/eq-armor/lamellar-cuirass"
title = "Lamellar Cuirass"
:::

::: entry-link
target = "ref/eq-armor/leather"
title = "Leather"
:::

::: entry-link
target = "ref/eq-armor/light-steel-quickdraw-shield"
title = "Light Steel Quickdraw Shield"
:::

::: entry-link
target = "ref/eq-armor/light-steel-shield"
title = "Light Steel Shield"
:::

::: entry-link
target = "ref/eq-armor/light-wooden-quickdraw-shield"
title = "Light Wooden Quickdraw Shield"
:::

::: entry-link
target = "ref/eq-armor/light-wooden-shield"
title = "Light Wooden Shield"
:::

::: entry-link
target = "ref/eq-armorenh/locked-gauntlet"
title = "Locked Gauntlet"
:::

::: entry-link
target = "ref/carried/ultimate-equipment/rules/arms-and-armor/armor/armor-and-shields/madu"
title = "Madu"
:::

::: entry-link
target = "ref/eq-armor/mountain-pattern"
title = "Mountain Pattern"
:::

::: entry-link
target = "ref/eq-armor/o-yoroi"
title = "O-Yoroi"
:::

::: entry-link
target = "ref/eq-armor/padded"
title = "Padded"
:::

::: entry-link
target = "ref/eq-armor/parade"
title = "Parade"
:::

::: entry-link
target = "ref/eq-armor/quilted-cloth"
title = "Quilted Cloth"
:::

::: entry-link
target = "ref/eq-armor/scale-mail"
title = "Scale Mail"
:::

::: entry-link
target = "ref/eq-armorenh/shield-spikes"
title = "Shield Spikes"
:::

::: entry-link
target = "ref/eq-armor/silken-ceremonial"
title = "Silken Ceremonial"
:::

::: entry-link
target = "ref/eq-armor/splint-mail"
title = "Splint Mail"
:::

::: entry-link
target = "ref/eq-armor/stoneplate"
title = "Stoneplate"
:::

::: entry-link
target = "ref/eq-armor/studded-leather"
title = "Studded Leather"
:::

::: entry-link
target = "ref/eq-armor/tatami-do"
title = "Tatami-Do"
:::

::: entry-link
target = "ref/eq-armor/tower-shield"
title = "Tower Shield"
:::

::: entry-link
target = "ref/eq-armor/wooden"
title = "Wooden"
:::
