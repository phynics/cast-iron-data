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

## Bestow Curse

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

### Greater Bestow Curse

**Sources:** Pathfinder \#82: Secrets of the Sphinx pg 75

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

### Conditional Curse

**Sources:** Ultimate Intrigue pg 206

This spell functions as bestow curse, except that you must state a condition under which the curse
is broken, ending its effect. An intelligent target, even one of animal intelligence, innately
understands this condition even if it doesn't understand your language. The condition must be
possible for the target to bring about within a year and a day without ensuring its own death and
stated in 25 or fewer words. The curse is more difficult to remove via magic. The DC to remove
conditional curse with [break enchantment](ref/spell/break-enchantment) or
[remove curse](ref/spell/remove-curse) increases by 5.

### Major Curse

**Sources:** Ultimate Magic pg 215

This spell functions as bestow curse, except the DC to remove the curse is equal to the save DC + 5.
