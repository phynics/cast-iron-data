+++
id = "ref/carried/technology-guide/rules/equipment/armor"
kind = "rule"
title = "Armor"
source_ids = ["technology-guide"]
section = ["Rules", "Equipment"]
parent = "ref/carried/technology-guide/rules/equipment"
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Technology Guide/Rules/Equipment/Armor", path = "technology_guide/rules/equipment.json" },
]

[fields]
kind = "none"
+++

Each suit of technological armor has a full description, including a set of abbreviated statistics.
This information is organized as follows.

## Price {#price}

This is the cost in gold pieces to purchase the suit of armor if it's available for sale. As with
magic armor, a technological suit of armor can be sold by PCs for half this value.

## Weight {#weight}

The weight of the armor in pounds. Weight figures are for armor sized to fit Medium characters.
Armor fitted for Small characters weighs half as much, and armor fitted for Large characters weighs
twice as much.

## Type {#type}

This indicates if the suit is light, medium, or heavy armor.

## AC {#ac}

The protective value of the armor. This armor bonus is added to the wearer's Armor Class.

## Max Dex {#max-dex}

This number is the maximum Dexterity bonus that this type of armor allows.

## Penalty {#penalty}

This lists the armor check penalty of the suit of armor.

## Spell Failure {#spell-failure}

This indicates the armor's arcane spell failure chance.

## Speed {#speed}

This lists a character's adjusted speed while wearing the armor. Adjusted speeds for characters with
base speeds of 20 ft. and 30 ft. are included.

## Capacity {#capacity}

The armor's charge capacity is listed here. If the armor doesn't use energy, this entry is omitted.

## Usage {#usage}

This value lists the number of charges the armor consumes over time while activated. (Activating
powered armor is a standard action, and deactivating is a free action.) The charge is immediately
spent at the beginning of the duration, and any time remaining when the armor is deactivated is
lost.

## Description {#description}

This describes the armor's appearance, powers, and abilities.

## Construction {#construction}

Certain requirements must be met for a character to craft a suit of technological armor. These
requirements generally consist of having a feat and access to a manufacturing facility.

## Craft {#craft}

This is the Craft DC required to create the armor. It is also the Knowledge (engineering) DC to
correctly identify the armor.

## Cost {#cost}

This is the cost in gold pieces to create the technological item. Generally, this cost is equal to
half the price of the armor.

### Technology Guide Armor {#technology-guide-armor}

