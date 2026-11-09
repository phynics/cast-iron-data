+++
id = "ref/spell/ego-whip-1"
kind = "spell"
title = "Ego Whip I"
aon = "SpellDisplay.aspx?ItemName=Ego%20Whip%20I"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ego_whip_1", path = "json/spells13.json" },
]
[[sources]]
publication = "occult-adventures"
page = "169"

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

You can use your psychic power to overwhelm the target's ego, leaving the target feeling hopeless
and unsure of itself. Choose Intelligence, Wisdom, or Charisma. The target takes a -2 penalty to
that ability score, and is also staggered for the first round it's affected. A successful Will save
negates the staggered effect and reduces the duration of the penalty to 1 round.
