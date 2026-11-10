+++
id = "ref/spell/blood-song"
kind = "spell"
title = "Blood Song"
aon = "SpellDisplay.aspx?ItemName=Blood%20Song"
source_ids = ["faiths-and-philosophies"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blood_song", path = "json/spells2.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/imbue-with-spell-ability" },
]
[[sources]]
publication = "faiths-and-philosophies"
page = "28"

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Bard", level = 4 },
  { class = "Skald", level = 4 },
]
casting_time = "2 minutes"
components = "V, S, M (the caster's blood)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched; see text" },
]
duration = "1 day or until discharged (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Bard, Skald
Casting time: 2 minutes
Components: V, S, M (the caster's blood)
Range: touch
Duration: 1 day or until discharged (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched; see text
:::

This spell functions as [imbue with spell ability](ref/spell/imbue-with-spell-ability), with the
following exceptions: only bard spells of the conjuration (healing), enchantment, and transmutation
schools can be transferred; the imbued spells last for 1 day; and the subject isn't beholden to any
principles regarding the imbued spells' use.

As part of the casting, the caster must shed some of his blood (or an equivalent humor). If the
caster isn't susceptible to bleed damage, regardless of the reason, he can't cast blood song. For
each spell that is imbued using blood song, the caster loses 5 hit points, which can't be regained
by any means until the spell ends or is discharged.
