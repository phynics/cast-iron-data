+++
id = "ref/arc-paladin/invigorator"
kind = "archetype"
title = "Invigorator"
source_ids = ["healers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "invigorator", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]

[fields]
kind = "none"
+++

**Sources:** Healer's Handbook pg 24\
Invigorators devote themselves to keeping their allies bodily whole. These selfless paladins believe
the best way to combat evil is by bolstering the health and spirits of those who fight alongside
them. They play vital roles and often command troops among martial faiths, such as those of
[Iomedae](ref/faith/iomedae) and [Torag](ref/faith/torag).

**Bestow Hope (Su)**

**Action:** Ability

**At 20th Level:** The invigorator may choose a number of nonevil allies equal to her Charisma
modifier + 2.

**At 7th Level:** The invigorator may choose a number of nonevil allies equal to her Charisma
modifier + 1.

**Gained:** At 1st Level

**Replaces:** Smite evil

**Special:** The DR this ability grants does not stack with the DR the invigorator receives from
_aura of righteousness_ or _holy champion._

**Usage:** Charisma3 modifier times/day

At 4th level: The DR 2/-.

At 7th level: The DR 3/-.

At 10th level: The DR 4/-.

At 13th level: The DR 5/-.

At 16th level: The DR 6/-.

At 19th level: The DR 7/-.

An invigorator is a champion of her faith who can call upon her deity's holy power to bathe battling
allies in protective energy. As a **swift action** during combat, the invigorator can choose a
number of nonevil allies within sight equal to her Charisma modifier upon whom to _bestow hope._
Once activated, _bestow hope_ grants the invigorator and these allies DR 1/- until the combat ends,
at which point the [damage reduction](ref/rule/damage-reduction) immediately ends.

During a battle, the invigorator can change the allies this ability affects as a **swift action**.
Ending it is a **free action**, but each time it is activated during a single combat, another use of
the ability is expended. The invigorator must participate in the combat to use this ability. If she
is frightened, panicked, paralyzed, stunned, unconscious, or otherwise prevented from participating
in the combat, any DR this ability bestows is temporarily suspended until she can participate in the
combat again; this doesn't count as ending the ability.

**Holy Fount (Su)**

**Free:** An invigorator can expend two uses of _bestow hope_ to radiate healing energies to bolster
her nearby allies. For a number of rounds equal to 1/2 the invigorator's paladin level, the
invigorator and all nonevil allies within a 10-foot radius of her gain
[fast healing](ref/umr/fast-healing) 10.

**Gained:** At 11th Level

**Replaces:** Aura of justice

**Special:** This ability is an aura centered on the invigorator; allies must be within the aura at
the beginning of their turns to benefit from the [fast healing](ref/umr/fast-healing).

**Champion of Life (Sp)**

**Flavor:** An invigorator's holy resolve can sometimes overcome death - or smite the horror that is
undeath.

**Gained:** At 20th Level

**Replaces:** Holy champion

**Standard:** Three per day, an invigorator can use [breath of life](ref/spell/breath-of-life) as a
[spell-like ability](ref/umr/spell-like-abilities), using her paladin level as her caster level.
Creatures brought back to life with this ability do not suffer the normal temporary negative level
the spell imposes.
