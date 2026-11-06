+++
id = "ref/rule/limited-magic"
kind = "rule"
title = "Limited Magic"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "limited_magic", path = "json/rules_subsystems04.json" },
]

[fields]
kind = "none"
+++

**Sources:** Pathfinder Unchained pg 146

As a character gains caster levels under the normal magic system, the efficacy of her spells can
swing wildly, necessitating a constant reevaluation of each spell's utility. The limited magic rules
are meant to keep spells' power more tightly tiered by spell level and reduce the amount by which a
caster's power level escalates.

When using limited magic rules, all spells are cast at the minimum caster level and with the minimum
required ability score. The minimum caster level of a spell is fixed at 2 × the spell's level - 1,
and does not change based on class levels. A spell's level can vary by class; therefore, different
classes may have different minimum caster levels for the same spell. The minimum ability score for
any spell is 10 + the spell's level, so the save DC for each spell (10 + the spell's level + the
caster's ability score modifier) is also constant. These values are listed below on Table 4-3:
Limited Magic for ease of reference. The CL (9) column lists the minimum caster level for casters
who get up to 9th-level spells, such as the cleric, druid, or wizard. The CL (6) column covers
casters who get 6th-level spells, such as bards. The CL (4) column covers casters who get up to only
4th-level spells, such as paladins and rangers. If a class's spellcasting progression differs from
these minimum caster levels, it always overrides the numbers on this table.

### Table 4-3: Limited Magic

|Spell Level|CL (9)\*|CL (6)|CL (4)|Ability Score|DC|
| --- | --- | --- | --- | --- | --- |
|0|1|1|-|10|10|
|1|1|1|4|11|11|
|2|3|4|7|12|13|
|3|5|7|10|13|14|
|4|7|10|13|14|16|
|5|9|13|-|15|17|
|6|11|16|-|16|19|
|7|13|-|-|17|20|
|8|15|-|-|18|22|
|9|17|-|-|19|23|

\* For a sorcerer, increase the minimum caster level of any spell of 2nd level or higher by 1.

### Limited Magic Items

Spells from magic items use the same rules as above. That means a [fireball](ref/spell/fireball)
cast from a wand created by a sorcerer or wizard has the same save DC and amount of damage dice as a
_[fireball](ref/spell/fireball)_ cast by any sorcerer or wizard. When calculating the base cost or
price of a magic item, always use the minimum CL as defined by this system (even if the item's
creator would have had a higher caster level). Potions and scrolls always default to the appropriate
cleric, druid, or wizard spell level to determine their base costs.

### Heighten Spell

Under this system, spells can still be improved using [Heighten Spell](ref/feat/heighten-spell). A
heightened spell uses the minimum CL, but does so as though it were a higher-level spell. For
example, a _[fireball](ref/spell/fireball)_ heightened to 5th level would have a DC of 17 and deal
9d6 points of damage, the same as a [cone of cold](ref/spell/cone-of-cold) cast in the same slot.

### Other Considerations

Limited magic can take some getting used to. It reduces the power of most spellcasters dramatically,
but can speed the game up by requiring less research into the caster levels of monsters, NPCs, and
magic items. Limited magic can also encourage better-rounded spellcaster characters, especially if
you're using the purchase system to generate ability scores, as there's less reward for focusing
solely on their spellcasting attributes. Using this system means that if a class gets a spell at a
lower level than another class does, that spell's effects are weaker for the former class. A bard's
[heroism](ref/spell/heroism) is not as good as a wizard's. However, classes with slower spell
progressions (such as the bard, paladin, and ranger) have other abilities that keep them competitive
when limited magic weakens the overall power of spells.

Consider altering other rules to account for a landscape with lower average DCs. For instance,
[Great Fortitude](ref/feat/great-fortitude), [Iron Will](ref/feat/iron-will), and
[Lightning Reflexes](ref/feat/lightning-reflexes) might provide only a +1 bonus on saves, or the
increases to spell DCs from [Spell Focus](ref/feat/spell-focus) and
[Greater Spell Focus](ref/feat/greater-spell-focus) could go up to 2.

**With Esoteric Spell Components:** This system works especially well with the
[esoteric material components system](ref/rule/esoteric-material-components). Using both systems
means that spellcasting in the campaign is weaker overall, but can be boosted on occasion by
characters willing to spend money to increase the potency of their spells.
