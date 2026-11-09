+++
id = "ref/spell/blade-tutors-spirit"
kind = "spell"
title = "Blade Tutor's Spirit"
source_ids = ["melee-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blade_tutors_spirit", path = "json/spells12.json" },
]
[[sources]]
publication = "melee-tactics-toolbox"
page = "30"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Magus", level = 1 },
  { class = "Paladin", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Magus\
2: Antipaladin, Arcanist, Paladin, Sorcerer, Summoner, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: you
Subschool: Creation
:::

You summon an insubstantial spirit of force that resembles a cloudy vapor hovering around your fists
or any melee weapons you wield. The spirit compensates for your defensive or reckless melee attacks,
nudging your weapons in the proper direction. When you voluntarily use one or more actions or feats
that apply penalties to attack rolls with your melee weapons (such as a charge, fighting
defensively, or using the [Power Attack](ref/feat/power-attack) feat), the spirit reduces the total
penalty on affected attacks by 1 (to a minimum penalty of 0). The penalty is reduced by an
additional 1 for every 5 caster levels you possess (to a minimum penalty of 0). Only penalties
incurred by voluntary use of feats or maneuvers are reduced by this spell.

The spirit can't be attacked or harmed by physical attacks, but
[disintegrate](ref/spell/disintegrate), [dispel magic](ref/spell/dispel-magic), a
[rod of cancellation](ref/magic-rod/rod-of-cancellation), or a
[sphere of annihilation](ref/magic-artifact/sphere-of-annihilation) can affect it. A protective
spirit's AC against touch attacks is equal to 10 + your Dexterity modifier.
