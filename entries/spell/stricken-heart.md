+++
id = "ref/spell/stricken-heart"
kind = "spell"
title = "Stricken Heart"
aon = "SpellDisplay.aspx?ItemName=Stricken%20Heart"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "stricken_heart", path = "json/spells15.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "194"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["death"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Arcanist, Inquisitor, Mesmerist, Psychic, Sorcerer, Spiritualist, Witch, Wizard\
3: Shaman
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Target: creature touched
Descriptors: death
:::

This spell covers your hand with a writhing black aura. As part of casting the spell, you can make a
melee touch attack that deals 2d6 points of negative energy damage and causes the target to be
staggered for 1 round. If the attack is a critical hit, the target is staggered for 1 minute
instead. Creatures immune to precision damage are immune to the staggered effect.
