+++
id = "ref/spell/detect-magic-greater"
kind = "spell"
title = "Greater Detect Magic"
source_ids = ["core-rulebook", "adventurers-guide", "andoran-spirit-of-liberty", "ultimate-intrigue", "potions-and-poisons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "detect_magic_greater", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "60 ft."
effects = [
  { label = "Area", value = "cone-shaped emanation" },
]
duration = "concentration, up to 1 min./level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Arcanist, Bard, Cleric, Druid, Hunter, Inquisitor, Magus, Medium, Mesmerist, Occultist, Oracle, Psychic, Shaman, Skald, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: 60 ft.
Area: cone-shaped emanation
Duration: concentration, up to 1 min./level (D)
Saving throw: none
Spell resistance: no
:::

## Detect Magic

**Sources:** PRPG Core Rulebook pg 267

You detect magical auras. The amount of information revealed depends on how long you study a
particular area or subject.

_1st Round:_ Presence or absence of magical auras.

_2nd Round:_ Number of different magical auras and the power of the most potent aura.

_3rd Round:_ The strength and location of each aura. If the items or creatures bearing the auras are
in line of sight, you can make Knowledge (arcana) skill checks to determine the school of magic
involved in each. (Make one check per aura: DC 15 + spell level, or 15 + 1/2 caster level for a
non-spell effect.) If the aura eminates from a magic item, you can attempt to identify its
properties (see [Spellcraft](ref/skill/spellcraft)).

Magical areas, multiple types of magic, or strong local magical emanations may distort or conceal
weaker auras.

_Aura Strength:_ An aura's power depends on a spell's functioning spell level or an item's caster
level; see the accompanying table. If an aura falls into more than one category, detect magic
indicates the stronger of the two.

_Lingering Aura:_ A magical aura lingers after its original source dissipates (in the case of a
spell) or is destroyed (in the case of a magic item). If detect magic is cast and directed at such a
location, the spell indicates an aura strength of dim (even weaker than a faint aura). How long the
aura lingers at this dim level depends on its original power:

|Original Strength|Duration of Lingering Aura|
| --- | --- |
|Faint|1d6 rounds|
|Moderate|1d6 minutes|
|Strong|1d6 × 10 minutes|
|Overwhelming|1d6 days|

Outsiders and elementals are not magical in themselves, but if they are summoned, the conjuration
spell registers. Each round, you can turn to detect magic in a new area. The spell can penetrate
barriers, but 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or
dirt blocks it.

Detect magic can be made permanent with a [permanency](ref/spell/permanency) spell.

|Item|Faint Aura|Moderate|Strong|Overwhelming|
| --- | --- | --- | --- | --- |
|Functioning spell (spell level)|3rd or lower|4th-6th|7th-9th|10th+ (deity-level)|
|Magic item (caster level)|5th or lower|6th-11th|12th-20th|21st+ (artifact)|

### Detect Charm

**Sources:** Adventurer's Guide pg 77, Andoran, Spirit of Liberty pg 27

This spell functions as per _[detect magic](ref/spell/detect-magic),_ except that it detects only
charm, compulsion, and possession effects. You immediately detect the strength and location of each
such aura on all creatures in the area. You can attempt to identify the properties of each aura (see
[Spellcraft](ref/skill/spellcraft)). In addition to noticing the targets of these effects, you can
recognize when creatures in the area are using these effects on others by attempting a
[Sense Motive](ref/skill/sense-motive) check as a standard action (DC = 20 + caster level). If you
succeed, you can attempt a Spellcraft check to identify what magic it is using (even if the target
is not in the area).

### Greater Detect Magic

**Sources:** Ultimate Intrigue pg 212

This spell functions as _[detect magic](ref/spell/detect-magic),_ except that you can glean much
more information from the magical auras that you find, and those auras can be found after a much
greater length of time. You can detect a lingering aura for up to 1 day per caster level you have,
regardless of the aura's original strength.

Additionally, when you use a standard action to concentrate on this spell, you can also study a
creature within the spell's area and attempt a Spellcraft check in order to determine the last spell
that the creature cast by identifying lingering traces that the spell left in the caster's aura. The
DC to identify the spell is equal to 20 + the creature's caster level.

Finally, you are able to locate and analyze the signature flourishes in a magical aura that allow
you to match a spell to the person who cast it. In order to find these identifiers in a spell's
aura, you must spend 1 round focusing on that spell in particular, and succeed at an opposed
Knowledge (arcana) check against the caster (or a Knowledge \[arcana\] check with a DC equal to 15 +
the spell level if the caster wants her work to be identified and emphasizes these unique elements
rather than obscuring them). Once you learn a caster's set of identifiers, you can remember them as
easily as a face or a voice. You can recognize this signature if you succeed at a Spellcraft check
when later identifying a spell to determine whether or not that spell was cast by the same
individual. The spell greater magic aura can obfuscate this information, making it seem that someone
else cast the spell. Greater detect magic grants a saving throw against magic aura (but not greater
magic aura).

### Identifier's Eye

**Sources:** Potions and Poisons pg 17

This spell infuses a spark of magical energy into the veins of the target, allowing it to feel the
presence of magic the way one might feel the thrum of vibrations in the air. For the spell's
duration, the target gains the benefits of the spell _[detect magic](ref/spell/detect-magic)_ and
also gains a +5 enhancement bonus on Spellcraft checks to identify the properties and command words
of magic items. Further, the target can attempt such checks untrained while under the effects of
this spell. This ability does not allow the target to identify artifacts.
