+++
id = "ref/spell/force-punch"
kind = "spell"
title = "Force Punch"
aon = "SpellDisplay.aspx?ItemName=Force%20Punch"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "force_punch", path = "json/spells13.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "221"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Arcanist, Bloodrager, Magus, Psychic, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Fortitude partial
Spell resistance: yes
Target: creature touched
Descriptors: force
:::

This spell charges your hand with telekinetic force. Your successful melee touch attack deals 1d4
points of force damage per level (maximum 10d4) and causes the target to be pushed away from you in
a straight line up to 5 feet per two caster levels. For every size category of the target above
Medium, reduce the distance pushed by 5 feet (-5 feet for Large, -10 feet for Huge, -15 for
Gargantuan, and -20 feet for Colossal) to a minimum of 0 feet. A successful Fortitude save negates
the movement but not the damage.
