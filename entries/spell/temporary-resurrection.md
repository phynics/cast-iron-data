+++
id = "ref/spell/temporary-resurrection"
kind = "spell"
title = "Temporary Resurrection"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "temporary_resurrection", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Occultist", level = 6 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "10 minutes"
components = "V, S, M (diamond dust worth 500 gp)"
range = "touch"
effects = [
  { label = "Target", value = "dead creature touched" },
]
duration = "24 hours"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 6: Occultist\
7: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M (diamond dust worth 500 gp)
Range: touch
Duration: 24 hours
Saving throw: none
Spell resistance: no
Target: dead creature touched
:::

**Sources:** Ultimate Magic pg 243

You restore temporary life to a body that has been dead for less than 48 hours. The spell lasts for
24 hours, after which the target dies again. The target gains 1 permanent negative level while under
the effect of this spell; this negative level goes away when the target dies or is permanently
raised from the dead (such as with [raise dead](ref/spell/raise-dead)). The target still counts as a
dead corpse (but not undead) for the purpose of spells that revive dead creatures, so a cleric can
cast raise dead or a similar spell on the target even while this spell is active. Once a creature
has been revived with temporary resurrection, this spell cannot be used on it again until it is
permanently raised from the dead.
