+++
id = "ref/spell/forests-sense"
kind = "spell"
title = "Forest's Sense"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "forests_sense", path = "json/spells13.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "231"

[fields]
kind = "spell"
school = "divination"
subschools = ["Scrying"]
levels = [
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Shaman", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "1 mile/level"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 minute/level (d); see text"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Hunter, Ranger\
4: Druid, Shaman
Casting time: 1 standard action
Components: V, S
Range: 1 mile/level
Duration: 1 minute/level (d); see text
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Scrying
:::

You can sense the location of a target creature within range if it is also within 10 feet of a
living plant or fungus. You must be able to target the creature by tangible qualities such as its
build, clothing texture, size, or tracks, but you need not have line of effect to your target. The
fungus or plants near the target serve as a scrying sensor for this spell. Your senses of hearing,
smell, and touch extend to all fungus and plants within 10 feet of the target, allowing you to gauge
the size and shape of nearby objects and potentially to overhear conversations in which the target
is currently participating. Your scent ability and [tremorsense](ref/umr/tremorsense) extend through
this scrying sensor if you have them, but any other special senses you might have do not. For 1 day
after casting this spell, you gain a +5 insight bonus on Survival checks to track creatures you
sensed via the spell. You can dismiss this bonus on Survival checks.
