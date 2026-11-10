+++
id = "ref/spell/pyrotechnics"
kind = "spell"
title = "Pyrotechnics"
aon = "SpellDisplay.aspx?ItemName=Pyrotechnics"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pyrotechnics", path = "json/spells15.json" },
]
[[sources]]
publication = "core-rulebook"
page = "328"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (one fire source)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Target", value = "one fire source, up to a 20-ft. cube" },
]
duration = "1d4+1 rounds, or 1d4+1 rounds after creatures leave the smoke cloud; see text"
saving_throw = "Will negates or Fortitude negates; see text"
spell_resistance = "yes or no; see text"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Bloodrager, Bard, Magus, Mesmerist, Psychic, Red Mantis Assassin, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (one fire source)
Range: long (400 ft. + 40 ft./level)
Duration: 1d4+1 rounds, or 1d4+1 rounds after creatures leave the smoke cloud; see text
Saving throw: Will negates or Fortitude negates; see text
Spell resistance: yes or no; see text
Target: one fire source, up to a 20-ft. cube
:::

Pyrotechnics turns a fire into a burst of blinding fireworks or a thick cloud of choking smoke,
depending on your choice. The spell uses one fire source, which is immediately extinguished. A fire
so large that it exceeds a 20-foot cube is only partly extinguished. Magical fires are not
extinguished, although a fire-based creature used as a source takes 1 point of damage per caster
level.

_Fireworks:_ The fireworks are a flashing, fiery, momentary burst of glowing, colored aerial lights.
This effect causes creatures within 120 feet of the fire source to become blinded for 1d4+1 rounds
(Will negates). These creatures must have line of sight to the fire to be affected.
[Spell resistance](ref/rule/spell-resistance) can prevent blindness.

_Smoke Cloud:_ A stream of smoke billows out from the fire, forming a choking cloud that spreads 20
feet in all directions and lasts for 1 round per caster level. All sight, even
[darkvision](ref/rule/darkvision), is ineffective in or through the cloud. All within the cloud take
-4 penalties to Strength and Dexterity (Fortitude negates). These effects last for 1d4+1 rounds
after the cloud dissipates or after the creature leaves the area of the cloud.
[Spell resistance](ref/rule/spell-resistance) does not apply.
