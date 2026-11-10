+++
id = "ref/arc-shifter/oozemorph"
kind = "archetype"
title = "Oozemorph"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "oozemorph", path = "json/archetypes_shifter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shifter" },
]

[fields]
kind = "archetype"
replaces = ["Weapon and armor proficiencies", "Chimeric aspect", "greater chimeric aspect", "wild shape", "shifter aspect", "Shifter claws", "Defensive instinct", "Woodland stride"]
alters = ["Wild empathy"]
replaces_features = ["weapon-and-armor-proficiencies", "chimeric-aspect", "greater-chimeric-aspect", "wild-shape", "shifter-aspect", "shifter-claws", "defensive-instinct", "woodland-stride"]
alters_features = ["wild-empathy"]
+++

**Source** Ultimate Wilderness pg. 81, official Paizo FAQ\
While most shifters are trained in druidic traditions that allow them to tap into animalistic
powers, others look instead to the simplest forms of life for inspiration. Known as oozemorphs,
these shifters focus on the ooze - a form of life as simple in construction as it is dangerous in
combat. While some shifters consider the oozemorph to be unsettling or even vile, these shifters
merely embrace a stranger form of life than most. They are not inherently evil, yet they are often
misunderstood by druidic circles and these circles' shifter champions.

**Weapon and Armor Proficiency**

**Info:** An oozemorph is proficient with all simple weapons and light armor.

**Replaces:** Weapon and armor proficiencies

**Compression (Ex)**

**Ability:** An oozemorph gains [compression](ref/umr/compression) as per the universal monster
rule. This ability can be used regardless of the current form the oozemorph has taken.

**Fluidic Body (Su)**

**At 15th Level:** She can treat this ability as [beast shape II](ref/spell/beast-shape-2) or
[giant form I](ref/spell/giant-form-1).

**At 8th Level:** The oozemorph can treat this ability as [beast shape I](ref/spell/beast-shape-1)

**Info:** An oozemorph's base form is not that of her race but rather that of a protoplasmic blob
that has the same volume and weight. An oozemorph treats her creature type as both
[ooze](ref/type/ooze) and her base creature type from her race for the purposes of effects targeting
creatures by type (such as [bane](ref/magic-enh/bane) weapons and a ranger's
[favored enemy](ref/ability/favored-enemy)). In this form, the oozemorph is immune to critical hits
and precision damage and can't be flanked. However, she has no magic item slots and she cannot
benefit from armor; cast spells; hold objects; speak; or use any magic item that requires
activation, is held, or is worn on the body. An oozemorph reverts to this formless state whenever
she is unconscious or in an area of antimagic. This is treated as a polymorph effect.

**Move:** An oozemorph can assume a humanoid form. This transformation is identical to
[alter self](ref/spell/alter-self), except for the base duration. Each hour after this duration, the
oozemorph must succeed at a DC 15 Fortitude save or revert back to her fluidic body until she rests
for at least 8 hours. This save DC increases by 1 for each additional hour spent maintaining the
form. Ending this transformation at any time reverts the oozemorph back to her ooze form and renders
her [fatigued](ref/misc/fatigued) for a number of minutes equal to the number of hours she
maintained the form.

**Replaces:** Chimeric aspect, greater chimeric aspect, wild shape, shifter aspect

**Special:** _Fluidic Body_ is essentially two effects in one. The first, which is a permanent part
of your character once you become an oozemorph, is that your base form is now an ooze shape. Even if
you lose fluidic body for some reason ([antimagic field](ref/spell/antimagic-field), violating your
code of conduct, etc) your base form is still the amorphous ooze-like form. The other half of the
ability is a supernatural [polymorph](ref/spelldef/polymorph) effect to transform into humanoid (and
later bestial) forms.

Despite having an ooze-like shape, an oozemorph's base form is not an ooze, though it does also
count as an ooze for the purposes of effects targeting creatures by type. The ooze-like form doesn't
gain any abilities of the ooze creature type except as stated by the archetype itself. This form
retains the base senses and land speed of the oozemorph's original race, as well as racial abilities
like [dwarfs'](ref/race/dwarf) _greed_ or [gnomes'](ref/race/gnome) _obsession_ that don't depend on
shape, but it loses abilities dependent on form, including form-based speeds like
[strix's](ref/race/strix) flight (and most other racial speeds beyond land speed), racial natural
attacks like [catfolks'](ref/race/catfolk) claws, and other abilities like
[tieflings'](ref/race/tiefling) prehensile tail. However, if the oozemorph possesses a racial
ability denied her in her ooze-like form and transforms into a member of her own race with fluidic
body, she gains the full benefits of that racial ability for that duration, even if it isn't usually
granted when using _[alter self](ref/spell/alter-self)_ (or the appropriate spell for a non-humanoid
oozemorph). An oozemorph's compression, [damage reduction](ref/rule/damage-reduction), and morphic
weaponry function in its ooze-like form and any form it takes via fluidic body, though not in forms
it takes via other polymorph effects.

An oozemorph can carry items floating in its mass that are considered to be attuned. When it turns
into a humanoid form via fluidic body, it can equip any number of those items (even armor, which
usually takes time to don), leaving the rest on the ground in its space. If it turns into an animal
via fluidic form, the items meld into the new form and grant some passive benefits, as normal for
polymorph effects.

**Usage:** 1 time/day per 2 shifter levels (minimum 1)

**Morphic Weaponry (Ex)**

**Flavor:** An oozemorph can create a number of natural weapons to fight with from any portion of
her body, regardless of her current form.

**Gained:** At 1st Level

**Move:** An oozemorph can form two primary natural attacks that each deal 1d6 points of
bludgeoning, piercing, or slashing damage, chosen by the oozemorph when she forms them.

**Repeat:** An oozemorph gains an additional primary natural attack., 6, 9

**Replaces:** Shifter claws

**Special:** The total number of natural attacks an oozemorph has at any given time includes those
gained via her current form. For example, an 8th-level oozemorph who has taken the form of a wolf
with _[beast shape I](ref/spell/beast-shape-1)_ has a bite attack as part of that form; she can
create only two additional natural attacks via _morphic weaponry,_ for a total of three attacks
available to her at that level. If the oozemorph later reverts to a humanoid form with no natural
weapons, she can instead create three _morphic weapons._

**Swift:** An oozemorph can change the damage type of any number of her natural weapons.

**Ooze Empathy (Ex)**

**Ability:** An oozemorph gains the shifter's _wild empathy_ class feature, but she can use it only
to influence the attitude of oozes with an Intelligence score of 2 or lower. An oozemorph can use
this ability on mindless oozes; when she does so, she imparts a modicum of intellect to the ooze to
allow it to respond to her commands.

**Alters:** Wild empathy

**Damage Reduction (Ex)**

**Gained:** At 2nd Level

**Passive:** An oozemorph gains DR 4/slashing while unencumbered and either wearing no armor or
wearing light nonmetal armor.

**Replaces:** Defensive instinct

At 4th level: This [damage reduction](ref/rule/damage-reduction) 6.

At 8th level: This [damage reduction](ref/rule/damage-reduction) 8.

At 12th level: This [damage reduction](ref/rule/damage-reduction) 10.

At 16th level: This [damage reduction](ref/rule/damage-reduction) 12.

At 20th level: This [damage reduction](ref/rule/damage-reduction) 14.

**Clinging Ooze (Ex)**

**Ability:** When in her natural form, an oozemorph gains a climb speed of 10 feet.

**Gained:** At 4th Level

**Replaces:** Woodland stride
