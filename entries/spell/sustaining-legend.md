+++
id = "ref/spell/sustaining-legend"
kind = "spell"
title = "Sustaining Legend"
aon = "SpellDisplay.aspx?ItemName=Sustaining%20Legend"
source_ids = ["mythic-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sustaining_legend", path = "json/spells10.json" },
]
[[sources]]
publication = "mythic-origins"
page = "15"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Bard", level = 5 },
  { class = "Cleric", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Skald", level = 5 },
  { class = "Warpriest", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Bard, Skald\
6: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates (harmless)
Spell resistance: yes
Target: one creature/level, no two of which can be more than 30 ft. apart
Subschool: Healing
:::

The rulers of Azlant are thought to have used this spell to amplify the mythic power of themselves
and their most gifted lieutenants. You amplify the mythic power of the target creatures, bolstering
them with healing energy each time they draw upon their mythic abilities. When a creature affected
by this spell expends uses of mythic power for any ability, it immediately heals 2d8 points of
damage + 1 point per caster level (maximum +25). In addition, the creature benefits from one of the
following additional effects.

- Remove any one of the following conditions: dazzled, fatigued, shaken, sickened, or staggered.
- Reduce the dazed or stunned condition to staggered.
- Reduce the exhausted condition to fatigued.
- Reduce the frightened condition to shaken, or the panicked condition to frightened.
- Reduce the nauseated condition to sickened.

A target can benefit from the effects of sustaining legend only once per round, even if the target
expends multiple uses of mythic power during that time.
