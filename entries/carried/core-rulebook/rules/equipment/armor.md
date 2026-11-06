+++
id = "ref/carried/core-rulebook/rules/equipment/armor"
kind = "rule"
title = "Armor"
source_ids = ["core-rulebook"]
section = ["Rules", "Equipment"]
parent = "ref/rule/equipment"
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Rules/Equipment/Armor", path = "core_rulebook/rules/equipment.json" },
]

[fields]
kind = "none"
+++

For most, armor is the simplest way to protect oneself in a world of rampant threats and dangers.
Many characters can wear only the simplest of armors, and only some can use shields. To wear heavier
armor effectively, a character can select the Armor Proficiency feats, but most classes are
automatically proficient with the armors that work best for them.

Here is the format for armor entries (given as column headings on Table: Armor and Shields).

## Cost {#cost}

The cost in gold pieces of the armor for Small or Medium humanoid creatures. See Table: Armor for
Unusual Creatures for armor prices for other creatures.

## Armor/Shield Bonus {#armor-shield-bonus}

Each type of armor grants an armor bonus to AC, while shields grant a shield bonus to AC. The armor
bonus from a suit of armor doesn't stack with other effects or items that grant an armor bonus.
Similarly, the shield bonus from a shield doesn't stack with other effects that grant a shield
bonus.

## Maximum Dex Bonus {#maximum-dex-bonus}

This number is the maximum Dexterity bonus to AC that this type of armor allows. Dexterity bonuses
in excess of this number are reduced to this number for the purposes of determining the wearer's AC.
Heavier armors limit mobility, reducing the wearer's ability to dodge blows. This restriction
doesn't affect any other Dexterity-related abilities.

Even if a character's Dexterity bonus to AC drops to 0 because of armor, this situation does not
count as losing his Dexterity bonus to AC.

A character's encumbrance (the amount of gear carried, including armor) may also restrict the
maximum Dexterity bonus that can be applied to his Armor Class.

### Shields {#shields}

Shields do not affect a character's maximum Dexterity bonus, except for tower shields.

## Armor Check Penalty {#armor-check-penalty}

Any armor heavier than leather, as well as any shield, hurts a character's ability to use Dexterity-
and Strength-based skills. An armor check penalty applies to all Dexterity- and Strength-based skill
checks. A character's encumbrance may also incur an armor check penalty.

### Shields {#shields-2}

If a character is wearing armor and using a shield, both armor check penalties apply.

### Nonproficient with Armor Worn {#nonproficient-with-armor-worn}

