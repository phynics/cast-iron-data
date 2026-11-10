+++
id = "ref/spell/spore-burst"
kind = "spell"
title = "Spore Burst"
aon = "SpellDisplay.aspx?ItemName=Spore%20Burst"
source_ids = ["cohorts-and-companions"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spore_burst", path = "json/spells9.json" },
]
[[sources]]
publication = "cohorts-and-companions"
page = "21"

[fields]
kind = "spell"
school = "conjuration"
descriptors = ["poison"]
levels = [
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Ranger", level = 3 },
  { class = "Shaman", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a tiny puffball mushroom)"
range = "touch"
effects = [
  { label = "Target", value = "one plant creature; see text" },
]
duration = "see text"
saving_throw = "special, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Druid, Hunter, Shaman, Witch\
3: Ranger
Casting time: 1 standard action
Components: V, S, M (a tiny puffball mushroom)
Range: touch
Duration: see text
Saving throw: special, see text
Spell resistance: no
Target: one plant creature; see text
Descriptors: poison
:::

You cause a willing plant creature's body to sprout small, puffy mushrooms that remain for 1 round
per caster level or until the creature uses them. As a standard action, the target can cause these
mushrooms to burst open, releasing a cloud of toxic spores that affect all creatures in a
20-foot-radius spread. Those in the area must succeed at Fortitude saves or be sickened for 1d6
rounds as they are overcome by sneezing and coughing. The caster is immune to this poison effect, as
are all creatures of the plant type.
