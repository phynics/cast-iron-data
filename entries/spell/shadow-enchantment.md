+++
id = "ref/spell/shadow-enchantment"
kind = "spell"
title = "Shadow Enchantment"
source_ids = ["occult-realms"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadow_enchantment", path = "json/spells15.json" },
]
[[sources]]
publication = "occult-realms"
page = "17"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
descriptors = ["shadow"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "see text"
effects = [
  { label = "Effect", value = "see text" },
]
duration = "see text"
saving_throw = "Will disbelief, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Arcanist, Bard, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: see text
Duration: see text
Saving throw: Will disbelief, see text
Spell resistance: yes
Effect: see text
Subschool: Shadow
Descriptors: shadow
:::

You use material from the Shadow Plane to cast a quasi-real, illusory version of a psychic,
sorcerer, or wizard enchantment spell of 2nd level or lower. Spells that deal damage or have other
effects work as normal unless the affected creature succeeds at a Will save. If the disbelieved
enchantment spell has a damaging effect, that effect is one-fifth as strong (if applicable) or only
20% likely to occur. If recognized as a shadow enchantment, a damaging spell deals only one-fifth
(20%) the normal amount of damage.

If the disbelieved attack has a special effect other than damage, that effect is one-fifth as strong
(if applicable) or only 20% likely to occur. Regardless of the result of the save to disbelieve, an
affected creature is also allowed any save (or [spell resistance](ref/rule/spell-resistance)) that
the spell being simulated allows, but the save DC is set according to shadow enchantment's level
(3rd) rather than the spell's normal level. Objects, mindless creatures, and creatures immune to
mind-affecting effects automatically succeed at their Will saves against this spell.
