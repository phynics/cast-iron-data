+++
id = "ref/spell/arcane-lock"
kind = "spell"
title = "Arcane Lock"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arcane_lock", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (gold dust worth 25 gp)"
range = "touch"
effects = [
  { label = "Target", value = "door, chest, or portal touched, up to 30 sq. ft./level in size" },
]
duration = "permanent"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Arcanist, Occultist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (gold dust worth 25 gp)
Range: touch
Duration: permanent
Saving throw: none
Spell resistance: no
Target: door, chest, or portal touched, up to 30 sq. ft./level in size
:::

**Sources:** PRPG Core Rulebook pg 243

An arcane lock spell cast upon a door, chest, or portal magically locks it. You can freely pass your
own arcane lock without affecting it. If the locked object has a lock, the DC to open that lock
increases by 10 while it remains attached to the object. If the object does not have a lock, this
spell creates one that can only be opened with a DC 20 Disable Device skill check. A door or object
secured with this spell can be opened only by breaking in or with a successful
[dispel magic](ref/spell/dispel-magic) or [knock](ref/spell/knock) spell. Add 10 to the normal DC to
break open a door or portal affected by this spell. A knock spell does not remove an arcane lock; it
only suppresses the effect for 10 minutes.
