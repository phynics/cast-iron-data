+++
id = "ref/spell/discern-value"
kind = "spell"
title = "Discern Value"
aon = "SpellDisplay.aspx?ItemName=Discern%20Value"
source_ids = ["dungeoneers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "discern_value", path = "json/spells3.json" },
]
[[sources]]
publication = "dungeoneers-handbook"
page = "30"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, F (platinum monocle worth 100 gp)"
range = "60 ft."
effects = [
  { label = "Area", value = "cone-shaped emanation" },
]
duration = "concentration, up to 1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Arcanist, Bard, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F (platinum monocle worth 100 gp)
Range: 60 ft.
Duration: concentration, up to 1 minute/level (D)
Saving throw: none
Spell resistance: no
Area: cone-shaped emanation
:::

You can quickly analyze the monetary value of objects and identify which are most valuable to an
average trader. You must specify a minimum value to detect when you cast this spell (such as 1 gp,
100 gp, or 1,000 gp). The amount of information revealed depends on how long you study a particular
area or subject.

_1st Round:_ Presence or absence of objects worth at least the specified amount.

_2nd Round:_ The most valuable object in range glows brighter than all of the others. If an aura is
outside your line of sight, then you discern its direction but not its exact location.

_3rd Round:_ Objects whose values are within 10% of the most valuable item in range glow slightly.

The spell's effect does not indicate whether an item has magical properties and does not detect
artifacts or items that are priceless.
