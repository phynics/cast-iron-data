+++
id = "ref/spell/speak-local-language"
kind = "spell"
title = "Speak Local Language"
source_ids = ["heroes-of-the-streets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "speak_local_language", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/tongues" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, M/DF (a worn-out coin)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Arcanist, Bard, Cleric, Hunter, Inquisitor, Oracle, Ranger, Skald, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, M/DF (a worn-out coin)
Range: touch
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: no
Target: creature touched
:::

**Sources:** Heroes of the Streets pg 31

This spell functions as [tongues](ref/spell/tongues), except the creature touched gains only the
ability to speak and understand a regional human language, such as Varisian or Common (Taldane in
the Inner Sea region or Tien in Tian Xia), and the language granted must be one you know. You must
select the language at the time of casting. The language can't be a dead language, such as Ancient
Osiriani or Jistka.

The target speaks the language with a native accent, but the spell doesn't impart knowledge about
any culture associated with the language, nor does it change the target's appearance.
