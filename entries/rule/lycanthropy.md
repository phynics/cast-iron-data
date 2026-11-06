+++
id = "ref/rule/lycanthropy"
kind = "rule"
title = "Lycanthropy"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lycanthropy", path = "json/rules_campaign_types02.json" },
]

[fields]
kind = "none"
+++

**Sources:** Horror Adventures pg. 28-29\
There is a sound pulsing through your blood, a call to the wild and savage places of the world,
where you are free to hunt and to kill to satisfy your bloodlust. You are filled with the desire to
rend foes limb from limb with tooth and claw.

### Catalyst

Lycanthropy is contracted from being savagely wounded by the teeth or claws of a lycanthrope,
typically when reduced to less than 10% of your maximum hit points in a single combat with one.
(This can vary with the power of the creature.) When you contract this corruption, note the animal
associated with the lycanthrope, as that is the kind if lycanthrope you will become.

### Progression

Lycanthropy's progress is tied to the phases of the moon. Each month, the moon is considered full
for three nights. At the onset of the corruption, you must attempt a Will saving throw during one of
the nights chosen by the GM. For each stage of lycanthropy corruption you have, you must attempt a
save on one additional night, eventually needing to save on nights leading up to and possibly after
the full moon. The DC of this save is equal to 15 + your manifestation level. If you fail a save,
you don't need to attempt more until the next full moon.

Failing a saving throw against this corruption causes you to black out, losing control of your
character. During this time, your form becomes that of the associated creature and you give into
your animalistic urges, hunting and killing with abandon. The next morning, you regain control,
typically in the wilderness without any gear and soaked in blood. If you fail the save but your
inner animal is prevented from running free, perhaps because you were restrained, you transform and
attempt to run free without a save on the remaining full moon nights, and you also go out of control
any time you shift forms during the days of that full moon. If you last through it and remain
restrained, your corruption doesn't progress to the next stage. However, the DC of the Will save
against your corruption progressing increases by 2. These increases stack each time this occurs, and
they last until your corruption reaches the next stage.

**Corruption Stage 1**

**Details:** The first time you lose control, you kill defenseless small animals, such as birds,
rodents, and possibly even a dog.

**Corruption Stage 2**

**Details:** The second time this occurs, you kill larger animals, such as a horse, a cow, or a pig.

**Corruption Stage 3**

**Details:** The third time this happens, you kill a nearby sentient humanoid, at which point the
corruption becomes incurable and you are doomed to live a life of lycanthropy, forever turning evil
and becoming an NPC under the GM's control.

### Removing the Corruption

Removing lycanthropy requires you to slay the source of your corruption and, at the height of the
next full moon, consume 1 dose of [belladonna](ref/eq-poison/belladonna) per 2 manifestation levels
you have all at once. You must choose to fail the initial saving throw against the belladonna.

### Manifestations

The following are manifestations of the lycanthropy corruption.

**Animalistic Health**

**Flavor:** You are hardier in your animal form.

**Prereq:** Shift form

**Gift:** Whenever you _shift forms,_ you gain a +2 bonus to your Constitution score that lasts as
long as you are in your _shifted form._ Hit points gained from this bonus are lost when you revert
to your normal form.

**Stain:** You take a -2 penalty to your Charisma score.

**Animalistic Might**

**Flavor:** You are stronger in your animal form.

**Prereq:** Shift form

**Gift:** Whenever you _shift forms,_ you gain a +2 bonus to your Strength score that lasts as long
as you're in your _shifted form._

**Stain:** Whenever you _shift form_ involuntarily, your body spasms and changes size, causing you
to drop whatever you were holding and burst out of your other gear and clothing. Items that can stay
on throughout this size change might not fall off, at the GM's discretion.

**Feral Senses**

**Flavor:** You gain the senses of your animalistic side.

**Gift:** You gain [low-light vision](ref/rule/low-light-vision).

At manifestation level 3rd, you gain the [scent](ref/umr/scent) special ability if your lycanthrope
animal type has the scent ability.

**Stain:** Creatures of the animal type (except those of your lycanthrope type) are unnerved by your
lycanthropic presence, causing you to take a -2 penalty on Handle Animal and Ride skill checks.

At manifestation level 3rd, these penalties change to -4.

**Fur Armor**

