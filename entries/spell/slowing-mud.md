+++
id = "ref/spell/slowing-mud"
kind = "spell"
title = "Slowing Mud"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "slowing_mud", path = "json/spells9.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "192"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Shaman", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (earth and water)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level (see text)"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Druid, Hunter, Shaman
Casting time: 1 standard action
Components: V, S, M (earth and water)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (see text)
Saving throw: Fortitude negates
Spell resistance: yes
Targets: one creature/level, no two of which can be more than 30 ft. apart
Subschool: Creation
:::

You coat the targets in thick, sticky mud. The mud acts as a [slow](ref/spell/slow) spell and also
blinds the targets. A creature can use a standard action to remove the mud from its eyes or the eyes
of an adjacent creature, ending the blinded condition for that individual. Removing enough mud to
end the slow effect is a full-round action. Jumping into a lake or being subject to an effect that
creates a lot of water (such as create water or hydraulic push) removes all the mud in 1 round.

A haste effect cast on a creature slowed by the mud allows it to act normally for the duration of
the haste. Slow does not stack with the effects of slowing mud. This spell cannot counter or dispel
haste.
