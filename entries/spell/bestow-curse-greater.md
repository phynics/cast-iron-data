+++
id = "ref/spell/bestow-curse-greater"
kind = "spell"
title = "Greater Bestow Curse"
source_ids = ["core-rulebook", "pathfinder-82-secrets-of-the-sphinx", "ultimate-intrigue", "ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bestow_curse_greater", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/bestow-curse" },
]
[[sources]]
publication = "pathfinder-82-secrets-of-the-sphinx"
page = "75"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Cleric", level = 7 },
  { class = "Oracle", level = 7 },
  { class = "Sorcerer", level = 8 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 8 },
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
Level: 7: Cleric, Oracle, Witch\
8: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Target: creature touched
Duration: permanent
Saving throw: Will negates
Spell resistance: yes
Descriptors: curse
:::

### Greater Bestow Curse

You place a curse on the subject. Choose one of the following.

- -12 penalty to an ability score, or -6 penalty to two ability scores (to a minimum ability score
  of 1).
- -8 penalty on attack rolls, saves, ability checks, and skill checks.
- Each turn, the target has a 25% chance to act normally; otherwise, it takes no actions.
- Bestow one of the curses or variants in this article.
- Bestow [curse of the ages](ref/curse/curse-of-the-ages) or [unluck](ref/curse/unluck).

If a specific affliction is bestowed, the save DC of the spell replaces the usual save DC of the
affliction. You can also invent your own curse, but it should be no more powerful than those
described above.

The curse bestowed by this spell cannot be dispelled, but it can be removed with a
[break enchantment](ref/spell/break-enchantment), [limited wish](ref/spell/limited-wish),
[miracle](ref/spell/miracle), or [wish](ref/spell/wish) spell. It cannot be removed with
[remove curse](ref/spell/remove-curse) or suppressed with [abeyance](ref/spell/abeyance). The DC to
remove the curse with break enchantment increases by 5.
