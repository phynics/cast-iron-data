+++
id = "ref/spell/jannis-jaunt"
kind = "spell"
title = "Janni's Jaunt"
aon = "SpellDisplay.aspx?ItemName=Janni%27s%20Jaunt"
source_ids = ["planes-of-power"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "jannis_jaunt", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/plane-shift" },
]
[[sources]]
publication = "planes-of-power"
page = "9"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["teleportation"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Shaman", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 5 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, F (a forked metal rod attuned to the plane of travel)"
range = "touch"
effects = [
  { label = "Target", value = "Up to eight willing creatures joining hands" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Medium\
4: Cleric, Oracle, Psychic, Warpriest\
5: Summoner, Unchained Summoner\
6: Arcanist, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F (a forked metal rod attuned to the plane of travel)
Range: touch
Duration: instantaneous
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: Up to eight willing creatures joining hands
Subschool: teleportation
:::

### Janni's Jaunt

This spell functions as per [plane shift](ref/spell/plane-shift), but with the following exceptions.
First, you are able to transport only willing creatures. Second, the spell can transport you and any
other willing targets only to an Elemental Plane, the Astral Plane, or the Material Plane.
