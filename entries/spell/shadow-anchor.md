+++
id = "ref/spell/shadow-anchor"
kind = "spell"
title = "Shadow Anchor"
aon = "SpellDisplay.aspx?ItemName=Shadow%20Anchor"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadow_anchor", path = "json/spells15.json" },
]
[[sources]]
publication = "advanced-race-guide"
page = "211"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
descriptors = ["shadow"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
  { label = "Effect", value = "a shadowy shadow tether" },
]
duration = "1 round/level (d); see text"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 2: Arcanist, Bard, Mesmerist, Psychic, Red Mantis Assassin, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: S
Range: touch
Duration: 1 round/level (d); see text
Saving throw: Will negates
Spell resistance: yes
Target: creature touched
Effect: a shadowy shadow tether
Subschool: Shadow
Descriptors: shadow
:::

> _[Wayangs](ref/race/wayang) have access to the following spell._

The target's shadow becomes a flexible tether to its current square. The creature can move up to 5
feet from that square without penalty. Moving farther than 5 feet from the tether point requires the
target to make a bull rush combat maneuver check against a CMB of 10 + 1/2 your caster level + your
Intelligence modifier (if a witch or wizard) or Charisma modifier (if a bard or sorcerer). The
target takes a -1 penalty for every 5 feet of distance between it and its tethered square. Failing
this check means the target's move is wasted and it cannot move farther away. If it fails this check
by 10 or more, it is pulled 5 feet toward the tether square and is knocked prone. If it beats the
check by 10 or more, the spell ends. This spell does not work on creatures that do not cast shadows
or reflections. If the target uses a teleportation effect or leaves the current plane, the spell
ends.
