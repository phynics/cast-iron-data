+++
id = "ref/carried/core-rulebook/rules/magic-items/wondrous-items/bag-of-tricks"
kind = "item"
title = "Bag of Tricks"
source_ids = ["core-rulebook"]
section = ["Rules", "Magic Items", "Wondrous Items"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Rules/Magic Items/Wondrous Items/Bag of Tricks", path = "core_rulebook/item/bag_of_tricks.json" },
]

[fields]
kind = "item"
category = "Wondrous Items"
price = "3,400 gp (gray); 8,500 gp (rust); 16,000 gp (tan)"
slot = "none"
aura = "faint (gray or rust) or moderate (tan) conjuration"
caster_level = "3rd (gray), 5th (rust), 9th (tan)"
attributes = [
  { label = "Construction: Cost", value = "1,700 gp (gray); 4,250 gp (rust); 8,000 gp (tan)" },
  { label = "Construction: Requirements", value = "Craft Wondrous Item, summon nature's ally II (gray), summon nature's ally III (rust), or summon nature's ally V (tan)" },
]
+++

::: statblock
Slot: none
Aura: faint (gray or rust) or moderate (tan) conjuration
CL: 3rd (gray), 5th (rust), 9th (tan)
Price: 3,400 gp (gray); 8,500 gp (rust); 16,000 gp (tan)
Construction\: Cost: 1,700 gp (gray); 4,250 gp (rust); 8,000 gp (tan)
Construction\: Requirements: Craft Wondrous Item, summon nature's ally II (gray), summon nature's ally III (rust), or summon nature's ally V (tan)
:::

## Description {#description}

This small sack appears empty. Anyone reaching into the bag feels a small, fuzzy ball. If the ball
is removed and tossed up to 20 feet away, it turns into an animal. The animal serves the character
who drew it from the bag for 10 minutes (or until slain or ordered back into the bag), at which
point it disappears. It can follow any of the commands described in the Handle Animal skill. Each of
the three kinds of _bags of tricks _produces a different set of animals. Use the following tables to
determine what animals can be drawn out of each.

### Gray Bag {#gray-bag}

::: table
head = [
  [
    { text = "Gray Bag", header = true, colspan = 2 },
    { text = "Rust Bag", header = true, colspan = 2 },
    { text = "Tan Bag", header = true, colspan = 2 },
  ],
  [
    { text = "d%", header = true },
    { text = "Animal", header = true },
    { text = "d%", header = true },
    { text = "Animal", header = true },
    { text = "d%", header = true },
    { text = "Animal", header = true },
  ],
]
body = [
  [
    { text = "01–30" },
    { text = "Bat" },
    { text = "01–30" },
    { text = "Wolverine" },
    { text = "01–30" },
    { text = "Grizzly bear" },
  ],
  [
    { text = "31–60" },
    { text = "Rat" },
    { text = "31–60" },
    { text = "Wolf" },
    { text = "31–60" },
    { text = "Lion" },
  ],
  [
    { text = "61–75" },
    { text = "Cat" },
    { text = "61–85" },
    { text = "Boar" },
    { text = "61–80" },
    { text = "Heavy horse" },
  ],
  [
    { text = "76–90" },
    { text = "Weasel" },
    { text = "86–100" },
    { text = "Leopard" },
    { text = "81–90" },
    { text = "Tiger" },
  ],
  [
    { text = "91–100" },
    { text = "Riding dog" },
    { text = "—", colspan = 2 },
    { text = "91–100" },
    { text = "Rhinoceros" },
  ],
]
:::

The heavy horse appears with harness and tack and accepts the character who drew it from the bag as
a rider.

Animals produced are always random, and only one may exist at a time. Up to 10 animals can be drawn
from the bag each week, but no more than two per day.
