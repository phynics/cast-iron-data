+++
id = "ref/spell/hunters-eye"
kind = "spell"
title = "Hunter's Eye"
aon = "SpellDisplay.aspx?ItemName=Hunter%27s%20Eye"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hunters_eye", path = "json/spells5.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "228"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 3 },
  { class = "Ranger", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Hunter, Ranger\
3: Inquisitor
Casting time: 1 standard action
Components: V, S, DF
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level
Saving throw: none
Spell resistance: yes
Target: one creature
:::

Sharpening your perceptive abilities and tuning them against obfuscating effects, hunter's eye
greatly enhances your senses against the target creature. You gain the ability to perceive the
target when it is invisible or ethereal as though using the see invisibility spell, and receive a
+20 competence bonus on Perception checks to locate the target. You ignore concealment provided by
fog or mist, [blur](ref/spell/blur), [displacement](ref/spell/displacement),
[invisibility](ref/spell/invisibility), and similar effects affecting the target, but not
concealment provided by darkness. This spell provides no benefits to your allies, and no benefits
against creatures other than the target.
