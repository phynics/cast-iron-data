+++
id = "ref/spell/steal-book"
kind = "spell"
title = "Steal Book"
source_ids = ["pathfinder-society-s03-10-the-immortal-connundrum"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "steal_book", path = "json/spells9.json" },
]
[[sources]]
publication = "pathfinder-society-s03-10-the-immortal-connundrum"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Bard", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one book touched" },
]
duration = "permanent"
saving_throw = "Fortitude negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Bard, Inquisitor, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: permanent
Saving throw: Fortitude negates (object)
Spell resistance: yes (object)
Target: one book touched
:::

This spell allows you to copy the contents of one book, folio, scroll, or other text to a blank one
of suffient size. In doing so, the original pages are wiped blank, though any covers or bindings
remain unchanged. Differences in size between the original and blank folio don't matter, though the
blank folio must have an equal or greater amount of space (in number of pages or inches of scroll),
or else any text that overflows the document is lost forever.

This spell cannot transfer magical writing (such as a wizard's spellbook or a magical scroll).

Optionally, if the GM allows it, the spell can restore lost information, such as a page obscured by
spilled wine, text erased by magical or mundane means, or even pages lost to fire or another type of
damage.
