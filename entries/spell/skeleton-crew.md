+++
id = "ref/spell/skeleton-crew"
kind = "spell"
title = "Skeleton Crew"
source_ids = ["pirates-of-the-inner-sea"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "skeleton_crew", path = "json/spells9.json" },
]
[[sources]]
publication = "pirates-of-the-inner-sea"
page = "29"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M"
range = "touch"
effects = [
  { label = "Targets", value = "one or more humanoid corpses touched" },
]
duration = "1 day/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Cleric, Oracle, Warpriest\
4: Arcanist, Sorcerer, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M
Range: touch
Duration: 1 day/level
Saving throw: none
Spell resistance: no
Targets: one or more humanoid corpses touched
:::

This spell turns corpses into skeletons that act as crew and obey your commands to the extent of
their abilities.

The undead you create are 1 Hit Die skeletons that possess Profession (sailor) scores equal to half
your character level plus your Wisdom modifier (for clerics), Intelligence modifier (for witches and
wizards), or Charisma modifier (for sorcerers and summoners). Each skeleton can perform the duties
of one crew member but has no other abilities. The created skeletons cannot speak, attack, or even
defend themselves. The only orders they obey are ones pertaining to the operation of a ship.
Skeletal crew members are not proficient with any weapons or armor.

You can't create more Hit Dice of skeletal crew members than twice your caster level with a single
casting of skeleton crew. The desecrate spell doubles this limit.

The undead you create by casting skeleton crew remain under your control for the duration of the
spell, and do not count against your limit of total Hit Dice worth of undead creatures you can
control.

A skeletal crew member can only be created from a mostly intact humanoid corpse. The corpse must
have bones. When you cast this spell, any flesh left on the corpses melts away into fog.
