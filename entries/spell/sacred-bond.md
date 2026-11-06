+++
id = "ref/spell/sacred-bond"
kind = "spell"
title = "Sacred Bond"
source_ids = ["advanced-players-guide", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sacred_bond", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 2 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 round"
components = "V, S, F (a pair of golden bracelets worth 100 gp each worn by both you and the target)"
range = "touch; see text"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Inquisitor, Paladin\
3: Cleric, Oracle, Warpriest
Casting time: 1 round
Components: V, S, F (a pair of golden bracelets worth 100 gp each worn by both you and the target)
Range: touch; see text
Duration: 10 minutes/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Subschool: Healing
:::

**Sources:** Advanced Player's Guide pg 240

To use this spell, you first touch the intended recipient, creating a sympathetic field of healing
energies between you. Once the spell has been cast, you and the target may cast conjuration
(healing) spells with a range of touch upon each other so long as you are within close range (25
ft. + 5 ft./2 levels). Should either you or the target remove your bracelet, the spell immediately
ends.

### Mythic Sacred Bond

**Sources:** Mythic Adventures pg 106\
The range at which you and the target can cast conjuration (healing) spells on each other increases
to medium (100 feet + 10 feet per caster level). When you or the target uses the sacred bond to cast
a healing spell on the other, the caster also heals a number of hit points equal to the minimum
amount the spell can heal.

_Augmented (6th):_ If you expend two uses of mythic power, casting a healing spell through the link
heals the caster the normal amount instead of the minimum amount.

You and the target can use the link to heal each other with targeted healing abilities such as lay
on hands. Unlike with healing spells, a character using a healing ability in this way doesn't heal
herself.
