+++
id = "ref/spell/ego-whip-5"
kind = "spell"
title = "Ego Whip V"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ego_whip_5", path = "json/spells13.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/ego-whip-1" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Psychic", level = 3 },
]
casting_time = "1 standard action"
components = "S"
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
School: enchantment
Level: 3: Psychic
Casting time: 1 standard action
Components: S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will partial
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

## Ego Whip I

**Sources:** Occult Adventures pg 169

You can use your psychic power to overwhelm the target's ego, leaving the target feeling hopeless
and unsure of itself. Choose Intelligence, Wisdom, or Charisma. The target takes a -2 penalty to
that ability score, and is also staggered for the first round it's affected. A successful Will save
negates the staggered effect and reduces the duration of the penalty to 1 round.

### Ego Whip II

**Sources:** Occult Adventures pg 169

This functions as [ego whip I](ref/spell/ego-whip-1), but the target takes a -4 penalty to the
chosen ability score and is staggered for 1d4 rounds on a failed Will save. This spell can be
undercast.

### Ego Whip III

**Sources:** Occult Adventures pg 169

This functions as ego whip I, but the target takes a -6 penalty to the chosen ability score and is
staggered for 1d6 rounds on a failed Will save. This spell can be undercast.

### Ego Whip IV

**Sources:** Occult Adventures pg 169

This functions as ego whip I, but the target takes -8 penalty to the chosen ability score and is
staggered for 1d8 rounds on a failed Will save. This spell can be undercast.

### Ego Whip V

**Sources:** Occult Adventures pg 169

This functions as ego whip I, but the target takes -10 penalty to the chosen ability score and is
staggered for 1d10 rounds on a failed Will save. This spell can be undercast.
