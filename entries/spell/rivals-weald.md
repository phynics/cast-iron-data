+++
id = "ref/spell/rivals-weald"
kind = "spell"
title = "Rival's Weald"
source_ids = ["chronicle-of-legends"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rivals_weald", path = "json/spells8.json" },
]
[[sources]]
publication = "chronicle-of-legends"
page = "14"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Druid", level = 9 },
  { class = "Shaman", level = 9 },
  { class = "Witch", level = 9 },
]
casting_time = "1 standard action"
components = "V, S, M (a hardened piece of tree sap)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/two levels, no two of which can be more than 30 ft. apart" },
]
duration = "permanent"
saving_throw = "Fortitude negates, Will partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 9: Druid, Shaman, Witch
Casting time: 1 standard action
Components: V, S, M (a hardened piece of tree sap)
Range: close (25 ft. + 5 ft./2 levels)
Duration: permanent
Saving throw: Fortitude negates, Will partial (see text)
Spell resistance: yes
Target: one creature/two levels, no two of which can be more than 30 ft. apart
Subschool: Polymorph
:::

This spell transforms your targets into trees as per [tree shape](ref/spell/tree-shape), except the
targets transform into living trees that resemble their original forms. If a target is in a
situation that would prove fatal to a tree created by this spell, such as off the ground or under
water, the target receives a +4 bonus on its Fortitude save.

If the spell succeeds, the target must also attempt a Will save. On a failed save, the creature
loses the ability to observe what transpires around it, and its mental capacity reverts to that of a
tree, rendering it unable to take any kind of action. A target that succeeds at the saving throw can
observe the area around it but can't take any actions other than communicate to those under the
effects of a [speak with plants](ref/spell/speak-with-plants) spell or to other trees. Over the span
of 1 year, the target's appearance becomes more like a common tree and less like its original form.

Any polymorph effects on a target are automatically dispelled when the target fails to resist the
effects of rival's weald, and as long as rival's weald remains in effect, the target cannot use
other polymorph spells or effects to assume a new form. Incorporeal, gaseous, and plant creatures
are immune to rival's weald.
