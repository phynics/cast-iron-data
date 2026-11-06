+++
id = "ref/spell/enchantment-sight"
kind = "spell"
title = "Enchantment Sight"
source_ids = ["heroes-of-the-high-court"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "enchantment_sight", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "10 minutes/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Alchemist, Arcanist, Bard, Cleric, Inquisitor, Investigator, Medium, Mesmerist, Occultist, Oracle, Paladin, Psychic, Skald, Sorcerer, Spiritualist, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 10 minutes/level (D)
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Heroes of the High Court pg 10

Your irises take on a purplish tinge and you can see whether creatures within 60 feet of you are
affected by an enchantment effect. To your eyes only, a creature under the effects of an enchantment
spell glows with a simple white light around its head. You can immediately discern whether the
brightness of the light is faint, moderate, strong, or overwhelming depending on the highest spell
level of enchantment currently in effect (as per detect magic). Enchantments of the charm or
compulsion subschool glow with a scarlet or emerald hue, respectively.

If a creature under an enchantment effect is in your line of sight, you can attempt a Spellcraft
check as a move action to determine the highest-level spell or spell effect (DC = 15 + the spell
level, or 15 + 1/2 the caster level for a non-spell effect). Effects that block divination magic
also block this spell.

Enchantment sight can be made permanent with a [permanency](ref/spell/permanency) spell cast by a
caster of 9th level or higher, at a cost of 2,500 gp.
