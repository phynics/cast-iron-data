+++
id = "ref/spell/aggravate-affliction"
kind = "spell"
title = "Aggravate Affliction"
source_ids = ["pathfinder-82-secrets-of-the-sphinx"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aggravate_affliction", path = "json/spells.json" },
]
[[sources]]
publication = "pathfinder-82-secrets-of-the-sphinx"
page = "75"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous"
saving_throw = "see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Cleric, Druid, Hunter, Oracle, Warpriest, Witch\
4: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: see text
Spell resistance: yes
Target: one creature
:::

All recurring afflictions (those with a frequency, including curses, diseases, and poison) possessed
by the targeted creature immediately trigger, requiring an immediate saving throw (as described in
the affliction) to avoid suffering their effects. A successful saving throw does not count toward
ending the affliction, and this extra save does not change the timing of the next save against the
affliction. Afflictions without a frequency are unaffected by this spell.
