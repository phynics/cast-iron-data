+++
id = "ref/spell/vampiric-touch"
kind = "spell"
title = "Vampiric Touch"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vampiric_touch", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "instantaneous/1 hour; see text"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Antipaladin, Arcanist, Bloodrager, Magus, Medium, Mesmerist, Psychic, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous/1 hour; see text
Saving throw: none
Spell resistance: yes
Target: living creature touched
:::

**Sources:** PRPG Core Rulebook pg 364

You must succeed on a melee touch attack. Your touch deals 1d6 points of damage per two caster
levels (maximum 10d6). You gain temporary hit points equal to the damage you deal. You can't gain
more than the subject's current hit points + the subject's Constitution score (which is enough to
kill the subject). The temporary hit points disappear 1 hour later.

### Mythic Vampiric Touch

**Sources:** Mythic Adventures pg 111\
The spell's damage increases to 1d8 points of damage per 2 caster levels (maximum 10d8). Your melee
touch attack to deliver the spell threatens a critical hit on a 19 or 20. This expanded threat range
doesn't stack with other effects or abilities that increase the threat range. If the damage kills
the target, you gain [fast healing](ref/umr/fast-healing) 5 for a number of rounds equal to the Hit
Dice of the target.
