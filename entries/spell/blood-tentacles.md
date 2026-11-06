+++
id = "ref/spell/blood-tentacles"
kind = "spell"
title = "Blood Tentacles"
source_ids = ["agents-of-evil"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blood_tentacles", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 4 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a fresh handful of the caster's blood)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Antipaladin, Summoner\
5: Arcanist, Cleric, Oracle, Shaman, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a fresh handful of the caster's blood)
Range: personal
Duration: 1 round/level
Saving throw: Will negates (harmless)
Spell resistance: no
Target: you
:::

**Sources:** Agents of Evil pg 30

You smear a handful of your own blood across your chest, causing one writhing tentacle per caster
level to burst forth. You can direct these tentacles to attack a single creature within 15 feet as a
standard action, or one creature per 5 caster levels as a full-round action. Each tentacle has an
attack bonus equal to your base attack bonus plus either your Constitution or Charisma bonus
(whichever is higher). Each tentacle deals 2d6 points of damage, and a tentacle collapses into dried
blood on a successful hit, granting you a number of temporary hit points equal to the damage dealt.
You can't gain more temporary hit points than your maximum number of hit points. These temporary hit
points disappear after 1 hour.
