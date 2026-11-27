+++
id = "ref/arc-spiritualist/grim-apostle"
kind = "archetype"
title = "Grim Apostle"
aon = "ArchetypeDisplay.aspx?FixedName=Spiritualist%20Grim%20Apostle"
source_ids = ["pathfinder-144-midwives-to-death"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "grim_apostle", path = "json/archetypes_spiritualist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/spiritualist" },
]
[[sources]]
publication = "pathfinder-144-midwives-to-death"
page = "72"

[fields]
kind = "archetype"
features = [
  { anchor = "grim-phantom", level = 1 },
  { anchor = "hardened-soul", level = 1 },
]
trades = [
  { replaces = "The phantom's emotional focus", feature = "phantom", power = "emotional focus", by = ["grim-phantom"] },
  { replaces = "Shared consciousness", feature = "shared-consciousness", by = ["hardened-soul"] },
  { replaces = "fused consciousness", feature = "fused-consciousness", by = ["hardened-soul"] },
  { alters = "Phantom", feature = "phantom", by = ["grim-phantom"] },
]
+++

Some devotees of the Four Horsemen can form spiritual manifestations of the daemonic demigods.

## Grim Phantom (Su) {#grim-phantom}

The spirit linked to a grim apostle functions in all respects as a regular spiritualist's phantom,
but each day when the grim apostle regains her daily spell slots, she can choose which Horseman
focus (see below) is dominant within the grim phantom.

When the grim phantom is banished to the Ethereal Plane, the grim apostle takes an amount of damage
equal to 1d4 × the grim phantom's number of Hit Dice.

This ability modifies the phantom ability and replaces the phantom's emotional focus.

## Hardened Soul (Su) {#hardened-soul}

At 1st level, while a grim phantom is confined in the grim apostle's consciousness, the grim apostle
gains a +4 bonus on saving throws against death effects and effects that would remove or subsume the
grim apostle's soul (such as _[possession](ref/spell/possession)_ or
_[trap the soul](ref/spell/trap-the-soul)_). At 6th level and every 6 levels thereafter, this bonus
increases by 2 (to a maximum of +10 at 18th level). This ability replaces shared consciousness and
fused consciousness.

## Horseman Focus {#horseman-focus}

Instead of an emotional focus, a grim phantom has one of the following Horseman foci.

The DC for a saving throw against any of the grim phantom's abilities is equal to 10 + 1/2 the grim
phantom's Hit Dice + the grim phantom's Charisma modifier. For any
[spell-like abilities](ref/umr/spell-like-abilities) a grim phantom receives, it uses its Hit Dice
as its caster level.

### Death {#death}

Grim phantoms influenced by [Charon](ref/faith/charon), the Horseman of Death, are dark, almost
shapeless specters.

#### Skills {#skills}

The grim phantom gains ranks in Knowledge (history) and Stealth equal to its number of Hit Dice.

#### Good Saves {#good-saves}

Fortitude and Will.

#### Fleet {#fleet}

The grim phantom gains [Fleet](ref/feat/fleet) as a bonus feat.

#### Marked for Death (Su) {#marked-for-death}

When manifested in ectoplasmic form, the grim phantom gains a +1 bonus on attack rolls against a
creature the grim apostle has hit with a melee or ranged attack since its last turn (the phantom's
"marked target"). Additionally, such an attack by the grim phantom deals an additional 1d6 points of
negative energy damage. At 5th level and every 5 spiritualist levels thereafter, the negative energy
damage increases by 1d6.

#### Fatal Aura (Su) {#fatal-aura}

At 7th level, the grim phantom can create a 10-foot-radius aura as a swift action that makes healing
more difficult. The DC of Heal checks to provide first aid and treat deadly wounds within the aura
is increased by 5. Any creature within the aura that casts a conjuration (healing) spell, or casts
another spell or uses an ability that restores hit points, must succeed at a Will saving throw or
lose the spell or use of the ability. Ending the aura is a free action.

#### No Escape (Su) {#no-escape}

At 12th level, the grim phantom gains the benefits of the [Following Step](ref/feat/following-step),
[Step Up](ref/feat/step-up), and [Step Up and Strike](ref/feat/step-up-and-strike) feats but only
against its marked target (see above).

#### Killing Word (Sp) {#killing-word}

At 17th level, the grim phantom can cast _[power word kill](ref/spell/power-word-kill)_ once per day
as a [spell-like ability](ref/umr/spell-like-abilities).

### Famine {#famine}

Grim phantoms influenced by [Trelmarixian](ref/faith/trelmarixian), the Horseman of Famine, are
gaunt with jackal-like features.

#### Skills {#famine-skills}

The grim phantom gains ranks in Perception and Sense Motive equal to its number of Hit Dice.

#### Good Saves {#famine-good-saves}

Reflex and Will.

#### Weapon Finesse {#weapon-finesse}

The grim phantom gains [Weapon Finesse](ref/feat/weapon-finesse) as a bonus feat.

