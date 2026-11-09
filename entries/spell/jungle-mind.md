+++
id = "ref/spell/jungle-mind"
kind = "spell"
title = "Jungle Mind"
aon = "SpellDisplay.aspx?ItemName=Jungle%20Mind"
source_ids = ["faiths-and-philosophies"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "jungle_mind", path = "json/spells6.json" },
]
[[sources]]
publication = "faiths-and-philosophies"
page = "28"

[fields]
kind = "spell"
school = "divination"
subschools = ["Scrying"]
levels = [
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Ranger", level = 4 },
]
casting_time = "1 minute"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (see text)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 4: Hunter, Ranger\
5: Druid, Oracle
Casting time: 1 minute
Components: V, S, DF
Range: personal
Duration: 10 minutes/level
Saving throw: Will negates (see text)
Spell resistance: no
Target: you
Subschool: Scrying
:::

You merge your mind into the jungle's social hierarchy, mystically establishing yourself as a master
of wild beasts and an apex predator. You attain knowledge about the general animal population in a
radius of 1 mile as commune with nature, and you then select one type of animal (such as birds,
cats, snakes, or fish). For the duration of the spell, you can sense the location, movement, and
size of creatures of this type in the area, though you can't discern species or individual identity.
In addition, you improve the starting attitude of animals of the chosen type by one step for the
duration of the spell.

As a full-round action, you may focus on a single animal that you can sense with this spell to
establish a mental link. You can read the animal's surface thoughts as detect thoughts, and can see,
hear, and smell what the animal is experiencing using your own Perception skill. If you target
another creature's animal companion, the spell ends if the animal succeeds at a Will save. Using
this ability reduces the spell's remaining duration to 1 round/level, and the selected animal is
treated as the scrying sensor.

Despite the name, jungle mind functions within any terrain.