::: table
caption = "Technology Guide Armor"
head = [
  [
    { text = "Light Armor", header = true },
    { text = "Price", header = true },
    { text = "Armor/Shield Bonus", header = true },
    { text = "Max. Dex Bonus", header = true },
    { text = "Armor Check Penalty", header = true },
    { text = "Arcane Spell Failure Chance", header = true },
    { text = "Speed (30 ft.)", header = true },
    { text = "Speed (20 ft.)", header = true },
    { text = "Weight", header = true },
    { text = "Capacity", header = true },
    { text = "Usage", header = true },
  ],
]
body = [
  [
    { text = "Heavy weapon harness" },
    { text = "9,000 gp" },
    { text = "+1" },
    { text = "+6" },
    { text = "-1" },
    { text = "5%" },
    { text = "30 ft." },
    { text = "20 ft." },
    { text = "10 lbs." },
    { text = "—" },
    { text = "—" },
  ],
  [
    { text = "Scatterlight suit (brown)" },
    { text = "100 gp" },
    { text = "+1" },
    { text = "+8" },
    { text = "-1" },
    { text = "5%" },
    { text = "30 ft." },
    { text = "20 ft." },
    { text = "5 lbs." },
    { text = "24" },
    { text = "1 charge/hour" },
  ],
  [
    { text = "Chameleon suit" },
    { text = "15,000 gp" },
    { text = "+2" },
    { text = "+6" },
    { text = "0" },
    { text = "10%" },
    { text = "30 ft." },
    { text = "20 ft." },
    { text = "5 lbs." },
    { text = "50" },
    { text = "1 charge/minute" },
  ],
  [
    { text = "Scatterlight suit (black)" },
    { text = "150 gp" },
    { text = "+2\\*" },
    { text = "+8" },
    { text = "-1" },
    { text = "5%" },
    { text = "30 ft." },
    { text = "20 ft." },
    { text = "5 lbs." },
    { text = "24" },
    { text = "1 charge/hour" },
  ],
  [
    { text = "Inssuit" },
    { text = "19,250 gp" },
    { text = "+3" },
    { text = "+6" },
    { text = "0" },
    { text = "15%" },
    { text = "30 ft." },
    { text = "20 ft." },
    { text = "10 lbs." },
    { text = "—" },
    { text = "—" },
  ],
  [
    { text = "Deep diving suit" },
    { text = "26,000 gp" },
    { text = "+3" },
    { text = "+5" },
    { text = "-2" },
    { text = "30%" },
    { text = "30 ft." },
    { text = "20 ft." },
    { text = "20 lbs." },
    { text = "25" },
    { text = "1 charge/hour" },
  ],
  [
    { text = "Scatterlight suit (white)" },
    { text = "200 gp" },
    { text = "+3\\*" },
    { text = "+8" },
    { text = "-1" },
    { text = "5%" },
    { text = "30 ft." },
    { text = "20 ft." },
    { text = "5 lbs." },
    { text = "24" },
    { text = "1 charge/hour" },
  ],
  [
    { text = "Smart armor (compact form)" },
    { text = "16,500 gp" },
    { text = "+4" },
    { text = "+4" },
    { text = "-2" },
    { text = "25%" },
    { text = "30 ft." },
    { text = "20 ft." },
    { text = "20 lbs." },
    { text = "60" },
    { text = "1 charge/10 minutes" },
  ],
  [
    { text = "Scatterlight suit (gray)" },
    { text = "700 gp" },
    { text = "+4\\*" },
    { text = "+8" },
    { text = "-1" },
    { text = "5%" },
    { text = "30 ft." },
    { text = "20 ft." },
    { text = "5 lbs." },
    { text = "24" },
    { text = "1 charge/hour" },
  ],
  [
    { text = "Scatterlight suit (green)" },
    { text = "1,000 gp" },
    { text = "+5\\*" },
    { text = "+8" },
    { text = "-1" },
    { text = "5%" },
    { text = "30 ft." },
    { text = "20 ft." },
    { text = "5 lbs." },
    { text = "24" },
    { text = "1 charge/hour" },
  ],
  [
    { text = "Scatterlight suit (red)" },
    { text = "1,400 gp" },
    { text = "+6\\*" },
    { text = "+8" },
    { text = "-1" },
    { text = "5%" },
    { text = "30 ft." },
    { text = "20 ft." },
    { text = "5 lbs." },
    { text = "24" },
    { text = "1 charge/hour" },
  ],
  [
    { text = "Scatterlight suit (blue)" },
    { text = "3,600 gp" },
    { text = "+7\\*" },
    { text = "+8" },
    { text = "-1" },
    { text = "5%" },
    { text = "30 ft." },
    { text = "20 ft." },
    { text = "5 lbs." },
    { text = "24" },
    { text = "1 charge/hour" },
  ],
  [
    { text = "Scatterlight suit (orange)" },
    { text = "6,000 gp" },
    { text = "+8\\*" },
    { text = "+8" },
    { text = "-1" },
    { text = "5%" },
    { text = "30 ft." },
    { text = "20 ft." },
    { text = "5 lbs." },
    { text = "24" },
    { text = "1 charge/hour" },
  ],
  [
    { text = "Scatterlight suit (prismatic)" },
    { text = "12,000 gp" },
    { text = "+9\\*" },
    { text = "+8" },
    { text = "-1" },
    { text = "5%" },
    { text = "30 ft." },
    { text = "20 ft." },
    { text = "5 lbs." },
    { text = "24" },
    { text = "1 charge/hour" },
  ],
  [
    { text = "Gravity suit" },
    { text = "40,000 gp" },
    { text = "Varies" },
    { text = "+8" },
    { text = "0" },
    { text = "5%" },
    { text = "30 ft." },
    { text = "20 ft." },
    { text = "5 lbs." },
    { text = "24" },
    { text = "1 charge/hour" },
  ],
  [
    { text = "Medium Armor", header = true, colspan = 11 },
  ],
  [
    { text = "Panic suit" },
    { text = "2,000 gp" },
    { text = "+2" },
    { text = "+2" },
    { text = "-4" },
    { text = "50%" },
    { text = "20 ft." },
    { text = "15 ft." },
    { text = "2 lbs." },
    { text = "10" },
    { text = "1 charge/hour, disposable" },
  ],
  [
    { text = "HEV suit" },
    { text = "61,000 gp" },
    { text = "+4" },
    { text = "+3" },
    { text = "-4" },
    { text = "40%" },
    { text = "20 ft." },
    { text = "15 ft." },
    { text = "20 lbs." },
    { text = "25" },
    { text = "1 charge/hour" },
  ],
  [
    { text = "Nanite ablative armor" },
    { text = "10,000 gp" },
    { text = "+4" },
    { text = "+4" },
    { text = "-3" },
    { text = "20%" },
    { text = "20 ft." },
    { text = "15 ft." },
    { text = "35 lbs." },
    { text = "24" },
    { text = "1 charge/hour" },
  ],
  [
    { text = "Heavy Armor", header = true, colspan = 11 },
  ],
  [
    { text = "Spacesuit" },
    { text = "90,000 gp" },
    { text = "+7" },
    { text = "+0" },
    { text = "-8" },
    { text = "50%" },
    { text = "20 ft." },
    { text = "15 ft." },
    { text = "35 lbs." },
    { text = "25" },
    { text = "1 charge/hour" },
  ],
  [
    { text = "Smart armor (expanded form)" },
    { text = "16,500 gp" },
    { text = "+8" },
    { text = "+1" },
    { text = "-5" },
    { text = "35%" },
    { text = "20 ft." },
    { text = "15 ft." },
    { text = "20 lbs." },
    { text = "60" },
    { text = "1 charge/10 minutes" },
  ],
  [
    { text = "Shields", header = true, colspan = 11 },
  ],
  [
    { text = "Hard light shield" },
    { text = "6,400 gp" },
    { text = "+2" },
    { text = "—" },
    { text = "0" },
    { text = "10%" },
    { text = "—" },
    { text = "—" },
    { text = "1 lb." },
    { text = "20" },
    { text = "1 charge/minute" },
  ],
]
foot = [
  [
    { text = "\\* The full bonus applies only to touch AC. See item for details.", colspan = 11 },
  ],
]
:::

