+++
id = "ref/arc-witch/ley-line-guardian"
kind = "archetype"
title = "Ley Line Guardian"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Ley%20Line%20Guardian"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ley_line_guardian", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "occult-adventures"
page = "125"

[fields]
kind = "archetype"
features = [
  { anchor = "ley-line-powered" },
  { anchor = "conduit-surge", level = 1 },
]
trades = [
  { replaces = "Familiar", feature = "witch-s-familiar", by = ["conduit-surge"] },
  { replaces = "Hexes gained at 1st and 8th levels", feature = "hex", levels = [1, 8], by = ["conduit-surge"] },
  { alters = "Spellcasting", feature = "spells", by = ["ley-line-powered"] },
]
+++

Some witches tap into the power of their patrons not through a special connection with a familiar,
but rather directly through the vast network of ley lines that crosses the planes. These witches can
harness the latent powers of ley lines without even needing to be near one of the points where ley
lines' powers are accessible to mortal spellcasters.

## Ley Line Powered {#ley-line-powered}

Instead of preparing her spells, a ley line guardian draws the power casting spells directly from
ley lines. A ley line guardian is a spontaneous spellcaster. She knows the same number of spells and
receives the same number of spell slots per day as a [sorcerer](ref/class/sorcerer) of her witch
level. Bonus spells granted by a ley line guardian's patron are added to the ley line guardian's
total spells known at the appropriate levels. This ability alters the witch's spellcasting.

## Conduit Surge (Su) {#conduit-surge}

At 1st level, a ley line guardian is adept at channeling energy from ley lines to enhance her own
spells. As a swift action, she can increase her effective caster level for the next spell she casts
in that round by 1d4–1 levels. After performing a conduit surge, the ley line guardian must succeed
at a Fortitude save (DC = 10 + level of spell cast + number of additional caster levels granted) or
become [staggered](ref/misc/staggered) for a number of minutes equal to the level of the spell cast.
At 8th level, the caster level increase becomes 1d4. She can use this ability a number of times per
day equal to 3 + her Charisma modifier.

This ability replaces familiar and the hexes gained at 1st and 8th levels.
