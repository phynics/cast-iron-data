+++
id = "ref/spell/malediction-hero-points"
kind = "spell"
title = "Malediction (Hero Points)"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "malediction_hero_points", path = "json/spells6.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "324"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["death", "evil"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, F (onyx dust worth 500 gp)"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "instantaneous/1 minute per hd of the target; see text"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F (onyx dust worth 500 gp)
Range: touch
Duration: instantaneous/1 minute per hd of the target; see text
Saving throw: Will negates
Spell resistance: yes
Target: living creature touched
Descriptors: death, evil
:::

You utter a dire curse over the body of a dying creature, allowing you to consume its waning life
force. Upon casting this spell, you touch a living creature that has -1 or fewer hit points. If the
target fails its saving throw, it dies and you gain 1 hero point for every 5 Hit Dice possessed by
the target (minimum 1, maximum 3). These hero points last for a number of minutes equal to the
target's Hit Dice. Any hero points remaining when this spell ends are lost.
