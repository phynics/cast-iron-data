+++
id = "ref/spell/touch-of-slime"
kind = "spell"
title = "Touch of Slime"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "touch_of_slime", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["disease"]
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a drop of acid and a black glass sphere)"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Alchemist, Arcanist, Bloodrager, Druid, Hunter, Investigator, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a drop of acid and a black glass sphere)
Range: touch
Duration: instantaneous
Saving throw: Fortitude negates
Spell resistance: yes
Target: living creature touched
Subschool: Creation
Descriptors: disease
:::

**Sources:** Ultimate Magic pg 243

You create a coating of slime on your hand. When you make a successful melee touch attack with the
slime, it pulls free of you and sticks to the target, at which point it acts like green slime,
dealing 1d3 points of Constitution damage per round. Anything that destroys green slime (scraping,
freezing, burning, cutting, sunlight, or [remove disease](ref/spell/remove-disease)) destroys this
slime. If the slime kills a creature, it consumes the body and then dies. It cannot transfer to a
creature other than the original target, and dies if separated from the original target.
