+++
id = "ref/spell/undead-anatomy-1"
kind = "spell"
title = "Undead Anatomy I"
aon = "SpellDisplay.aspx?ItemName=Undead%20Anatomy%20I"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "undead_anatomy_1", path = "json/spells11.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "244"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of the creature whose form you plan to assume)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Alchemist, Arcanist, Bloodrager, Investigator, Magus, Red Mantis Assassin, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of the creature whose form you plan to assume)
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
Subschool: Polymorph
:::

When you cast this spell, you can assume the form of any Small or Medium corporeal creature of the
undead type, which must be vaguely humanoid-shaped (like a ghoul, skeleton, or zombie). You gain a
bite attack (1d6 for Medium forms, 1d4 for Small forms), two claw or slam attacks (1d6 for Medium
forms, 1d4 for Small forms), and [darkvision](ref/rule/darkvision) 60 feet. If the form you assume
has any of the following abilities, you gain the listed ability: climb 30 feet, fly 30 feet (average
maneuverability), swim 30 feet, [low-light vision](ref/rule/low-light-vision), and scent.

In this form, you detect as an undead creature (such as with
[detect undead](ref/spell/detect-undead), but not with magic that reveals your true form, such as
[true seeing](ref/spell/true-seeing)) and are treated as undead for the purposes of channeled
energy, cure spells, and inflict spells, but not for other effects that specifically target or react
differently to undead (such as [searing light](ref/spell/searing-light)).

_Small undead:_ If the form you take is that of a Small undead, you gain a +2 size bonus to your
Dexterity and a +1 natural armor bonus.

_Medium undead:_ If the form you take is that of a Medium undead, you gain a +2 size bonus to your
Strength and a +2 natural armor bonus.
