+++
id = "ref/carried/advanced-players-guide/rules/new-rules/hero-points/hero-point-spells/malediction"
kind = "spell"
title = "Malediction"
source_ids = ["advanced-players-guide"]
section = ["Rules", "New Rules", "Hero Points", "Hero Point Spells"]
tags = ["necromancy", "death", "evil"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Advanced Players Guide/Rules/New Rules/Hero Points/Hero Point Spells/Malediction", path = "advanced_players_guide/spell/malediction.json" },
]

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
duration = "instantaneous/1 minute per HD of the target; see text"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
School: necromancy \[death, evil\]
Level: 3: Arcanist, Sorcerer, Witch, Wizard
Casting Time: 1 standard action
Components: V, S, F (onyx dust worth 500 gp)
Range: touch
Target: living creature touched
Duration: instantaneous/1 minute per HD of the target; see text
Saving Throw: Will negates
Spell Resistance: yes
:::

_You curse a dying creature to gain hero points._

You utter a dire curse over the body of a dying creature, allowing you to consume its waning life
force. Upon casting this spell, you touch a living creature that has –1 or fewer hit points. If the
target fails its saving throw, it dies and you gain 1 hero point for every 5 Hit Dice possessed by
the target (minimum 1, maximum 3). These hero points last for a number of minutes equal to the
target's Hit Dice. Any hero points remaining when this spell ends are lost.
