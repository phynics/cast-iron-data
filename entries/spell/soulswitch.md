+++
id = "ref/spell/soulswitch"
kind = "spell"
title = "Soulswitch"
source_ids = ["familiar-folio"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "soulswitch", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, F (two brass collars worth 50 gp each)"
range = "touch"
effects = [
  { label = "Targets", value = "you and your familiar" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 5: Arcanist, Bard, Cleric, Druid, Hunter, Inquisitor, Magus, Oracle, Shaman, Skald, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F (two brass collars worth 50 gp each)
Range: touch
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Targets: you and your familiar
:::

**Sources:** Familiar Folio pg 23

You may only cast this spell if you currently have a familiar. You place your soul into the body of
your familiar, and your familiar's soul is placed in your body. This functions as if you possessed
your familiar using [magic jar](ref/spell/magic-jar); your familiar simultaneously possesses your
body in the same manner. You can't freely transfer your soul between your body and your familiar's -
if you choose to return to your body as a standard action, the spell ends. If either body is killed,
both spirits return to their original bodies, the spell ends, and the original owner of the slain
body dies.
