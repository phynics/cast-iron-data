+++
id = "ref/spell/create-undead"
kind = "spell"
title = "Create Undead"
aon = "SpellDisplay.aspx?ItemName=Create%20Undead"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "create_undead", path = "json/spells3.json" },
]
[[sources]]
publication = "core-rulebook"
page = "262"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Shaman", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Spiritualist", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 hour"
components = "V, S, M (a clay pot filled with grave dirt and an onyx gem worth at least 50 gp per HD of the undead to be created)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one corpse" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 6: Arcanist, Cleric, Oracle, Shaman, Sorcerer, Spiritualist, Warpriest, Wizard
Casting time: 1 hour
Components: V, S, M (a clay pot filled with grave dirt and an onyx gem worth at least 50 gp per HD of the undead to be created)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: one corpse
Descriptors: evil
:::

A much more potent spell than [animate dead](ref/spell/animate-dead), this evil spell allows you to
infuse a dead body with negative energy to create more powerful sorts of undead: ghouls, ghasts,
mummies, and mohrgs. The type or types of undead you can create are based on your caster level, as
shown on the table below.

|Caster Level|Undead Created|
| --- | --- |
|11th or lower|Ghoul|
|12th-14th|Ghast|
|15th-17th|Mummy|
|18th or higher|Mohrg|

You may create less powerful undead than your level would allow if you choose. Created undead are
not automatically under the control of their animator. If you are capable of commanding undead, you
may attempt to command the undead creature as it forms.

This spell must be cast at night.

Other publications have added more creatures that can be created by this spell. They include:

- [Bone Priest](ref/monster/bone-priest)
- [Blast Shadow](ref/monster/blast-shadow)
- [Centianima](ref/monster/centianima)
- [Crypt Thing](ref/monster/crypt-thing)
- [Huecuva](ref/monster/huecuva)
- [Lesser Hollow Serpent](ref/monster/hollow-serpent-lesser-hollow-serpent)
- [Phantom Armor](ref/family/phantom-armor)
- [Spartolos](ref/monster/spartolos)
- [Tikoloshe](ref/monster/tikoloshe)
- [Wraithwing](ref/monster/wraithwing)