A character who wears armor and/or uses a shield with which he is not proficient takes the armor's
(and/or shield's) armor check penalty on attack rolls as well as on all Dexterity- and
Strength-based ability and skill checks. The penalty for nonproficiency with armor stacks with the
penalty for shields.

### Sleeping in Armor {#sleeping-in-armor}

A character who sleeps in medium or heavy armor is automatically fatigued the next day. He takes a
–2 penalty on Strength and Dexterity and can't charge or run. Sleeping in light armor does not cause
fatigue.

## Arcane Spell Failure Chance {#arcane-spell-failure-chance}

Armor interferes with the gestures that a spellcaster must make to cast an arcane spell that has a
somatic component. Arcane spellcasters face the possibility of arcane spell failure if they're
wearing armor. Bards can wear light armor and use shields without incurring any arcane spell failure
chance for their bard spells.

### Casting an Arcane Spell in Armor {#casting-an-arcane-spell-in-armor}

A character who casts an arcane spell while wearing armor must usually make an arcane spell failure
check. The number in the Arcane Spell Failure Chance column on Table: Armor and Shields is the
percentage chance that the spell fails and is ruined. If the spell lacks a somatic component,
however, it can be cast with no chance of arcane spell failure.

### Shields {#shields-3}

If a character is wearing armor and using a shield, add the two numbers together to get a single
arcane spell failure chance.

## Speed {#speed}

Medium or heavy armor slows the wearer down. The number on Table: Armor and Shields is the
character's speed while wearing the armor. Humans, elves, half-elves, and half-orcs have an
unencumbered speed of 30 feet. They use the first column. Dwarves, gnomes, and halflings have an
unencumbered speed of 20 feet. They use the second column. Remember, however, that a dwarf's land
speed remains 20 feet even in medium or heavy armor or when carrying a medium or heavy load.

### Shields {#shields-4}

Shields do not affect a character's speed.

## Weight {#weight}

This column gives the weight of the armor sized for a Medium wearer. Armor fitted for Small
characters weighs half as much, and armor for Large characters weighs twice as much.

## Armor Descriptions {#armor-descriptions}

### Table: Armor and Shields {#table-armor-and-shields}

::: table
caption = "Table: Armor and Shields"
head = [
  [
    { text = "Armor", header = true, rowspan = 2 },
    { text = "Cost", header = true, rowspan = 2 },
    { text = "Armor/Shield Bonus", header = true, rowspan = 2 },
    { text = "Maximum Dex Bonus", header = true, rowspan = 2 },
    { text = "Armor Check Penalty", header = true, rowspan = 2 },
    { text = "Arcane Spell Failure Chance", header = true, rowspan = 2 },
    { text = "Speed", header = true, colspan = 2 },
    { text = "Weight^1^", header = true, rowspan = 2 },
  ],
  [
    { text = "30 ft.", header = true },
    { text = "20 ft.", header = true },
  ],
]
body = [
  [
    { text = "_Light armor_", colspan = 9 },
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
    { text = "Studded leather" },
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
    { text = "_Medium armor_", colspan = 9 },
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
    { text = "_Heavy armor_", colspan = 9 },
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
    { text = "_Shields_", colspan = 9 },
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
    { text = "Shield, light wooden" },
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
    { text = "Shield, light steel" },
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
    { text = "Shield, heavy wooden" },
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
    { text = "Shield, heavy steel" },
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
    { text = "Shield, tower" },
    { text = "30 gp" },
    { text = "+4^3^" },
    { text = "+2" },
    { text = "–10" },
    { text = "50%" },
    { text = "—" },
    { text = "—" },
    { text = "45 lbs." },
  ],
  [
    { text = "_Extras_", colspan = 9 },
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
    { text = "Gauntlet, locked" },
    { text = "8 gp" },
    { text = "—" },
    { text = "—" },
    { text = "special" },
    { text = "n/a^4^" },
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
    { text = "1 Weight figures are for armor sized to fit Medium characters. Armor fitted for Small characters weighs half as much, and armor fitted for Large characters weighs twice as much.", colspan = 9 },
  ],
  [
    { text = "2 When running in heavy armor, you move only triple your speed, not quadruple.", colspan = 9 },
  ],
  [
    { text = "3 A tower shield can instead grant you cover. See the description.", colspan = 9 },
  ],
  [
    { text = "4 Hand not free to cast spells.", colspan = 9 },
  ],
]
:::

Any special benefits or accessories to the types of armor found on Table: Armor and Shields are
described below.

::: entry-link
target = "ref/eq-armorenh/armor-spikes"
title = "Armor Spikes"
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
target = "ref/eq-armor/full-plate"
title = "Full Plate"
:::

::: entry-link
target = "ref/eq-armorenh/locked-gauntlet"
title = "Gauntlet, Locked"
:::

::: entry-link
target = "ref/eq-armor/half-plate"
title = "Half-Plate"
:::

::: entry-link
target = "ref/eq-armor/hide"
title = "Hide"
:::

::: entry-link
target = "ref/eq-armor/leather"
title = "Leather"
:::

::: entry-link
target = "ref/eq-armor/padded"
title = "Padded"
:::

::: entry-link
target = "ref/eq-armor/scale-mail"
title = "Scale Mail"
:::

::: entry-link
target = "ref/eq-armor/heavy-wooden-shield"
title = "Shield, Heavy; Wooden"
:::

::: entry-link
target = "ref/eq-armor/heavy-steel-shield"
title = "Shield, Heavy; Steel"
:::

::: entry-link
target = "ref/eq-armor/light-wooden-shield"
title = "Shield, Light; Wooden"
:::

::: entry-link
target = "ref/eq-armor/light-steel-shield"
title = "Shield, Light; Steel"
:::

::: entry-link
target = "ref/eq-armor/tower-shield"
title = "Shield, Tower"
:::

::: entry-link
target = "ref/eq-armorenh/shield-spikes"
title = "Shield Spikes"
:::

::: entry-link
target = "ref/eq-armor/splint-mail"
title = "Splint Mail"
:::

::: entry-link
target = "ref/eq-armor/studded-leather"
title = "Studded Leather"
:::

## Masterwork Armor {#masterwork-armor}

Just as with weapons, you can purchase or craft masterwork versions of armor or shields. Such a
well-made item functions like the normal version, except that its armor check penalty is lessened
by 1.

A masterwork suit of armor or shield costs an extra 150 gp over and above the normal cost for that
type of armor or shield.

The masterwork quality of a suit of armor or shield never provides a bonus on attack or damage
rolls, even if the armor or shield is used as a weapon.

All magic armors and shields are automatically considered to be of masterwork quality.

You can't add the masterwork quality to armor or a shield after it is created; it must be crafted as
a masterwork item.

## Armor for Unusual Creatures {#armor-for-unusual-creatures}

Armor and shields for unusually big creatures, unusually little creatures, and nonhumanoid creatures
(such as horses) have different costs and weights from those given on Table: Armor and Shields.
Refer to the appropriate line on Table: Armor for Unusual Creatures and apply the multipliers to
cost and weight for the armor type in question.

### Table: Armor for Unusual Creatures {#table-armor-for-unusual-creatures}

::: table
caption = "Table: Armor for Unusual Creatures"
head = [
  [
    { text = "Size", header = true, rowspan = 2 },
    { text = "Humanoid", header = true, colspan = 2 },
    { text = "Nonhumanoid", header = true, colspan = 2 },
  ],
  [
    { text = "Cost", header = true },
    { text = "Weight", header = true },
    { text = "Cost", header = true },
    { text = "Weight", header = true },
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

The time required to don armor depends on its type; see Table: Donning Armor.

### Don {#don}

This column tells how long it takes a character to put the armor on. (One minute is 10 rounds.)
Readying (strapping on) a shield is only a move action.

### Don Hastily {#don-hastily}

This column tells how long it takes to put the armor on in a hurry. The armor check penalty and
armor bonus for hastily donned armor are each 1 point worse than normal.

### Remove {#remove}

This column tells how long it takes to get the armor off. Removing a shield from the arm and
dropping it is only a move action.

#### Table: Donning Armor {#table-donning-armor}

::: table
caption = "Table: Donning Armor"
head = [
  [
    { text = "Armor Type", header = true },
    { text = "Don", header = true },
    { text = "Don Hastily", header = true },
    { text = "Remove", header = true },
  ],
]
body = [
  [
    { text = "Shield (any)" },
    { text = "1 move action" },
    { text = "n/a" },
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
    { text = "1 If the character has some help, cut this time in half. A single character doing nothing else can help one or two adjacent characters. Two characters can't help each other don armor at the same time.", colspan = 4 },
  ],
  [
    { text = "2 The wearer must have help to don this armor. Without help, it can be donned only hastily.", colspan = 4 },
  ],
]
:::
