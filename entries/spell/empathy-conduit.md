+++
id = "ref/spell/empathy-conduit"
kind = "spell"
title = "Empathy Conduit"
source_ids = ["familiar-folio"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "empathy_conduit", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, F (a glass rod)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "an animal companion, familiar, or other bonded creature and its master (which may be no more than 30 ft. apart)" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 5: Arcanist, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F (a glass rod)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Targets: an animal companion, familiar, or other bonded creature and its master (which may be no more than 30 ft. apart)
:::

**Sources:** Familiar Folio pg 23

You make a conduit between the targeted master and her familiar, allowing you to target the master
or the familiar with your spells in order to affect the other. If the master succeeds at its save to
resist this spell but the familiar fails, you can choose to have your spells that target the master
affect the familiar instead. If the familiar resists but the master doesn't, your spells that target
the familiar can affect the master instead. If both the familiar and the master fail to resist this
spell, you can affect either the familiar or the master when you target either with a spell. When
you target the master to affect her familiar or vice versa, the target attempts a save (if one is
allowed) with its own saving throw bonus, but the other creature is affected by the spell.

Only spells that target one or more creatures can be cast through empathy conduit. The creature to
be affected must still be a valid target of the spell being cast; for example, you can't affect a
familiar with charm person through an empathy conduit. Spells with a duration other than
instantaneous that are cast through an empathy conduit last either their normal duration or until
the empathy conduit expires, whichever comes first. Whenever the master or its familiar is targeted
with a spell intended to affect the other creature, the targeted creature can attempt an additional
save against the empathy conduit.
