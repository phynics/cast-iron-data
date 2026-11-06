+++
id = "ref/spell/depilate"
kind = "spell"
title = "Depilate"
source_ids = ["blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "depilate", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 round"
components = "S, M (a sliver of cow's tongue)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature with hair or fur" },
]
duration = "instantaneous"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Arcanist, Bard, Druid, Hunter, Skald, Sorcerer, Witch, Wizard
Casting time: 1 round
Components: S, M (a sliver of cow's tongue)
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: Will negates
Spell resistance: yes
Target: one creature with hair or fur
:::

**Sources:** Blood of the Beast pg 27

> _While [tengus](ref/race/tengu) are renowned for their supposed ability to eat bad luck or hex
> with a foul stare, most tengus have long forgotten the jinx magic their ancestors perfected
> millennia ago in the mountains of Tian Xia to confound meddling visitors bearing imperial decrees.
> Only a handful of these luck-manipulating spells now remain known outside the secretive temples of
> Hei Feng, largely practiced by tengu witches and the occasional tengu or halfling rogue, by way of
> the [major magic](ref/talent/major-magic) rogue talent._

This simple jinx causes a target's hair or fur to fall out in patchy clumps, leaving the creature
disheveled and less commanding. A jinxed creature takes a -2 penalty on all Diplomacy, Intimidate,
and Perform checks until the hair begins to regrow 1 week later, or until the damage can be
concealed with a successful Disguise or Heal check (the DC is equal to the original save DC of the
spell). A successful [break enchantment](ref/spell/break-enchantment),
[remove curse](ref/spell/remove-curse), or similar effect instantly regrows the target's hair or fur
and removes the spell's effects.
