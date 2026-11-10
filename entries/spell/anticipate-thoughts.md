+++
id = "ref/spell/anticipate-thoughts"
kind = "spell"
title = "Anticipate Thoughts"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "anticipate_thoughts", path = "json/spells.json" },
]
[[sources]]
publication = "occult-adventures"
page = "157"

[fields]
kind = "spell"
school = "divination"
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level"
saving_throw = "Will partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Arcanist, Bard, Inquisitor, Magus, Mesmerist, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will partial
Spell resistance: yes
Target: one creature
Descriptors: mind-affecting
:::

This spell taps into the target's mind so you get an impression of the actions it will take. You
gain a +2 insight bonus to AC against the target's attacks. If the target fails its Will save, you
also see how the target will react to your attacks, and the bonus applies on your attack rolls and
damage rolls against the target. These bonuses apply only while the target is within range of the
spell, though if it goes out of range, the bonuses return once it's back in range. Whenever the
target misses you with an attack, the spell's bonuses increase by 1 until the spell ends (to a
maximum of +5).
