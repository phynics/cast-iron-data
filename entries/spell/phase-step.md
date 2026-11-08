+++
id = "ref/spell/phase-step"
kind = "spell"
title = "Phase Step"
source_ids = ["core-rulebook", "mythic-adventures", "potions-and-poisons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "phase_step", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/dimension-door" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Target", value = "you and touched objects or other touched willing creatures" },
]
duration = "instantaneous"
saving_throw = "none and Will negates (object)"
spell_resistance = "no and yes (object)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Medium, Summoner\
4: Arcanist, Bard, Magus, Mesmerist, Occultist, Psychic, Skald, Sorcerer, Spiritualist, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V
Range: long (400 ft. + 40 ft./level)
Duration: instantaneous
Saving throw: none and Will negates (object)
Spell resistance: no and yes (object)
Target: you and touched objects or other touched willing creatures
Subschool: Teleportation
:::

### Mythic Dimension Door

**Sources:** Mythic Adventures pg 91

The duration of this spell changes to 1 round per 2 caster levels, and it creates a temporary,
invisible, one-way portal in your square to your destination. You immediately pass through the
portal and arrive at the destination, but you can't take any other creatures with you.

When casting the spell, you can designate a number of creatures equal to your caster level. These
creatures can see and use the portal, passing through it to arrive at the destination (this isn't an
action). A creature that passes through the portal can't take any other actions until its next turn.

### Phase Step

**Sources:** Potions and Poisons pg 17

You instantly transfer the touched creature to a point you designate within range. This otherwise
functions as [the spell dimension door](ref/spell/dimension-door), except that you must have line of
sight and line of effect to the target's destination for this spell's effects to properly function.