::: entry-link
target = "ref/tech-armor/chameleon-suit"
title = "Chameleon Suit"
:::

::: entry-link
target = "ref/tech-armor/deep-diving-suit"
title = "Deep Diving Suit"
:::

::: entry-link
target = "ref/tech-armor/gravity-suit"
title = "Gravity Suit"
:::

::: entry-link
target = "ref/tech-armor/hard-light-shield"
title = "Hard Light Shield"
:::

::: entry-link
target = "ref/tech-armor/heavy-weapon-harness"
title = "Heavy Weapon Harness"
:::

::: entry-link
target = "ref/tech-armor/hev-suit"
title = "HEV Suit"
:::

::: entry-link
target = "ref/tech-armor/inssuit"
title = "Inssuit"
:::

::: entry-link
target = "ref/tech-armor/nanite-ablative-armor"
title = "Nanite Ablative Armor"
:::

::: entry-link
target = "ref/tech-armor/panic-suit"
title = "Panic Suit"
:::

::: entry-link
target = "ref/carried/technology-guide/rules/equipment/armor/scatterlight-suit"
title = "Scatterlight Suit"
:::

::: entry-link
target = "ref/tech-armor/smart-armor-compact-form"
title = "Smart Armor (Compact Form)"
:::

::: entry-link
target = "ref/tech-armor/smart-armor-expanded-form"
title = "Smart Armor (Expanded Form)"
:::

::: entry-link
target = "ref/tech-armor/spacesuit"
title = "Spacesuit"
:::
