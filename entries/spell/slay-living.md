+++
id = "ref/spell/slay-living"
kind = "spell"
title = "Slay Living"
aon = "SpellDisplay.aspx?ItemName=Slay%20Living"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "slay_living", path = "json/spells9.json" },
]
[[sources]]
publication = "core-rulebook"
page = "344"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["death"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Cleric", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Shaman", level = 6 },
  { class = "Spiritualist", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Antipaladin\
5: Cleric, Oracle, Spiritualist, Warpriest\
6: Shaman, Witch
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Fortitude partial
Spell resistance: yes
Target: living creature touched
Descriptors: death
:::

You can attempt to slay any one living creature. When you cast this spell, your hand seethes with
eerie dark fire. You must succeed on a melee touch attack to touch the target. The target takes 12d6
points of damage + 1 point per caster level. If the target's Fortitude saving throw succeeds, it
instead takes 3d6 points of damage + 1 point per caster level. The subject might die from damage
even if it succeeds on its saving throw.
