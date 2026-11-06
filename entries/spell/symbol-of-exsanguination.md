+++
id = "ref/spell/symbol-of-exsanguination"
kind = "spell"
title = "Symbol of Exsanguination"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "symbol_of_exsanguination", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 2 },
  { class = "Cleric", level = 3 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "10 minutes"
components = "V, S, M (powdered garnet and bloodstone worth a total of 500 gp)"
range = "0 ft.; see text"
effects = [
  { label = "Effect", value = "one symbol" },
]
duration = "10 minutes/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Bloodrager, Occultist\
3: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M (powdered garnet and bloodstone worth a total of 500 gp)
Range: 0 ft.; see text
Duration: 10 minutes/level
Saving throw: Fortitude negates
Spell resistance: yes
Effect: one symbol
Descriptors: evil
:::

**Sources:** Horror Adventures pg 129

This spell functions like [symbol of death](ref/spell/symbol-of-death), except that each creature
within the radius of symbol of exsanguination begins to bleed uncontrollably and violently from
their eyes, ears, nose, and mouth, as well as any existing open wounds. Creatures that failed their
saving throws immediately take 1d6 points of bleed damage and are sickened as long as they continue
to take bleed damage from the symbol.

While a DC 15 Heal check or magical healing can end the bleed damage as normal, the bleed damage and
sickened condition begin again each round so long as the creature begins its turn still within 60
feet of the symbol, including if the creature leaves the area and returns. Creatures that succeed at
their saving throw suffer no ill effects from the symbol, even if they leave its area and return.

Unlike symbol of death, symbol of exsanguination has no hit point limit on the creatures it can
affect. Once triggered, a symbol of exsanguination remains active for 10 minutes per caster level.

Magic traps such as symbol of exsanguination are hard to detect and disable. While any character can
use Perception to find a symbol, only a character who has the trapfinding class feature can use
Disable Device to disarm it. The DC in each case is equal to 25 + spell level, or 28 (27 for a
bloodrager) for symbol of exsanguination.
