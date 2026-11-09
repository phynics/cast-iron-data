+++
id = "ref/spell/sundering-shards"
kind = "spell"
title = "Sundering Shards"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sundering_shards", path = "json/spells16.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "195"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Red Mantis Assassin", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V"
range = "touch"
effects = [
  { label = "Target", value = "melee weapon touched" },
]
duration = "1 hour/level or until discharged"
saving_throw = "Reflex negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Arcanist, Bloodrager, Magus, Occultist, Psychic, Red Mantis Assassin, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V
Range: touch
Duration: 1 hour/level or until discharged
Saving throw: Reflex negates (see text)
Spell resistance: yes
Target: melee weapon touched
:::

You channel power into a melee weapon. If the weapon's wielder destroys an item with a successful
sunder combat maneuver, she can release the extra power in the weapon, shattering the sundered item
into jagged shards that deal 1d6 points of piercing and slashing damage to the creature that was
wearing, carrying, or wielding the now-shattered item. Any creature (other than the wielder of the
weapon targeted by this spell) adjacent to that creature must succeed at a Reflex saving throw or
take 1d6 points of piercing and slashing damage from flying shards. The shards also count as
whatever special materials the sundered item was made of (for example, the shards from a shattered
cold iron weapon are cold iron). Once the weapon's extra power is unleashed, the spell is
discharged.
