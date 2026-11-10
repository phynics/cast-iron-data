+++
id = "ref/spell/plane-shift"
kind = "spell"
title = "Plane Shift"
aon = "SpellDisplay.aspx?ItemName=Plane%20Shift"
source_ids = ["core-rulebook", "planes-of-power"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "plane_shift", path = "json/spells7.json" },
]
[[sources]]
publication = "core-rulebook"
page = "322"

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

You move yourself or some other creature to another plane of existence or alternate dimension. If
several willing persons link hands in a circle, as many as eight can be affected by the plane shift
at the same time. Precise accuracy as to a particular arrival location on the intended plane is nigh
impossible. From the Material Plane, you can reach any other plane, though you appear 5 to 500 miles
(5d%) from your intended destination. Plane shift transports creatures instantaneously and then
ends. The creatures need to find other means if they are to travel back (including casting plane
shift again).
