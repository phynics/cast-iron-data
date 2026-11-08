+++
id = "ref/spell/conditional-curse"
kind = "spell"
title = "Conditional Curse"
source_ids = ["core-rulebook", "pathfinder-82-secrets-of-the-sphinx", "ultimate-intrigue", "ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "conditional_curse", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/bestow-curse" },
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

This spell functions as [bestow curse](ref/spell/bestow-curse), except that you must state a
condition under which the curse is broken, ending its effect. An intelligent target, even one of
animal intelligence, innately understands this condition even if it doesn't understand your
language. The condition must be possible for the target to bring about within a year and a day
without ensuring its own death and stated in 25 or fewer words. The curse is more difficult to
remove via magic. The DC to remove conditional curse with
[break enchantment](ref/spell/break-enchantment) or [remove curse](ref/spell/remove-curse) increases
by 5.

### Major Curse

**Sources:** Ultimate Magic pg 215

This spell functions as bestow curse, except the DC to remove the curse is equal to the save DC + 5.
