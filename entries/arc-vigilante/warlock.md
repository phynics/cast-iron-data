+++
id = "ref/arc-vigilante/warlock"
kind = "archetype"
title = "Warlock"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "warlock", path = "json/archetypes_vigilante.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/vigilante" },
]

[fields]
kind = "archetype"
replaces = ["4th-", "8th-", "10th-", "14th-", "and 16th-level vigilante talents", "Vigilante specialization", "Unshakable"]
alters = ["Skill ranks per level", "Armor proficiencies", "Vigilante talents"]
+++

**Sources:** Ultimate Intrigue pg 60\
Practicing magic in secret, the warlock obscures her arcane scholarship from public view. Her study
of these arts allows her to hide her dual nature and enchant her enemies - or simply blast them with
furious magical attacks.

**Gained class skills:** ka, spc

**Lost class skills:** dd, ke, per, sur

**Skill Ranks per Level**

**Alters:** Skill ranks per level

**Info:** The warlock gains a number of skill ranks equal to 4 + her Intelligence modifier at each
level, instead of 6 + her Intelligence modifier skill ranks.

**Armor Proficiencies**

**Ability:** A warlock is not proficient with medium armor. Like a [magus](ref/class/magus), she can
cast her spells while wearing light armor without incurring the normal arcane spell failure chance.

**Alters:** Armor proficiencies

**Spellcasting**

**Ability:** A warlock casts arcane spells and cantrips as a magus. She prepares spells using a
spellbook, choosing them from the 6th-level and lower spells from the sorcerer/wizard spell list;
higher-level sorcerer/wizard spells are not on the warlock's spell list.

**Replaces:** 4th-, 8th-, 10th-, 14th-, and 16th-level vigilante talents

**Spellbook**

**Ability:** A warlock has a spellbook that functions in the same way as a magus's spellbook but
uses the 6th-level and lower spells from the sorcerer/wizard spell list.

**Mystic Bolts (Su)**

**Ability:** A warlock can sling projectiles of magical energy at will by shooting a bolt or
touching her foe. A melee mystic bolt requires the target to be within reach, and a ranged mystic
bolt is a ranged attack with a range of 30 feet. A mystic bolt deals points of damage equal to
1d6+[one-fourth](ref/misc/fractions-and-rounding) of her vigilante level.

**At 7th Level:** Each time she creates a mystic bolt, she can have it use any one of the damage
types she has selected.

**Info:** The warlock must choose one type of damage for her mystic bolt: acid, cold, electricity,
or fire. Attacking with a mystic bolt takes the place of one of the warlock's normal attacks, and
she can make a full attack using mystic bolts. The warlock vigilante attacks with mystic bolts as
though they were light one-handed weapons, and the bolts can be used for
[two-weapon fighting](ref/rule/two-weapon-fighting) (with each hand creating one mystic bolt) and
feats and abilities that apply to weapon attacks (unless they're excluded from that feat, such as
with [Power Attack](ref/feat/power-attack)). [Weapon Focus](ref/feat/weapon-focus) (ray) doesn't
apply to mystic bolts, but a warlock can take Weapon Focus (mystic bolt) and apply it to both melee
and ranged mystic bolts.

Creating a mystic bolt requires the hand to be free, but the bolt appears only briefly, so a warlock
using mystic bolts has a free hand any time she isn't attacking with a mystic bolt. The warlock
threatens with a mystic bolt, but only if she has a hand free.

**Repeat:** The warlock chooses another damage type from the list above., 7, 6

**Replaces:** Vigilante specialization

**Special:** Because mystic bolts are impermanent, a spell that targets a single weapon (like
[magic weapon](ref/spell/magic-weapon)) can't affect it, nor can a mystic bolt be made with magic
weapon special abilities. Abilities that affect all weapon attacks the warlock makes, such as the
_arcane striker_ warlock talent, function with mystic bolts.

**Piercing Bolts (Ex)**

**At 3rd Level:** The warlock can choose one mystic bolt per round to be a touch attack. This turns
a melee mystic bolt into a melee touch attack or a ranged mystic bolt into a ranged touch attack.

**At 5th Level:** The warlock can treat all of her mystic bolts as touch attacks.