**Flavor:** When in your _shifted form,_ you gain a thick coat of fur.

**Prereq:** Shift form

**Gift:** Whenever you _shift_ your form, your natural armor bonus increases by 1.

At manifestation level 5th, your natural armor bonus instead increases by 2.

**Stain:** Whenever you _shift form_ involuntarily, you _shift_ as a **free action** but you spend
your next round [confused](ref/misc/confused) and must roll to determine your action.

At manifestation level 5th, you are confused for 2 rounds instead. Immunities don't prevent this
confusion, and you can't remove the confusion early by any means.

**Greater Shift Form**

**Flavor:** You can become an animal.

**Prereq:** Manifestation level 6th, shift form

**Gift:** When you use _shift form,_ you can instead take your animal form, as if using
[polymorph](ref/spell/polymorph). Nonmagical clothing and gear don't meld into your animal form. You
don't gain any ability score adjustments (other than those gained from other manifestations), but
you do gain all of the other abilities granted by _[polymorph](ref/spell/polymorph)_ for your new
form.

**Stain:** While you're _shifted,_ you're treated as a lycanthrope and shapeshifter for abilities,
items, or spells that target lycanthropes or shapeshifters. In addition, when you _shift_
involuntarily, you can't _shift_ back until you spend a **full-round action** and succeed at a DC 20
Constitution check. If you don't succeed, you remain in your _shifted_ form, automatically consuming
a daily use of shifting each minute until you have used up all of your uses for the day.

**Lunar Call**

**Flavor:** The moon's light affects your mind.

**Prereq:** Shift form

**Gift:** Whenever you are outside and the moon is visible, you gain a +1 morale bonus on attack
rolls and damage rolls. These bonuses double during a full moon.

**Stain:** Whenever you are outside and the moon is visible, you take a -2 penalty on saving throws
against emotion effects and a -4 penalty on saving throws to resist involuntarily shifting. These
penalties double during a full moon.

**Lycanthropic Empathy**

**Flavor:** You can relate to the creatures that share your type.

**Gift:** You can communicate with animals related to your animal type. You can use
[Diplomacy](ref/skill/diplomacy) to alter such animals' attitudes, and you gain a +4 racial bonus on
such checks. This bonus also applies on your _wild empathy_ checks.

**Stain:** Your animalistic nature imposes a penalty on your [Bluff](ref/skill/bluff), Diplomacy,
and [Sense Motive](ref/skill/sense-motive) skill checks equal to your manifestation level (minimum
-2) when dealing with humanoids (and other civilized folk at the GM's discretion).

**Shift Form**

**Flavor:** You have some control over your shift to a feral nature.

**Special:** Upon receiving this manifestation, you must take both the gift and the stain, even with
the _useful corruption_ or _vile corruption_ [variants](ref/rule/corruption-variants).

**Gift:** You can attempt a DC 15 Constitution check as a **full-round action** to shift into a
feral form, with a bonus equal to your manifestation level. This form grants you a bite
[natural attack](ref/umr/natural-attacks) that deals 1d6 points of piercing damage if you're Medium
(1d4 if Small). You retain the use of your abilities and gear.

You can remain in this form for up to 1 minute, but can revert back as a **move action** at any
time. If the duration expires, you can extend it by 1 minute by spending another use of this ability
as a **free action**. You can use this ability a number of times per day equal to your manifestation
level.

**Stain:** When you are struck by a confirmed critical hit and aren't in your _shifted form,_ you
must attempt a Will save (DC = 15 + your manifestation level). If you fail, you automatically _shift
form_ on your next turn without attempting a check. This consumes one use of that ability. You must
also attempt this save if you take damage equal to or greater than your manifestation level while
not in combat or before you've acted in combat.

**Silver Allergy**

**Flavor:** You're resistant to harm, but can't abide the touch of silver.

**Prereq:** Manifestation level 4th, shift form

**Gift:** When you are _shifted,_ you gain an amount of
[damage reduction](ref/rule/damage-reduction) equal to half your manifestation level. This DR is
overcome by silver.

**Stain:** When you're not in your _shifted form_ and you touch silver, including being struck by a
silver weapon, you're [sickened](ref/misc/sickened) for 1 round. Immunities don't prevent this
sickened condition, and you can't remove it early. You can try to hide this aversion with a Bluff
check opposed by Sense Motive.
