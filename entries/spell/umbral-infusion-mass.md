+++
id = "ref/spell/umbral-infusion-mass"
kind = "spell"
title = "Mass Umbral Infusion"
source_ids = ["blood-of-shadows"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "umbral_infusion_mass", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["shadow"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Cleric", level = 8 },
  { class = "Oracle", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one mindless undead creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 minute/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 8: Arcanist, Cleric, Oracle, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Target: one mindless undead creature/level, no two of which can be more than 30 ft. apart
Duration: 1 minute/level
Saving throw: Will negates
Spell resistance: yes
Descriptors: shadow
:::

## Umbral Infusion

**Sources:** Blood of Shadows pg 31

You infuse the target mindless undead creature with power drawn from the Shadow Plane, immediately
granting it the advanced creature simple template. It gains a +2 bonus on all rolls, including
damage rolls, a +2 bonus to special ability DCs, a +4 bonus to AC and CMD, and 2 additional hit
points per Hit Die. The undead creature's destructive instincts take hold for the duration of this
spell, and any attempts to control or command the undead creature have a 50% chance of failing; if
uncontrolled, the undead creature attacks any living creatures it sees. This spell has no effect on
undead creatures that already have the advanced creature template.

### Mass Umbral Infusion

**Sources:** Blood of Shadows pg 31

This spell functions as umbral infusion, except it can affect multiple mindless undead creatures.
