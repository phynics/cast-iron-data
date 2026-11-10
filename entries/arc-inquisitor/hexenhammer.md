+++
id = "ref/arc-inquisitor/hexenhammer"
kind = "archetype"
title = "Hexenhammer"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Hexenhammer"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hexenhammer", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "horror-adventures"
page = "52"

[fields]
kind = "archetype"
replaces = ["Monster lore", "stern gaze", "Cunning initiative", "Teamwork feats", "Solo tactics"]
alters = ["Domain", "Spellcasting"]
replaces_features = ["monster-lore", "stern-gaze", "cunning-initiative", "solo-tactics"]
alters_features = ["domain"]
+++

Some inquisitors embrace the dark powers of their traditional foes, turning such powers toward their
own ends in order to pronounce judgment on those who oppose them. These inquisitors learn to use the
hexes and some spells of witches, but must pay the price for dealing with supernatural powers, as
they slip ever closer to the evil they seek to destroy.

**Withering Gaze (Su)**

**Ability:** Whenever a hexenhammer successfully demoralizes a creature as a standard action,
instead of applying the [shaken](ref/misc/shaken) condition, she can apply the effects of the witch
[evil eye](ref/hex/evil-eye) hex as if she were a 1st-level witch (save DC = 10 + 1/2 the
hexenhammer's inquisitor level + her Wisdom modifier).

**Flavor:** Hexenhammers study the effects of a witch's evil eye, and can use this dark magic to
steel their gaze in a similar manner.

**Gained:** At 1st Level

**Replaces:** Monster lore, stern gaze

**Pride and Penance (Ex)**

**Alters:** Domain

**Flavor:** Hexenhammers are deeply conflicted about their dealings with dark powers.

**Info:** If a hexenhammer uses a hex or casts a spell gained from the witch class spell list, she
temporarily loses access to her domain abilities and her _cunning mind_ bonus until she undergoes a
brief period of penance and atonement that takes 1 minute of quiet prayer and contemplation; this
atonement doesn't require any additional cost, and it automatically restores the lost abilities,
regardless of how many times the hexenhammer uses her dark powers. If the hexenhammer uses her _dark
trade_ ability (see below) to trade uses of judgment for hexes, she loses access to her domain
abilities and _cunning mind_ bonus until the next time she regains her spell slots for the day.

**Cunning Mind (Ex)**

**Gained:** At 2nd Level

**Passive:** A hexenhammer gains a +2 bonus on saving throws against hexes, curses, spells of the
necromancy school, and spells with the evil descriptor.

**Replaces:** Cunning initiative

**Hexcrafter (Su)**

**Ability:** She learns either the [blight](ref/hex/blight), the [misfortune](ref/hex/misfortune),
or the [slumber](ref/hex/slumber) hex from the witch's hex list, and can use that hex once per day
as a **standard action**, using her inquisitor level in place of a witch level. If the hex allows a
saving throw, the save DC to resist the hex is equal to 10 + 1/2 the inquisitor's level + the
inquisitor's Wisdom modifier.

**Flavor:** A hexenhammer learns to turn some powers of witches to her own advantage.

**At 12th Level:** The hexenhammer adds the [agony](ref/hex/agony),
[nightmares](ref/hex/nightmares), and [retribution](ref/hex/retribution) major hexes to that list.

**At 18th Level:** She can use any one of her hexes an additional time per day.

**At 9th Level:** The hexenhammer can use any one of her hexes one additional time per day.

**Gained:** At 3rd Level

**Replaces:** Teamwork feats

**Dark Trade (Su)**

**Ability:** She can trade a daily use of judgment to instead gain an additional use of one of her
hexes.

**Flavor:** A hexenhammer can forgo the power of her judgments and succumb to the temptation of
darker powers.

**Gained:** At 3rd Level

**Replaces:** Solo tactics

**Witchcraft (Ex)**

**Ability:** And at every 3 inquisitor levels thereafter, a hexenhammer can learn a witch spell in
place of a spell she already knows. In effect, she loses an old spell in exchange for a new one
selected from the witch class spell list. The new spell's level must be the same as that of the
spell being exchanged, and it must be at least 1 level lower than the highest-level inquisitor spell
she can cast.

**Alters:** Spellcasting

**Gained:** At 5th Level

**Special:** The hexenhammer can swap out only a single spell at any given level and must choose
whether or not to swap the spell at the same time she gains new spells known for the level.

At 8th level: She can learn a 2nd spell, as above.

At 11th level: She can learn a 3rd spell, as above.

At 14th level: She can learn a 4th spell, as above.

At 17th level: She can learn a 5th spell, as above.

At 20th level: She can learn a 6th spell, as above.
