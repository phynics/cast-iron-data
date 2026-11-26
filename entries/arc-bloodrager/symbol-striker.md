+++
id = "ref/arc-bloodrager/symbol-striker"
kind = "archetype"
title = "Symbol Striker"
aon = "ArchetypeDisplay.aspx?FixedName=Bloodrager%20Symbol%20Striker"
source_ids = ["heroes-from-the-fringe"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "symbol_striker", path = "json/archetypes_bloodrager.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bloodrager" },
]
[[sources]]
publication = "heroes-from-the-fringe"
page = "7"

[fields]
kind = "archetype"
features = [
  { anchor = "rune-training", level = 1 },
  { anchor = "weapon-rune", level = 6 },
  { anchor = "rune-trap", level = 9 },
]
trades = [
  { replaces = "Fast movement", feature = "fast-movement", by = ["rune-training"] },
  { replaces = "Bloodline feats gained at 6th, 12th, and 18th levels", feature = "bloodline", levels = [6, 12, 18], power = "bloodline feat", by = ["weapon-rune"] },
  { replaces = "Bloodline feat gained at 9th level", feature = "bloodline", levels = [9], power = "bloodline feat", by = ["rune-trap"] },
  { alters = "Class skills" },
]
+++

Symbol strikers are honored warriors of Dongun Hold, a Sky Citadel in Alkenstar that was a site of
frequent conflicts between the nations of Geb and Nex. The dwarven inhabitants used powerful magic
explosives to seal the fortress against the outside world and prevent the Sky Citadel from becoming
a pawn in the arcane wars between the two powers. Only with the arrival of Ancil Alkenstar in 4588
ar did Dongun Hold reopen itself to the outside world. By then, the constant exposure to strange
runic energies and the long isolation had caused a unique form of rune-wielding berserker
spellcaster to develop, though the symbol striker tradition has since spread beyond its origins.

## Skills {#skills}

A symbol striker gains Linguistics as a class skill, but does not gain Handle Animal as a class
skill.

This alters the bloodrager's class skills.

## Rune Training (Sp) {#rune-training}

A symbol striker can cast _[read magic](ref/spell/read-magic)_ at will and
_[comprehend languages](ref/spell/comprehend-languages)_ once per day, but only to decipher written
text. A symbol striker also adds _[arcane mark](ref/spell/arcane-mark)_ and
_[erase](ref/spell/erase)_ to his bloodrager spell list as 1st-level spells, though he must select
these as spells known to be able to cast them.

This replaces fast movement.

## Weapon Rune (Su) {#weapon-rune}

At 6th level, once per day as a standard action, a symbol striker can imbue any spell he knows that
has a range of touch or greater and a defined number of targets (rather than an area or other
non-target-based effect) into a melee weapon he is holding. The spell forms itself into a brightly
glowing rune, which is obvious to a casual observer. This ability functions only while the symbol
striker wields the weapon. If dropped or taken, the weapon ceases granting this ability until it is
returned to the symbol striker. The symbol striker can have only a single weapon rune active at a
time; if he casts an additional weapon rune while a previous rune is active, the earlier rune fades.
Weapon runes also fade when the symbol striker regains his spell slots for the day. Otherwise, the
rune remains until the spell is discharged or dispelled. At 12th level, a symbol striker can use
this ability twice per day. At 18th level, he can use this ability three times per day.

As a standard action, the symbol striker can make a melee attack with a weapon that has an active
weapon rune and, if the attack is successful, deal normal weapon damage and also expend the weapon
rune to discharge the stored spell into the target, as if delivering the spell with the
[magus](ref/class/magus) spellstrike class feature.

This replaces the bloodline feats gained at 6th, 12th, and 18th levels.

## Rune Trap (Sp) {#rune-trap}

At 9th level, as a standard action, the symbol striker can use a melee weapon to place a rune trap
in any adjacent square. Any creature entering a square containing a rune trap takes 1d6 points of
damage plus 1 additional point of damage for every 2 bloodrager levels the symbol striker has. This
rune deals either acid, cold, electricity, or fire damage, which is decided at the rune's creation.
The rune is clearly visible and lasts a number of minutes equal to the symbol striker's bloodrager
level or until discharged. A symbol striker cannot create a rune trap in a square occupied by
another creature. This rune counts as a 1st-level spell for the purpose of dispelling. A creature
can disarm the rune by succeeding at a DC 26 Disable Device check. The symbol striker can use this
ability a number of times per day equal to 3 plus his Charisma modifier.

This replaces the bloodline feat gained at 9th level.
