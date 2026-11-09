+++
id = "ref/spell/fortunes-path"
kind = "spell"
title = "Fortune's Path"
source_ids = ["disciples-doctrine"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fortunes_path", path = "json/spells13.json" },
]
[[sources]]
publication = "disciples-doctrine"
page = "10"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "10 minutes"
components = "V, S, M (incense worth 50 gp), F (silver mirror worth at least 100 gp)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Bard, Skald\
3: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 10 minutes
Components: V, S, M (incense worth 50 gp), F (silver mirror worth at least 100 gp)
Range: personal
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: you
:::

You predict events in your near future. Visions of the foretold events appear in the mirror after
you cast this spell. Roll d% and add your caster level (maximum 10) to determine results this spell
returns, as listed below.

|d%|Result|
| --- | --- |
|01-15|The mirror is murky. You foresee nothing specific.|
|16-35|You inaccurately predict a major event similar to the major events described in the 76-100 result.|
|36-50|You accurately predict a minor event likely to happen in the following week with no context, such as the chance meeting of an acquaintance, discovery of interesting but inapplicable information, victory in a minor game of chance, or the like. Alternatively, you predict an event so likely to happen that it might be obvious, such as the birth of a child or the collapse of a poorly built structure.|
|51-75|You accurately predict a generally positive or negative event to happening in the following week in a broad category such as academic, battle, domestic, political, professional, romantic, social, or travel. The details of the prediction should provide enough context for you to determine how your actions in the past week have influenced the happening.|
|76-100|You accurately predict a major event likely to happen in the next week. For example, you might foresee an enemy ambush, the discovery of sought-after information, or inclement weather causing significant travel delay (though this spell would not show you the event's exact details). At the GM's discretion, the vision might depict the location of the event.|
