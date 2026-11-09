+++
id = "ref/spell/sessile-spirit"
kind = "spell"
title = "Sessile Spirit"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sessile_spirit", path = "json/spells15.json" },
]
[[sources]]
publication = "occult-adventures"
page = "185"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 4 },
  { class = "Medium", level = 2 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 5 },
  { class = "Shaman", level = 4 },
  { class = "Spiritualist", level = 3 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature or object (see text)" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Medium\
3: Occultist, Spiritualist\
4: Inquisitor, Shaman\
5: Cleric, Oracle, Warpriest, Witch
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes
Target: one creature or object (see text)
:::

You reach into the target creature and cause that spirits within to become dormant and inactive. If
the target is a medium with a spirit inhabiting its body or a spiritualist with a phantom inhabiting
its consciousness (or a member of another class using the spirit or phantom class features), a
failed save renders that spirit or phantom powerless, suppressing any benefits the spirit or phantom
normally provides to its host, including bonus feats and spells known.

If a spirit within the target is a creature using a possession effect, including possess object,
possession, or a ghost's malevolence, the spell targets the possessing creature rather than the
creature it inhabits. On a failed save, the possessing spirit isn't exorcised from the target but is
dazed for the duration of the spell.
