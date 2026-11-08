+++
id = "ref/arc-spiritualist/ward-spiritualist"
kind = "archetype"
title = "Ward Spiritualist"
source_ids = ["wilderness-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ward_spiritualist", path = "json/archetypes_spiritualist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/spiritualist" },
]

[fields]
kind = "archetype"
replaces = ["Bonded senses", "phantom recall", "greater spiritual interference"]
alters = ["Phantom", "Spellcasting"]
+++

**Sources:** Wilderness Origins pg 18\
While many spiritualists are bound to a departed spirit, a condition more likely to be the result of
chance or tragedy than a career choice, there are some individuals who seek out this life. A ward
spiritualist ventures into the wilderness and petitions a [kami](ref/family/kami) to help her in her
travels, either taking an existing ward with her or becoming the kami's new ward.

**Kami Phantom (Su)**

**Alters:** Phantom

**Info:** The ward spiritualist's phantom is less powerful than most, but it has an innate
connection to its ward. The ward spiritualist's phantom is a kami phantom, functioning as normal for
a [phantom](ref/sidekick/phantom), except that its base attack bonus is equal to three-quarters its
Hit Dice (as a [rogue](ref/class/rogue)) and its Hit Dice are d8s instead of d10s. Additionally, a
kami phantom cannot manifest as incorporeal, only ectoplasmic.

**Ward Implement (Su)**

**Action:** Ability

**Alters:** Spellcasting

**Repeat At:** She gains a focus power for her implement school., 2, 6, 10

**Replaces:** Bonded senses, phantom recall, greater spiritual interference

**Special:** She must meet the prerequisites of these focus powers, treating her spiritualist level
as her occultist level for focus power prerequisites. She also treats her spiritualist level as her
occultist level for feat prerequisites.

The ward spiritualist gains a single implement school of her choice, as an
[occultist](ref/class/occultist), along with its resonant focus power and base focus power. The ward
spiritualist does not gain additional spells from her ward implement, and it always starts each day
with mental focus invested equal to half her class level (minimum 1).

When she gains her ward implement, the ward spiritualist must choose either to have a physical
implement or to be the implement herself. If she chooses to have a physical implement, her
spiritualist spells include it as a focus component, and she can change what item is her implement
when she regains her spells at the start of each day. Her implement must be an item that can be held
in one hand, and it cannot be a manufactured weapon. If the ward spiritualist chooses to be her own
ward implement, her spiritualist spells always have a somatic component in addition to their other
components; this component does not become an emotion component.

She can remove the focus or somatic component of her spells, but this requires a
[concentration](ref/rule/concentration) check with a DC equal to 15 + twice the spell level, which
is increased for a thought component as normal.

**Merged Manifestation (Su)**

**Ability:** The ward spiritualist learns how to merge her kami phantom with her ward implement.
This functions as _bonded manifestation,_ except that she does not choose ectoplasmic or
incorporeal. Instead, she gains different benefits depending on whether she has a physical implement
or is her own implement.

**Gained:** At 3rd Level

**Physical Implement**

**Ability:** If she has a physical implement, when using her _merged manifestation,_ her implement
functions as a one-handed [improvised weapon](ref/misc/improvised-weapons) of appropriate size, and
she does not take the usual penalties associated with wielding an improvised weapon. Additionally,
it is considered to have a +1 enhancement bonus for the duration of the _merged manifestation._

**At 13th Level:** Her implement also gains the benefits of
[spirit-bound blade](ref/spell/spirit-bound-blade) for the duration of the _merged manifestation._

**At 18th Level:** It now deals damage as a weapon two size categories larger.

**At 8th Level:** It deals damage as a weapon
[one size category larger](ref/misc/damage-die-adjustments).

At 8th level: The enchantment bonus +2.

At 13th level: The enchantment bonus +3.

At 18th level: The enchantment bonus +4.

**Is Her Own Implement**

**Ability:** If she is her own implement, when using her _merged manifestation,_ she gains the
_unarmed strike_ class feature as a 1st level [unchained monk](ref/class/unchained-monk).

**At 13th Level:** Her unarmed damage is that of an 8th-level unchained monk, and her unarmed
strikes gain the benefits of _[spirit-bound blade](ref/spell/spirit-bound-blade)_ for the duration
of the _merged manifestation._

**At 18th Level:** Her unarmed damage is that of a 12th level unchained monk, and she can use
_flurry of blows_ as an 11th-level unchained monk.

**At 8th Level:** Her unarmed strike damage is that of a 4th-level unchained monk, and she gains
_flurry of blows_ as a 1st-level unchained monk.

**Unarmed Strike (Ex)**

**Action:** Ability

**Flavor:** Text from the unchained monk class ability.

**At 1st Level:** Your unarmed strike deals 1d4 (Small), 1d6 (Medium), or 1d8 (Large) damage.

**At 12th Level:** Your unarmed strike now deals 1d10 (Small), 2d6 (Medium), or 3d6 (Large) damage.

**At 16th Level:** Your unarmed strike now deals 2d6 (Small), 2d8 (Medium), or 3d8 (Large) damage.

**At 20th Level:** Your unarmed strike now deals 2d8 (Small), 2d10 (Medium), or 4d8 (Large) damage.

**At 4th Level:** Your unarmed strike now deals 1d6 (Small), 1d8 (Medium), or 2d6 (Large) damage.

**At 8th Level:** Your unarmed strike now deals 1d8 (Small), 1d10 (Medium), or 2d8 (Large) damage.

**Special:** Your unarmed strike is treated as both a manufactured weapon and a natural weapon for
the purpose of spells and effects that enhance or improve either manufactured weapons or natural
weapons.

You gain [Improved Unarmed Strike](ref/feat/improved-unarmed-strike) as a bonus feat. Your attacks
can be with fists, elbows, knees, and feet. This means that you can make unarmed strikes with your
hands full. There is no such thing as an off-hand attack when you're striking unarmed. You can apply
your full Strength bonus on damage rolls for all your unarmed strikes. Your unarmed strikes deal
lethal damage, although you can choose to deal nonlethal damage with no penalty on the attack roll.
You can make this choice while grappling as well.

**Flurry of Blows (Ex)**

**Flavor:** Text from the unchained monk class ability.

**Fullround:** You can make a flurry of blows as a full-attack action. When doing this, you can make
one additional attack at your highest base attack bonus. This additional attack stacks with the
bonus attacks from [haste](ref/spell/haste) and other similar effects. When using this ability, you
can make these attacks with any combination of your unarmed strikes and weapons that have the monk
special weapon quality. You take no penalty for using multiple weapons when making a flurry of
blows, but you do not gain any additional attacks beyond what's already granted by the flurry for
doing so. (You can still gain additional attacks from a high base attack bonus, from this ability,
and from _[haste](ref/spell/haste)_ and similar effects).

**At 11th Level:** You can now make two additional attacks at your highest base attack bonus during
your flurry of blows. This still stacks with _[haste](ref/spell/haste)_ and similar effects.
