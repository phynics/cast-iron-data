+++
id = "ref/arc-bloodrager/symbol-striker"
kind = "archetype"
title = "Symbol Striker"
source_ids = ["heroes-from-the-fringe"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "symbol_striker", path = "json/archetypes_bloodrager.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bloodrager" },
]

[fields]
kind = "archetype"
replaces = ["Fast movement", "Bloodline feats gained at 6th", "12th", "and 18th levels", "Bloodline feat gained at 9th level"]
+++

**Sources:** Heroes from the Fringe pg 7\
Symbol strikers are honored warriors of Dongun Hold, a Sky Citadel in Alkenstar that was a site of
frequent conflicts between the nations of Geb and Nex. The dwarven inhabitants used powerful magic
explosives to seal the fortress against the outside world and prevent the Sky Citadel from becoming
a pawn in the arcane wars between the two powers. Only with the arrival of Ancil Alkenstar in 4588
AR did Dongun Hold reopen itself to the outside world. By then, the constant exposure to strange
runic energies and the long isolation had caused a unique form of rune-wielding berserker
spellcaster to develop, though the symbol striker tradition has since spread beyond its origins.

**Gained class skills:** ling

**Lost class skills:** ha

**Rune Training (Sp)**

**Ability:** A symbol striker can cast [read magic](ref/spell/read-magic) at will and
[comprehend languages](ref/spell/comprehend-languages) once per day, but only to decipher written
text. A symbol striker also adds [arcane mark](ref/spell/arcane-mark) and [erase](ref/spell/erase)
to his bloodrager spell list as 1st-level spells, though he must select these as spells known to be
able to cast them.

**Replaces:** Fast movement

**Weapon Rune (Su)**

**Ability:** Also as a **standard action**, the symbol striker can make a melee attack with a weapon
that has an active weapon rune and, if the attack is successful, deal normal weapon damage and also
expend the weapon rune to discharge the stored spell into the target, as if delivering the spell
with the [magus](ref/class/magus) spellstrike class feature.

**Gained:** At 6th Level

**Replaces:** Bloodline feats gained at 6th, 12th, and 18th levels

**Standard:** A symbol striker can imbue any spell he knows that has a range of touch or greater and
a defined number of targets (rather than an area or other non-target-based effect) into a melee
weapon he is holding. The spell forms itself into a brightly glowing rune, which is obvious to a
casual observer. This ability functions only while the symbol striker wields the weapon. If dropped
or taken, the weapon ceases granting this ability until it is returned to the symbol striker. The
symbol striker can have only a single weapon rune active at a time; if he casts an additional weapon
rune while a previous rune is active, the earlier rune fades. Weapon runes also fade when the symbol
striker regains his spell slots for the day. Otherwise, the rune remains until the spell is
discharged or dispelled.

**Usage:** 1 time/day per 6 bloodrager levels

**Rune Trap (Sp)**

**Gained:** At 9th Level

**Replaces:** Bloodline feat gained at 9th level

**Special:** A symbol striker cannot create a _rune trap_ in a square occupied by another creature.
This rune counts as a 1st-level spell for the purpose of dispelling. A creature can disarm the rune
by succeeding at a DC 26 Disable Device check.

**Standard:** The symbol striker can use a melee weapon to place a _rune trap_ in any adjacent
square. Any creature entering a square containing a _rune trap_ takes damage equal to 1d6 +
[half](ref/misc/fractions-and-rounding) of his bloodrager level. This rune deals either acid, cold,
electricity, or fire damage, which is decided at the rune's creation. The rune is clearly visible
and lasts a number of minutes equal to the symbol striker's bloodrager level or until discharged.

**Usage:** Cha3 modifier times/day
