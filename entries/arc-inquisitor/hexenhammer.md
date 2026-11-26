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
features = [
  { anchor = "withering-gaze", level = 1 },
  { anchor = "pride-and-penance", level = 1 },
  { anchor = "cunning-mind", level = 2 },
  { anchor = "hexcrafter", level = 3 },
  { anchor = "dark-trade", level = 3 },
  { anchor = "witchcraft", level = 5 },
]
trades = [
  { replaces = "Monster lore", feature = "monster-lore", by = ["withering-gaze"] },
  { replaces = "stern gaze", feature = "stern-gaze", by = ["withering-gaze"] },
  { replaces = "Cunning initiative", feature = "cunning-initiative", by = ["cunning-mind"] },
  { replaces = "Teamwork feats", feature = "teamwork-feat", by = ["hexcrafter"] },
  { replaces = "Solo tactics", feature = "solo-tactics", by = ["dark-trade"] },
  { alters = "Domain", feature = "domain", by = ["pride-and-penance"] },
  { alters = "Spellcasting", feature = "spells", by = ["witchcraft"] },
]
+++

Some inquisitors embrace the dark powers of their traditional foes, turning such powers toward their
own ends in order to pronounce judgment on those who oppose them. These inquisitors learn to use the
hexes and some spells of witches, but must pay the price for dealing with supernatural powers, as
they slip ever closer to the evil they seek to destroy.

## Withering Gaze (Su) {#withering-gaze}

Hexenhammers study the effects of a witch's [evil eye](ref/hex/evil-eye), and can use this dark
magic to steel their gaze in a similar manner. Beginning at 1st level, whenever a hexenhammer
successfully demoralizes a creature as a standard action, instead of applying the
[shaken](ref/misc/shaken) condition, she can apply the effects of the witch evil eye hex as if she
were a 1st-level witch (save DC = 10 + 1/2 the hexenhammer's inquisitor level + her Wisdom
modifier).

This ability replaces monster lore and stern gaze.

## Pride and Penance (Ex) {#pride-and-penance}

Hexenhammers are deeply conflicted about their dealings with dark powers. If a hexenhammer uses a
hex or casts a spell gained from the witch class spell list, she temporarily loses access to her
domain abilities and her cunning mind bonus until she undergoes a brief period of penance and
atonement that takes 1 minute of quiet prayer and contemplation; this atonement doesn't require any
additional cost, and it automatically restores the lost abilities, regardless of how many times the
hexenhammer uses her dark powers.

If the hexenhammer uses her dark trade ability (see below) to trade uses of judgment for hexes, she
loses access to her domain abilities and cunning mind bonus until the next time she regains her
spell slots for the day.

This ability alters domain.

## Cunning Mind (Ex) {#cunning-mind}

At 2nd level, a hexenhammer gains a +2 bonus on saving throws against hexes, curses, spells of the
necromancy school, and spells with the evil descriptor.

This ability replaces cunning initiative.

## Hexcrafter (Su) {#hexcrafter}

Beginning at 3rd level, a hexenhammer learns to turn some powers of witches to her own advantage.
She learns either the [blight](ref/hex/blight), the [misfortune](ref/hex/misfortune), or the
[slumber](ref/hex/slumber) hex from the witch's hex list, and can use that hex once per day as a
standard action, using her inquisitor level in place of a witch level. If the hex allows a saving
throw, the save DC to resist the hex is equal to 10 + 1/2 the inquisitor's level + the inquisitor's
Wisdom modifier.

At 6th level, 12th, and 15th levels, the hexenhammer learns an additional hex from her available
hexes. At 9th level and 18th level, the hexenhammer can use any one of her hexes one additional time
per day. At 12th level, the hexenhammer adds the [agony](ref/hex/agony),
[nightmares](ref/hex/nightmares), and [retribution](ref/hex/retribution) major hexes to her list of
learnable hexes.

This ability replaces teamwork feats.

## Dark Trade (Su) {#dark-trade}

At 3rd level, a hexenhammer can forgo the power of her judgments and succumb to the temptation of
darker powers. She can trade a daily use of judgment to instead gain an additional use of one of her
hexes.

This ability replaces solo tactics.

## Witchcraft (Ex) {#witchcraft}

At 5th level and at every 3 inquisitor levels thereafter, a hexenhammer can learn a witch spell in
place of a spell she already knows. In effect, she loses an old spell in exchange for a new one
selected from the witch class spell list. The new spell's level must be the same as that of the
spell being exchanged, and it must be at least 1 level lower than the highest-level inquisitor spell
she can cast. The hexenhammer can swap out only a single spell at any given level and must choose
whether or not to swap the spell at the same time she gains new spells known for the level.

This ability alters the inquisitor's spellcasting.
