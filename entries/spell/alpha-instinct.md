+++
id = "ref/spell/alpha-instinct"
kind = "spell"
title = "Alpha Instinct"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "alpha_instinct", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Charm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 3 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Skald", level = 2 },
]
casting_time = "10 minutes"
components = "V, S, M (a bit of musk from an alpha wolf or another socially dominant animal)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 hour/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Druid, Hunter, Medium, Mesmerist, Ranger, Shaman, Skald\
3: Bard
Casting time: 10 minutes
Components: V, S, M (a bit of musk from an alpha wolf or another socially dominant animal)
Range: personal
Duration: 1 hour/level (D)
Saving throw: none
Spell resistance: no
Target: you
Subschool: Charm
Descriptors: mind-affecting
:::

**Sources:** Ultimate Wilderness pg 227

Animals perceive you as a social superior. The starting attitude of animals you interact with
improves by one step, and you gain a +2 morale bonus on Handle Animal checks. Helpful animals
provide simple assistance (such as using the aid another action on skill checks they understand) as
long as the spell lasts, but they flee from attacks and do not support you in combat. At one point
during the spell's duration, you can issue a nonverbal command to helpful animals within 60 feet to
forage for you; the animal or animals immediately head out into the wilderness to do just that.
After 1 hour, the animals return to the location where you issued the command to make you an
offering of edible food sufficient for one meal for you and a number of others equal to your caster
level.
