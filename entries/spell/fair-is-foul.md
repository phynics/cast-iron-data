+++
id = "ref/spell/fair-is-foul"
kind = "spell"
title = "Fair is Foul"
source_ids = ["blood-of-the-coven"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fair_is_foul", path = "json/spells4.json" },
]
[[sources]]
publication = "blood-of-the-coven"
page = "21"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["curse"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a newt eye)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "permanent (D)"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Antipaladin, Witch\
3: Cleric, Oracle, Shaman, Spiritualist, Warpriest\
4: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a newt eye)
Range: touch
Duration: permanent (D)
Saving throw: Fortitude negates
Spell resistance: yes
Target: creature touched
Descriptors: curse
:::

You curse the target with a disfiguring or painful mutation. The target gains one random deformity
from the [Arcane Malignancies table](ref/trait/arcane-malignancies). The curse bestowed by this
spell cannot be dispelled but can be removed with a
[break enchantment](ref/spell/break-enchantment), [limited wish](ref/spell/limited-wish),
[miracle](ref/spell/miracle), [remove curse](ref/spell/remove-curse), or [wish](ref/spell/wish)
spell.
