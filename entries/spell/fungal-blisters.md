+++
id = "ref/spell/fungal-blisters"
kind = "spell"
title = "Fungal Blisters"
source_ids = ["pathfinder-119-prisoners-of-the-blight"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fungal_blisters", path = "json/spells13.json" },
]
[[sources]]
publication = "pathfinder-119-prisoners-of-the-blight"
page = "70"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level or until discharged (see text)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Alchemist, Arcanist, Druid, Hunter, Investigator, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level or until discharged (see text)
Saving throw: none
Spell resistance: no
Target: you
:::

> _Worshippers of [Cyth-V'sug](ref/faith/cyth-vsug) have access to the following spell._

When you cast this spell, horrible, fungal growths sprout forth all over your body. You develop
1d2+1 of these blisters per 2 caster levels. Each time you are dealt more than 5 points of
bludgeoning, piercing, or slashing damage from a single attack, one of these blisters bursts,
releasing a cloud of harmful spores in a 5-foot-radius burst centered on you. These spores enter the
lungs of all living creatures within the cloud that need to breathe and deal 1d6+1 points of damage
for every 2 caster levels you have (Fortitude negates). This is a disease effect, and you and plants
aren't affected by the spores. It is possible for more than one blister to burst in a single round.
If you are reduced to 0 or fewer hit points, all remaining blisters burst, and the resulting spores
deal the cumulative amount of damage.

You are not able to cast this spell while wearing heavy armor. If you don heavy armor during the
spell's duration, all remaining blisters burst as if you had been reduced to 0 or fewer hit points.
