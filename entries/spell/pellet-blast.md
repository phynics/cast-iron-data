+++
id = "ref/spell/pellet-blast"
kind = "spell"
title = "Pellet Blast"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pellet_blast", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Psychic", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a handful of metal pellets or handful of cold iron, silver, or adamantine pellets; see descriptions for cost)"
range = "30 ft."
effects = [
  { label = "Area", value = "cone-shaped burst" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Arcanist, Psychic, Sorcerer, Summoner, Unchained Summoner, Wizard\
4: Bloodrager, Magus
Casting time: 1 standard action
Components: V, S, M (a handful of metal pellets or handful of cold iron, silver, or adamantine pellets; see descriptions for cost)
Range: 30 ft.
Duration: instantaneous
Saving throw: none
Spell resistance: no
Area: cone-shaped burst
Subschool: Creation
:::

**Sources:** Ultimate Combat pg 238

This spell creates an explosion of conjured metal pellets, striking everything within its area and
dealing 1d8 points of piercing damage per two caster levels, maximum 5d8. This damage is subject to
[damage reduction](ref/rule/damage-reduction). If the material component is made of cold iron
(costing 50 gp), silver (costing 20 gp), or adamantine (costing 100 gp), the resulting blast can
overcome damage reduction of the appropriate type. The pellets disappear after the spell is cast and
the damage is dealt.
