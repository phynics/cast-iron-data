+++
id = "ref/spell/calamitous-flailing"
kind = "spell"
title = "Calamitous Flailing"
source_ids = ["blood-of-the-coven"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "calamitous_flailing", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 4 },
  { class = "Mesmerist", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 3 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Bard, Mesmerist, Skald, Spiritualist, Witch\
4: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Descriptors: curse
:::

**Sources:** Blood of the Coven pg 20

You cause the victim's attacks to careen wildly, endangering itself and those around it. Your target
gains a 25% miss chance on all attack rolls. If an attack misses due to this magical effect, the
victim instead targets an ally, or else itself if there are no allies within range of the original
attack. Apply the attack roll for the original attack to the new target's Armor Class to determine
if this attack hits. This is a curse effect.
