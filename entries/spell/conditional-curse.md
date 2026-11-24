+++
id = "ref/spell/conditional-curse"
kind = "spell"
title = "Conditional Curse"
aon = "SpellDisplay.aspx?ItemName=Conditional%20Curse"
source_ids = ["core-rulebook", "pathfinder-82-secrets-of-the-sphinx", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "conditional_curse", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/bestow-curse" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "206"
[[sources]]
publication = "pathfinder-82-secrets-of-the-sphinx"
page = "75"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 5 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "permanent (see text)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Medium, Mesmerist\
4: Antipaladin, Cleric, Inquisitor, Occultist, Oracle, Shaman, Warpriest, Witch\
5: Arcanist, Psychic, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: permanent (see text)
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Descriptors: curse
:::

### Conditional Curse

This spell functions as [bestow curse](ref/spell/bestow-curse), except that you must state a
condition under which the curse is broken, ending its effect. An intelligent target, even one of
animal intelligence, innately understands this condition even if it doesn't understand your
language. The condition must be possible for the target to bring about within a year and a day
without ensuring its own death and stated in 25 or fewer words. The curse is more difficult to
remove via magic. The DC to remove conditional curse with
[break enchantment](ref/spell/break-enchantment) or [remove curse](ref/spell/remove-curse) increases
by 5.
