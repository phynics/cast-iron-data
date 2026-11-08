+++
id = "ref/spell/bestow-curse"
kind = "spell"
title = "Bestow Curse"
source_ids = ["core-rulebook", "pathfinder-82-secrets-of-the-sphinx", "ultimate-intrigue", "ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bestow_curse", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse"]
levels = [
  { class = "Adept", level = 3 },
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Cleric", level = 3 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "permanent"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Medium\
3: Adept, Antipaladin, Cleric, Mesmerist, Occultist, Oracle, Shaman, Spiritualist, Warpriest, Witch\
4: Arcanist, Bloodrager, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: permanent
Saving throw: Will negates
Spell resistance: yes
Target: creature touched
Descriptors: curse
:::

**Sources:** PRPG Core Rulebook pg 247

You place a curse on the subject. Choose one of the following.

- -6 decrease to an ability score (minimum 1).
- -4 penalty on attack rolls, saves, ability checks, and skill checks.
- Each turn, the target has a 50% chance to act normally; otherwise, it takes no action.

You may also invent your own curse, but it should be no more powerful than those described above.

The curse bestowed by this spell cannot be dispelled, but it can be removed with a
[break enchantment](ref/spell/break-enchantment), [limited wish](ref/spell/limited-wish),
[miracle](ref/spell/miracle), [remove curse](ref/spell/remove-curse), or [wish](ref/spell/wish)
spell.

Bestow curse counters remove curse.