**Replaces:** Unshakable

**Warlock Talents**

**Alters:** Vigilante talents

**Info:** A warlock can select from any of the following vigilante talents, in addition to general
vigilante talents.

**Arcane Striker (Su)**

**Ability:** The warlock gains [Arcane Strike](ref/feat/arcane-strike) as a bonus feat.

**At 12th Level:** When she activates Arcane Strike, she can choose to also give her weapons the
[flaming](ref/magic-enh/flaming), [frost](ref/magic-enh/frost), [shock](ref/magic-enh/shock), or
[thundering](ref/magic-enh/thundering) weapon special ability. She makes this choice each time she
activates Arcane Strike, and it lasts for the same duration.

**At 16th Level:** She adds [anarchic](ref/magic-enh/anarchic),
[axiomatic](ref/magic-enh/axiomatic), [flaming burst](ref/magic-enh/flaming-burst),
[holy](ref/magic-enh/holy), [icy burst](ref/magic-enh/icy-burst),
[shocking burst](ref/magic-enh/shocking-burst), and [unholy](ref/magic-enh/unholy) to the list of
special abilities she can select. She can choose to apply an alignment-based weapon special ability
only while in her vigilante identity, and only if it matches the alignment of her vigilante
identity.

**Elemental Armor (Su)**

**At 12th Level:** The damage increases to 2d6 points.

**At 16th Level:** The warlock becomes immune to the chosen damage type while in her vigilante
identity.

**At 4th Level:** The warlock's armor deals 1d6 points of damage of the chosen energy type to any
creature striking the warlock with a natural weapon or a non-reach melee weapon. A creature that
attempts a [grapple](ref/rule/grapple) combat maneuver check against the warlock also takes this
damage. A creature can take damage in this way no more than once per round.

**At 8th Level:** The energy resistance increases to 10.

**Passive:** When in her vigilante identity, the warlock gains armor made of elemental energy. She
is surrounded by a nimbus of ice, lightning, or flames, granting her resistance 5 to cold,
electricity, or fire, respectively. The damage type must be chosen when she selects this talent, and
it can't be changed.

**Familiar (Ex)**

**Ability:** The warlock gains a [familiar](ref/sidekick/familiar), using her vigilante level as her
effective wizard level. The [familiar](ref/ability/familiars) also has a social identity as a
seemingly normal animal, though warlocks with outlandish familiars might still need to hide them.

**Social Simulacrum (Sp)**

**Ability:** The warlock can create a short-lived simulacrum (as
[lesser simulacrum](ref/spell/simulacrum-lesser)) that duplicates her social identity, allowing her
to appear to be in two places at once. Creating the duplicate takes 1 hour and requires no material
component cost. It lasts for 4 hours before turning back into an inert pile of snow.

The duplicate replicates only the warlock's social identity, with the same alignment and social
talents. It has no magical abilities, and can't assume a vigilante identity. As with the spell, the
simulacrum isn't under the warlock's control.

**Prereq:** 8th-level vigilante

**Special:** The warlock can create a social simulacrum no more than once per day and can have only
one in existence at a time.

**Tattoo Chamber (Su)**

**Ability:** The warlock can magically absorb items through a tattoo on his hand or wrist and easily
retrieve them or activate their magical abilities without making them manifest. The items seemingly
disappear into the tattoo, but actually enter an extradimensional space that the warlock can access
via the tattoo. Stowing an item in this way requires a **full-round action**, and the space can
store a number of items equal to 1 + [one-third](ref/misc/fractions-and-rounding) of his vigilante
level. These items must be items the warlock can hold in one hand.

**Ability2:** Retrieving a stowed item requires mentally activating the tattoo as a **swift
action**. The item appears in the warlock's hand, so worn items must still be donned to gain their
benefits.

**Flavor:** This talent functions as the [cabalist](ref/arc-vigilante/cabalist) ability of the same
name. The text below is from that ability.

**Special:** The warlock can also activate any [spell-trigger](ref/misc/spell-trigger) abilities of
a stored item as though he were wielding the item, producing the magic effect from his tattoo rather
than from the item. If the warlock dies while items are within his tattoo chamber, those items fade
into existence within 5 feet of the corpse.
