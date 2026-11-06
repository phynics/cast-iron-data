+++
id = "ref/arc-vigilante/hangman"
kind = "archetype"
title = "Hangman"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hangman", path = "json/archetypes_vigilante.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/vigilante" },
]

[fields]
kind = "none"
+++

**Sources:** Horror Adventures pg 70\
Wherever the guilty walk free, the hangman brings judgment.

**Weapon and Armor Proficiency**

**Alters:** Weapon and armor proficiencies

**Info:** A hangman is proficient with [nets](ref/eq-weapon/net) and [whips](ref/eq-weapon/whip),
but not shields.

**Vigilante Specialization**

**Alters:** Vigilante specialization

**Info:** A hangman must choose the _stalker_ specialization.

**Hangman's Noose (Ex)**

**Ability:** A hangman can wield a rope noose as a net or whip, and also can use it to
[grapple](ref/rule/grapple), gaining the benefits of [Improved Grapple](ref/feat/improved-grapple)
with it. He takes no penalty on combat maneuver checks with the noose for having the noose in his
hand, but he still doesn't add any bonuses he might have with a net or whip (such as weapon
enhancement bonuses or benefits from [Weapon Focus](ref/feat/weapon-focus)) on the check.

**Gained:** At 2nd Level

**Replaces:** 2nd-level vigilante talent

**Special:** He can spend 1 minute to weave a magical or masterwork net or whip into a noose,
thereafter gaining these benefits with it.

**Bound to Truth (Ex, Sp)**

**Ability:** A hangman adds half his vigilante level to his Sense Motive checks to notice lies told
by a creature entangled or grappled by his noose, by feeling the creature's throat clench or changes
in its breathing.

**Ability2:** In addition, he can prevent a creature entangled or grappled in his noose from lying
by tightening the noose, as per a single-target [zone of truth](ref/spell/zone-of-truth) (the caster
level equals his vigilante level; the save DC is Charisma-based). He can use the latter ability a
number of rounds per day equal to [half](ref/misc/fractions-and-rounding) his vigilante level. These
rounds don't need to be consecutive.

**Gained:** At 3rd Level

**Replaces:** Unshakable

**Twisted Rope (Su)**

**Ability:** A hangman can spend 1 hour preparing his noose, granting it temporary hit points equal
to his vigilante level, giving it a [hardness](ref/rule/breaking-things) equal to 1/2 his vigilante
level plus double the weapon's enhancement bonus (or its current [hardness](ref/umr/hardness),
whichever is better), and changing its break DC to 23 + 1/2 his vigilante level (or its current
break DC, whichever is better). These benefits last for 8 hours, but end immediately if the hangman
prepares another noose.

**Gained:** At 4th Level

**Replaces:** 4th-level vigilante talent

**Chokehold**

**Ability:** A hangman gains [Chokehold](ref/feat/chokehold) as a bonus feat.

**Gained:** At 5th Level

**Replaces:** Startling appearance

**Tighten the Noose (Ex)**

**Gained:** At 11th Level

**Replaces:** Frightening appearance

**Swift:** While a hangman is grappling a target with his noose, he can deal increased _hidden
strike_ damage to the target.

**Suffocation (Ex)**

**Ability:** The first time the hangman succeeds at a check to maintain a grapple (on his next turn
after establishing the grapple), in place of the other options, he can suffocate the target and
cause her to fall [unconscious](ref/misc/unconscious). A successful Fortitude save (DC = 15 + the
hangman's Strength bonus) negates the suffocation. On subsequent rounds, the hangman can maintain
the grapple to suffocate the target again. On the next failed save, the target drops to -1 hit
points and starts [dying](ref/misc/dying). On the third failed save, she dies. Even if the hangman
has the ability to maintain a grapple with less than a standard action, he can attempt to maintain a
grapple to suffocate only once per round.

**Gained:** At 17th Level

**Replaces:** Stunning appearance
