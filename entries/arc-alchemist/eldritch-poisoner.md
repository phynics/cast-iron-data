+++
id = "ref/arc-alchemist/eldritch-poisoner"
kind = "archetype"
title = "Eldritch Poisoner"
source_ids = ["black-markets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "eldritch_poisoner", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]

[fields]
kind = "archetype"
replaces = ["Bomb", "Throw Anything", "Mutagen", "persistent mutagen", "The discovery gained at 4th level"]
+++

**Sources:** Black Markets pg 28\
Eldritch poisoners are masters of the toxic arts, synthesizing lethal and incapacitating poisons
with uncanny speed and expertise.

**Arcanotoxin (Su)**

**Action:** Choice

**Flavor:** An eldritch poisoner can blend volatile chemicals and her own personal magic to create
deadly poisons known as arcanotoxins.

**Gained:** At 1st Level

**Move:** Apply an arcanotoxin to a weapon.

**Replaces:** Bomb

**Special:** An arcanotoxin functions only when used by the eldritch poisoner and becomes inert if
not used within 1 minute.

**Standard:** Create an arcanotoxin.

**Usage:** alchemist level + Intelligence modifier times/day

_The base stats for the arcanotoxin are presented below this ability block._

At 1st level, an eldritch poisoner must choose whether her arcanotoxin deals 1d2 Strength or
Dexterity damage. At 3rd level and every 2 alchemist levels thereafter (5th, 7th, 9th, and so on),
she can enhance her arcanotoxin in one of the following ways. She can't select the same improvement
twice in a row.

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

**Arcanotoxin**

**Type:** Poison (injury)

**Save:** Fortitude 10 + 1/2 the eldritch poisoner's level + her Int modifier

**Frequency:** 1/round for 2 rounds

**Effect:** 1d2 ability damage (see above)

**Cure:** 1 save

**Toxicologist (Ex)**

**Gained:** At 1st Level

**Passive:** An eldritch poisoner gains a +2 bonus on Craft (alchemy) checks to create poisons and
antitoxins, and creates them in half the normal amount of time.

**Replaces:** Throw Anything

**Sneak Attack (Ex)**

**Ability:** At 1st level, the eldritch poisoner gains a [sneak attack](ref/ability/sneak-attack)
identical to the rogue class feature, dealing 1d6 points of sneak attack damage.

**At 12th Level:** The damage becomes 4d6.

**At 16th Level:** The damage becomes 5d6.

**At 20th Level:** The damage becomes 6d6.

**At 4th Level:** The damage becomes 2d6.

**At 8th Level:** The damage becomes 3d6.

**Gained:** At 1st Level

**Replaces:** Mutagen, persistent mutagen

**Discoveries**

**Gained:** At 1st Level

**Passive:** An eldritch poisoner can select any of the following eleven discoveries, in addition to
those available to other alchemists.

**Special:** Arcanotoxin discoveries with a save DC use her arcanotoxin's save DC.

**Antidote (Su)**

**Ability:** The eldritch poisoner can sacrifice one use of her arcanotoxin to create an extract of
[delay poison](ref/spell/delay-poison) which she can feed to an adjacent, willing creature as a
**standard action**.

**At 10th Level:** She can instead use this ability to create an extract of
[neutralize poison](ref/spell/neutralize-poison).

**Apothecary (Ex, Sp)**

**Passive:** She gains bonus equal to [half](ref/misc/fractions-and-rounding) her alchemist level on
Heal checks to identify or treat poisons and to the bonus she grants when successfully treating a
poison.

**Standard:** The eldritch poisoner can use [detect poison](ref/spell/detect-poison) at will as a
[spell-like ability](ref/umr/spell-like-abilities).

**Combine Toxins (Ex)**

**Passive:** An eldritch poisoner can diversify her arcanotoxin, dealing damage to any two ability
scores with a single dose. The alchemist must already know how to target both ability scores with
her arcanotoxin. A combined toxin reduces the damage die of its arcanotoxin by one step, to a
minimum of 1 point of ability damage to each ability score.

**Contact Toxin (Su)**

**Passive:** The eldritch poisoner can create her arcanotoxin as a contact poison. A vial of contact
arcanotoxin can be thrown up to 30 feet as a ranged touch attack or smeared onto a surface as a
**standard action**, but it becomes inert after 1 minute. The arcanotoxin's save DC is reduced by 2.

**Prereq:** 4th-level alchemist

**Envenom (Su**

**Move:** The eldritch poisoner can create and apply her arcanotoxin to a held weapon (her own or an
ally's). The toxin lasts 1 minute or until used.

**Lethal Toxin (Su)**

**Ability:** The eldritch poisoner's arcanotoxin can deal Constitution damage.

**Prereq:** 10th-level alchemist

**Mind-Altering Toxin (Su)**

**At 10th Level:** Targets become [confused](ref/misc/confused) instead.

**Passive:** Whenever a creature fails its saving throw against the eldritch poisoner's arcanotoxin,
it also becomes [dazzled](ref/misc/dazzled) by hallucinations for the toxin's duration as a
secondary effect.

**Prereq:** 6th-level alchemist

**Paralytic Toxin (Su)**

**At 15th Level:** The target becomes [paralyzed](ref/rule/paralyzed) instead.

**Passive:** Whenever a creature fails its saving throw against the eldritch poisoner's arcanotoxin,
it also becomes [staggered](ref/misc/staggered) for the toxin's duration as a secondary effect.

**Prereq:** 8th-level alchemist

**Sickening Toxin (Su)**

**At 12th Level:** When the alchemist reaches 12th level, targets become
[nauseated](ref/misc/nauseated) instead.

**Passive:** When a creature fails its save against the eldritch poisoner's arcanotoxin, it also
becomes [sickened](ref/misc/sickened) for the toxin's duration as a secondary effect.

**Tailored Toxin (Ex)**

**Ability:** Choose one creature type (and subtype, for humanoids or outsiders). The eldritch
poisoner's arcanotoxin is particularly effective against such creatures, increasing the save DC
by 2.

**Special:** This discovery can be selected more than once; each time it applies to a different
creature type (or subtype).

**Toxic Fumes (Ex)**

**Ability:** The eldritch poisoner can create her arcanotoxin as an inhaled poison. She can throw a
vial of arcanotoxin up to 30 feet as a ranged touch attack, affecting all creatures in a
10-foot-by-10-foot square. The arcanotoxin's save DC is reduced by 4, its duration is halved, and a
successful save immediately ends the inhaled arcanotoxin's effect.

**Prereq:** 6th-level alchemist

**Careful Injection (Ex)**

**Gained:** At 4th Level

**Passive:** An eldritch poisoner can forgo some of her sneak attack damage in order to increase the
save DC of a poison or arcanotoxin on the weapon used to make the sneak attack. The poison's DC
increases by 1 for every 1d6 points of sneak attack damage forgone.

**Replaces:** The discovery gained at 4th level
