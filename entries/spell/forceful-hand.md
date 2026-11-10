+++
id = "ref/spell/forceful-hand"
kind = "spell"
title = "Forceful Hand"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "forceful_hand", path = "json/spells13.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/interposing-hand" },
]
[[sources]]
publication = "core-rulebook"
page = "285"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Magus", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, F (a soft glove)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "10-ft. hand" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 6: Arcanist, Magus, Occultist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F (a soft glove)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: yes
Effect: 10-ft. hand
Descriptors: force
:::

This spell functions as [interposing hand](ref/spell/interposing-hand), except that it can also
pursue and bull rush one opponent you select. The forceful hand gets one bull rush attack per round.
This attack does not provoke an attack of opportunity. Its CMB for bull rush checks uses your caster
level in place of its base attack bonus, with a +8 bonus for its Strength score (27), and a +1 bonus
for being Large. The hand always moves with the opponent to push them back as far as possible. It
has no movement limit for this purpose. Directing the spell to a new target is a move action.
Forceful hand prevents the opponent from moving closer to you without first succeeding on a bull
rush attack, moving both the forceful hand and the target closer to you. The forceful hand can
instead be directed to interpose itself, as interposing hand does.
