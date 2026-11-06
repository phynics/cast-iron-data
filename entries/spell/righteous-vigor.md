+++
id = "ref/spell/righteous-vigor"
kind = "spell"
title = "Righteous Vigor"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "righteous_vigor", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Inquisitor", level = 3 },
  { class = "Paladin", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Paladin\
3: Inquisitor
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 round/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** Advanced Player's Guide pg 239

Infusing the target with a surge of furious divine energy, you enhance a creature's ability to hit
an opponent based on the number of times it has already hit that opponent with a successful attack.
Each time the subject successfully strikes an opponent with a successful melee attack, the subject
gains a cumulative +1 morale bonus on attack rolls (maximum +4 bonus) and gains 1d8 temporary hit
points (to a maximum of 20 temporary hit points). If an attack misses, the attack bonus resets to +0
but any accumulated temporary hit points remain. The temporary hit points disappear at the end of
the spell's duration.
