+++
id = "ref/carried/ultimate-equipment/rules/wondrous-items/slotless/slotless-wondrous-items/bag-of-tricks"
kind = "item"
title = "Bag of Tricks"
source_ids = ["ultimate-equipment"]
section = ["Rules", "Wondrous Items", "Slotless", "Slotless Wondrous Items"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Equipment/Rules/Wondrous Items/Slotless/Slotless Wondrous Items/Bag of Tricks", path = "ultimate_equipment/item/bag_of_tricks.json" },
]

[fields]
kind = "item"
category = "Wondrous Items"
price = "Varies"
weight = "1 lb."
aura = "faint conjuration"
caster_level = "3rd"
attributes = [
  { label = "Construction Requirements: Gray", value = "1,700 gp" },
  { label = "Construction Requirements: Tan", value = "8,000 gp" },
  { label = "Construction Requirements: Rust", value = "4,250 gp" },
  { label = "Bag of Tricks: Gray", value = "3,400 gp" },
  { label = "Bag of Tricks: Tan", value = "16,000 gp" },
  { label = "Bag of Tricks: Rust", value = "8,500 gp" },
]
+++

::: statblock
Aura: faint conjuration
CL: 3rd
Price: Varies
Weight: 1 lb.
Construction Requirements\: Gray: 1,700 gp
Construction Requirements\: Tan: 8,000 gp
Construction Requirements\: Rust: 4,250 gp
Bag of Tricks\: Gray: 3,400 gp
Bag of Tricks\: Tan: 16,000 gp
Bag of Tricks\: Rust: 8,500 gp
:::

::: paragraph statline
This small sack looks empty at first glance. Anyone reaching into the bag feels a small, fuzzy ball
inside. If the ball is removed and tossed up to 20 feet away, it turns into an animal. The animal
serves the character who drew it from the bag for 10 minutes (or until slain or ordered back into
the bag), at which point it disappears. It can follow any of the commands described in the Handle
Animal skill. Each of the three kinds of bags of tricks produces a different set of animals. Use the
following tables to determine what animals can be drawn out of each.
:::

## Gray Bag {#gray-bag}

::: table
head = [
  [
    { text = "Gray Bagd% Animal", header = true, colspan = 2 },
    { text = "Rust Bagd% Animal", header = true, colspan = 2 },
    { text = "Tan Bagd% Animal", header = true, colspan = 2 },
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
    { text = "", colspan = 2 },
    { text = "91–100" },
    { text = "Rhinoceros" },
  ],
]
:::

::: paragraph statline
The heavy horse and the riding dog appear with harness and tack, and each accepts the character who
drew it from the bag as a rider.
:::

::: paragraph statline
Animals produced are always random, and only one may exist at a time. Up to 10 animals can be drawn
from the bag each week, but no more than two per day.
:::
