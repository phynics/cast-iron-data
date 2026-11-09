+++
id = "ref/spell/jannis-jaunt"
kind = "spell"
title = "Janni's Jaunt"
aon = "SpellDisplay.aspx?ItemName=Janni%27s%20Jaunt"
source_ids = ["core-rulebook", "planes-of-power"]
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
subschools = ["Teleportation"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Cleric", level = 5 },
  { class = "Medium", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Shaman", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Spiritualist", level = 5 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, F (a forked metal rod attuned to the plane of travel)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched, or up to eight willing creatures joining hands" },
]
duration = "instantaneous"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Medium\
5: Cleric, Oracle, Psychic, Spiritualist, Summoner, Warpriest\
6: Unchained Summoner\
7: Arcanist, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F (a forked metal rod attuned to the plane of travel)
Range: touch
Duration: instantaneous
Saving throw: Will negates
Spell resistance: yes
Target: creature touched, or up to eight willing creatures joining hands
Subschool: Teleportation
:::

### Janni's Jaunt

This spell functions as per [plane shift](ref/spell/plane-shift), but with the following exceptions.
First, you are able to transport only willing creatures. Second, the spell can transport you and any
other willing targets only to an Elemental Plane, the Astral Plane, or the Material Plane.
