+++
id = "ref/spell/undeath-sense"
kind = "spell"
title = "Undeath Sense"
source_ids = ["core-rulebook", "potions-and-poisons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "undeath_sense", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/detect-undead" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (earth from a grave)"
range = "60 ft."
effects = [
  { label = "Area", value = "cone-shaped emanation" },
]
duration = "concentration, up to 1 min./level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Alchemist, Arcanist, Cleric, Inquisitor, Investigator, Medium, Mesmerist, Oracle, Paladin, Psychic, Shaman, Sorcerer, Spiritualist, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (earth from a grave)
Range: 60 ft.
Duration: concentration, up to 1 min./level
Saving throw: none
Spell resistance: no
Area: cone-shaped emanation
:::

### Undeath Sense

**Sources:** Potions and Poisons pg 18

You grant the target the ability to pick up on the subtle scents and disturbances to the natural
order that are specific to the living dead, granting the target the ability to sense the presence of
undead creatures. The target is constantly aware of whether there are any undead auras within 60
feet of her in any direction. If at least one undead aura is present, the target can concentrate on
the spell's effects in order to gain more information on the auras present. This functions similarly
to [detect undead](ref/spell/detect-undead), except the number of rounds of concentration needed to
learn about the undead auras is reduced by 1 (1 round to learn the number of auras, and 2 rounds to
learn the strength and location of each aura).