#### Ravenous Bite (Ex) {#ravenous-bite}

The grim phantom's natural attacks take the form of bites that deal piercing damage as a creature
[one size category larger](ref/misc/damage-die-adjustments) than its current size. It also gains
[Power Attack](ref/feat/power-attack) as a bonus feat.

#### Aura of Starvation (Su) {#aura-of-starvation}

At 7th level, the grim phantom can create a 10-foot-radius aura of starvation as a swift action.
Enemies within the aura take a -2 penalty on attack and damage rolls. Ending the aura is a free
action.

#### Wail of the Hungry (Sp) {#wail-of-the-hungry}

At 12th level, the grim phantom can cast _[waves of fatigue](ref/spell/waves-of-fatigue)_ once per
day as a [spell-like ability](ref/umr/spell-like-abilities).

#### Distended Gullet (Su) {#distended-gullet}

At 17th level, as a swift action, the grim phantom in ectoplasmic form gains the
[swallow whole](ref/umr/swallow-whole) ability (_Pathfinder RPG Bestiary_ 304; 4d8 negative energy
damage, AC 17, one-tenth the phantom's total hit points) for a number of rounds equal to its
Charisma modifier. This ability can affect creatures no more than two size categories larger than
the phantom. Each creature the grim phantom swallows is shunted into an extradimensional space that
can hold any number of creatures. When the duration of this ability ends, any creatures still within
the extradimensional space appear adjacent to the grim phantom. The grim phantom is
[exhausted](ref/misc/exhausted) for 1 hour after using this ability and can't use it again during
that time.

### Pestilence {#pestilence}

Grim phantoms influenced by [Apollyon](ref/faith/apollyon), the Horseman of Pestilence, often have
rams' skulls for heads.

#### Skills {#pestilence-skills}

The grim phantom gains ranks in Acrobatics and Heal equal to its number of Hit Dice.

#### Good Saves {#pestilence-good-saves}

Fortitude and Will.

#### Great Fortitude {#great-fortitude}

The grim phantom gains [Great Fortitude](ref/feat/great-fortitude) as a bonus feat.

#### Weakening Strike (Su) {#weakening-strike}

A creature hit by the grim phantom's slam attack must succeed at a Fortitude saving throw or take a
-2 penalty on ability checks, attack rolls, saving throws, and skill checks for 1d4 rounds. This is
a disease effect. Penalties from multiple hits don't stack.

#### Aura of Flies (Su) {#aura-of-flies}

At 7th level, the grim phantom can surround itself with a cloud of biting flies as a swift action.
Any creature that ends its turn adjacent to the grim phantom takes 1d6 piercing damage. This damage
increases by 1d6 for every 4 spiritualist levels beyond 7th. Ending the aura is a free action.

#### Contagious Touch (Sp) {#contagious-touch}

At 12th level, the grim phantom can cast _[contagion](ref/spell/contagion)_ three times per day as a
[spell-like ability](ref/umr/spell-like-abilities).

#### Virulent Attack (Su) {#virulent-attack}

At 17th level, any creature under the effects of the grim phantom's weakening strike becomes a
dangerous vector for disease. Any creature that ends its turn adjacent to the target creature is
immediately exposed to any diseases the target creature has, no matter the normal method of
contracting that disease. The creature must immediately attempt a saving throw against that disease,
and the onset period doesn't apply.

### War {#war}

Grim phantoms influenced by [Szuriel](ref/faith/szuriel), the Horseman of War, look like sinister,
black-winged angels.

#### Skills {#war-skills}

The grim phantom gains ranks in Intimidate and Survival equal to its number of Hit Dice.

#### Good Saves {#war-good-saves}

Fortitude and Reflex.

#### Strength Focus {#strength-focus}

The grim phantom gains a +2 bonus to Strength and a -2 penalty to Dexterity. The phantom gains
bonuses to Strength instead of Dexterity as the grim apostle gains spiritualist levels.

#### Ruthless Combatant (Su) {#ruthless-combatant}

The grim phantom threatens a critical hit with its slam attack on a roll of 19–20. At 11th level,
the phantom's critical modifier with slam attacks increases to ×3. This doesn't stack with
[Improved Critical](ref/feat/improved-critical) or similar effects.

#### Aura of Fury (Su) {#aura-of-fury}

At 7th level, the grim phantom can create a 20-foot-radius aura as a swift action. Creatures within
the aura gain a +2 bonus on melee attack rolls but take a -2 penalty to AC. Ending the aura is a
free action.

#### Bloodlust (Su) {#bloodlust}

At 12th level, the grim phantom regains 1d6 hit points with each successful slam attack it makes.

#### Juggernaut (Su) {#juggernaut}

At 17th level, the grim phantom becomes immune to any effects that would cause it to become
cowering, exhausted, fatigued, frightened, panicked, shaken, or slowed (as the
_[slow](ref/spell/slow)_ spell).
