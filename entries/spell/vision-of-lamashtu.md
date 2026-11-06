+++
id = "ref/spell/vision-of-lamashtu"
kind = "spell"
title = "Vision of Lamashtu"
source_ids = ["inner-sea-world-guide", "pathfinder-5-sins-of-the-saviors"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vision_of_lamashtu", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["evil", "mind-affecting"]
levels = [
  { class = "Cleric", level = 7 },
  { class = "Inquisitor", level = 6 },
  { class = "Oracle", level = 7 },
  { class = "Shaman", level = 7 },
  { class = "Witch", level = 7 },
]
casting_time = "10 minutes (see text)"
components = "V, S"
range = "unlimited"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "instantaneous"
saving_throw = "Will negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 6: Inquisitor\
7: Cleric, Oracle, Shaman, Witch
Casting time: 10 minutes (see text)
Components: V, S
Range: unlimited
Duration: instantaneous
Saving throw: Will negates (see text)
Spell resistance: yes
Target: one living creature
Subschool: Phantasm
Descriptors: evil, mind-affecting
:::

**Sources:** Inner Sea World Guide pg 297, Pathfinder \#5: Sins of the Saviors pg 71

This spell functions exactly as the spell [nightmare](ref/spell/nightmare). In addition to the
effects of that spell, you can cause a second spell to be delivered when the target wakes at the
nightmare's conclusion. You must have this second spell prepared, and it must be cast immediately
after vision of Lamashtu (effectively adding the two spells' casting times). This second spell
"rides along" with the nightmare, affecting the target as soon as it wakes from its fitful sleep.
Any spell can be sent along with the nightmare, so long as it is of 6th level or lower, affects one
target (which is always the nightmare's recipient), and does not deal hit point damage. The second
spell's range is irrelevant for the purposes of vision of Lamashtu, and even touch attacks can be
delivered in this manner (you must still make a successful touch attack in order to affect the
target, though, with the act of touching occurring within the context of the victim's nightmare).
The target is allowed to save against the second spell if a save is allowed. For example, a cleric
of Lamashtu could send bestow curse along as part of a vision of Lamashtu, but not blade barrier
(affects an area), destruction (too high level), or inflict moderate wounds (deals hit point
damage).
