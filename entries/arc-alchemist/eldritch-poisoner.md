+++
id = "ref/arc-alchemist/eldritch-poisoner"
kind = "archetype"
title = "Eldritch Poisoner"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Eldritch%20Poisoner"
source_ids = ["black-markets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "eldritch_poisoner", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "black-markets"
page = "28"

[fields]
kind = "archetype"
features = [
  { anchor = "arcanotoxin", level = 1 },
  { anchor = "toxicologist", level = 1 },
  { anchor = "sneak-attack", level = 1 },
  { anchor = "careful-injection", level = 4 },
]
trades = [
  { replaces = "Bomb", feature = "bomb", by = ["arcanotoxin"] },
  { replaces = "Throw Anything", feature = "throw-anything", by = ["toxicologist"] },
  { replaces = "Mutagen", feature = "mutagen", by = ["sneak-attack"] },
  { replaces = "persistent mutagen", feature = "persistent-mutagen", by = ["sneak-attack"] },
  { replaces = "The discovery gained at 4th level", feature = "discovery", levels = [4], by = ["careful-injection"] },
]
+++

Eldritch poisoners are masters of the toxic arts, synthesizing lethal and incapacitating poisons
with uncanny speed and expertise.

## Arcanotoxin (Su) {#arcanotoxin}

An eldritch poisoner can blend volatile chemicals and her own personal magic to create deadly
poisons known as arcanotoxins. She can use this ability a number of times each day equal to her
alchemist level + her Intelligence modifier. An arcanotoxin functions only when used by the eldritch
poisoner and becomes inert if not used within 1 minute. Creating an arcanotoxin is a standard
action, and it can be applied to a weapon as a move action.

At 1st level, an eldritch poisoner must choose whether her arcanotoxin deals Strength or Dexterity
damage. At 3rd level and every 2 alchemist levels thereafter, she can enhance her arcanotoxin in one
of the following ways. She can't select the same improvement twice in a row.

- Select one additional form of ability damage: Charisma, Dexterity, Intelligence, Strength, or
  Wisdom.
- Grant an onset time of 1 round, or increase an existing onset time by 2 rounds (maximum 11
  rounds).
- Increase the ability damage die [by one step](ref/misc/damage-die-adjustments) (maximum 1d6).
- Increase the number of consecutive saves required to cure the poison by 1 (maximum 3).
- Increase the frequency by 2 rounds (maximum 10 rounds).

If an eldritch poisoner can deal different kinds of ability damage, she selects which ability to
affect each time she creates a dose of arcanotoxin, and can willingly reduce enhanced aspects of her
arcanotoxin, such as the save DC or onset time. Some discoveries apply secondary effects; a dose of
arcanotoxin can cause only one secondary effect. Alchemist discoveries that affect mundane poisons
do not apply to an arcanotoxin.

This ability replaces bomb.

**Arcanotoxin**

**Type** poison, injury; **Save** Fortitude DC = 10 + 1/2 the eldritch poisoner's alchemist level +
her Intelligence modifier\
**Frequency** 1/round for 2 rounds\
**Effect** 1d2 ability damage (see above); **Cure** 1 save

## Toxicologist (Ex) {#toxicologist}

An eldritch poisoner gains a +2 bonus on Craft (alchemy) checks to create poisons and antitoxins,
and creates them in [half](ref/misc/fractions-and-rounding) the normal amount of time. This ability
replaces Throw Anything.

## Sneak Attack (Ex) {#sneak-attack}

At 1st level, the eldritch poisoner gains a [sneak attack](ref/ability/sneak-attack) identical to
the rogue class feature, dealing 1d6 points of sneak attack damage at 1st level; the damage
increases by 1d6 at 4th level and every 4 alchemist levels thereafter. This ability replaces mutagen
and persistent mutagen.

## Discoveries {#discoveries}

An eldritch poisoner can select any of the following discoveries, in addition to those available to
other alchemists. Arcanotoxin discoveries with a save DC use her arcanotoxin's save DC.

### Antidote (Su) {#antidote}

The eldritch poisoner can sacrifice one use of her arcanotoxin to create an extract of
_[delay poison](ref/spell/delay-poison)_, which she can feed to an adjacent, willing creature as a
standard action. Beginning at 10th level, she can instead use this ability to create an extract of
_[neutralize poison](ref/spell/neutralize-poison)_.

### Apothecary (Ex, Sp) {#apothecary}

The eldritch poisoner can use _[detect poison](ref/spell/detect-poison)_ at will as a
[spell-like ability](ref/umr/spell-like-abilities) and gains a bonus equal to 1/2 her alchemist
level on Heal checks to identify or treat poisons and to the bonus she grants when successfully
treating a poison.

### Combine Toxins (Ex) {#combine-toxins}

An eldritch poisoner can diversify her arcanotoxin, dealing damage to any two ability scores with a
single dose. The alchemist must already know how to target both ability scores with her arcanotoxin.
A combined toxin reduces the damage die of its arcanotoxin by one step, to a minimum of 1 point of
ability damage to each ability score.

### Contact Toxin (Su) {#contact-toxin}

The eldritch poisoner can create her arcanotoxin as a contact poison. A vial of contact arcanotoxin
can be thrown up to 30 feet as a ranged touch attack or smeared onto a surface as a standard action,
but it becomes inert after 1 minute. The arcanotoxin's save DC is reduced by 2. The eldritch
poisoner must be at least 4th level to select this discovery.

### Envenom (Su) {#envenom}

The eldritch poisoner can create and apply her arcanotoxin to a held weapon (her own or an ally's)
as a move action. The toxin lasts 1 minute or until used.

### Lethal Toxin (Su) {#lethal-toxin}

The eldritch poisoner's arcanotoxin can deal Constitution damage. She must be at least 10th level to
select this discovery.

### Mind-Altering Toxin (Su) {#mind-altering-toxin}

Whenever a creature fails its saving throw against the eldritch poisoner's arcanotoxin, it also
becomes [dazzled](ref/misc/dazzled) by hallucinations for the toxin's duration as a secondary
effect. When the alchemist reaches 10th level, targets become [confused](ref/misc/confused) instead.
The alchemist must be at least 6th level to select this discovery.

### Paralytic Toxin (Su) {#paralytic-toxin}

Whenever a creature fails its saving throw against the eldritch poisoner's arcanotoxin, it also
becomes [staggered](ref/misc/staggered) for the toxin's duration as a secondary effect. Beginning at
15th level, the target becomes [paralyzed](ref/rule/paralyzed) instead. The poisoner must be at
least 8th level to select this discovery.

### Sickening Toxin (Su) {#sickening-toxin}

When a creature fails its save against the eldritch poisoner's arcanotoxin, it also becomes
[sickened](ref/misc/sickened) for the toxin's duration as a secondary effect. When the alchemist
reaches 12th level, targets become [nauseated](ref/misc/nauseated) instead.

### Tailored Toxin (Ex) {#tailored-toxin}

Choose one creature type (and subtype, for humanoids or outsiders). The eldritch poisoner's
arcanotoxin is particularly effective against such creatures, increasing the save DC by 2. This
discovery can be selected more than once; each time it applies to a different creature type (or
subtype).

### Toxic Fumes (Ex) {#toxic-fumes}

The eldritch poisoner can create her arcanotoxin as an inhaled poison. She can throw a vial of
arcanotoxin up to 30 feet as a ranged touch attack, affecting all creatures in a 10-foot-by-10-foot
square. The arcanotoxin's save DC is reduced by 4, its duration is halved, and a successful save
immediately ends the inhaled arcanotoxin's effect. The eldritch poisoner must be at least 6th level
to select this discovery.

## Careful Injection (Ex) {#careful-injection}

At 4th level, an eldritch poisoner can forgo some of her sneak attack damage in order to increase
the save DC of a poison or arcanotoxin on the weapon used to make the sneak attack. The poison's DC
increases by 1 for every 1d6 points of sneak attack damage forgone. This ability replaces the
discovery gained at 4th level.
