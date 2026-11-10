+++
id = "ref/spell/share-skin"
kind = "spell"
title = "Share Skin"
aon = "SpellDisplay.aspx?ItemName=Share%20Skin"
source_ids = ["blood-of-the-moon"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "share_skin", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/magic-jar" },
]
[[sources]]
publication = "blood-of-the-moon"
page = "11"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Witch", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one animal touched" },
]
duration = "1 minute/level or until you return to your body"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 6: Druid, Hunter, Witch
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute/level or until you return to your body
Saving throw: none
Spell resistance: no
Target: one animal touched
:::

> _The following spells are common among [werebears](ref/template/lycanthrope) coldborn
> [skinwalkers](ref/race/skinwalker), and those who associate with them._

You can possess an animal's body in a manner that functions like [magic jar](ref/spell/magic-jar),
except as noted here. Your body vanishes while the effect lasts and you don't require a receptacle.
