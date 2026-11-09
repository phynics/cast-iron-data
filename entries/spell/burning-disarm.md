+++
id = "ref/spell/burning-disarm"
kind = "spell"
title = "Burning Disarm"
source_ids = ["cheliax-empire-of-devils"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "burning_disarm", path = "json/spells2.json" },
]
[[sources]]
publication = "cheliax-empire-of-devils"
page = "22"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["fire"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Red Mantis Assassin", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "held metal item of one creature or 15 lbs. of unattended metal" },
]
duration = "instantaneous"
saving_throw = "Reflex negates (object, see text)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Arcanist, Cleric, Druid, Hunter, Oracle, Red Mantis Assassin, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Reflex negates (object, see text)
Spell resistance: yes (object)
Target: held metal item of one creature or 15 lbs. of unattended metal
Descriptors: fire
:::

This spell causes a metal object to instantly become red hot. A creature holding the item may
attempt a Reflex save to drop it and take no damage (even if it is not their turn), otherwise the
hot metal deals 1d4 points of fire damage per caster level (maximum 5d4). Circumstances that prevent
the creature from dropping the item (such as a locked gauntlet) mean the creature gets no saving
throw. The heat does not harm the item, and it does not get hot enough or last long enough to ignite
flammable objects. The item cools to its previous temperature almost instantly. If cast underwater,
burning disarm deals half damage and boils the surrounding water.
