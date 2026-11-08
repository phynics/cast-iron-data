+++
id = "ref/arc-antipaladin/insinuator"
kind = "archetype"
title = "Insinuator"
source_ids = ["agents-of-evil"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "insinuator", path = "json/archetypes_antipaladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/antipaladin" },
]

[fields]
kind = "archetype"
replaces = ["Aura of evil", "Smite good", "Touch of corruption", "Aura of cowardice", "Plague bringer", "Cruelty", "Antipaladin spells", "Aura of despair", "Aura of vengeance", "Aura of sin", "Aura of depravity", "Unholy champion"]
alters = ["Detect good", "Channel negative energy"]
+++

**Sources:** Agents of Evil pg 20\
Between the selfless nobility of paladins and the chaotic menace of antipaladins, there exists a
path of dedicated self-interest. Shunning the ties that bind them to a single deity, insinuators
embrace whatever forces help them achieve their own agenda and glory, borrowing power to emulate
divine warriors.

**Alignment**

**Info:** An insinuator can be lawful evil, neutral evil, or chaotic evil.

**Code of Conduct**

**Info:** An insinuator must always work toward his own self-interest, enrichment, or glory, and
must also abide by the moral strictures of whatever outsider they have chosen to invoke that day
(see invocation below). If the insinuator breaks an invoked outsider's code, he cannot invoke
outsiders of that same alignment until he seeks [atonement](ref/spell/atonement), although outsiders
of other alignments may still heed his call.

**Invocation (Ex)**

**Ability:** At the start of each day, an insinuator can meditate for 10 minutes to contact and
barter with an outsider to empower him for a day. An insinuator can freely invoke an outsider of his
own alignment. He can instead invoke an outsider within one step of his own alignment by succeeding
at a Diplomacy or Knowledge (religion) skill check (DC = 15 + the insinuator's antipaladin level).

**Passive:** While invoking the power of an outsider, the insinuator radiates an alignment aura that
matches that of the outsider's, and becomes vulnerable to alignment-based effects that target that
outsider's alignment (such as _smite evil_ or [chaos hammer](ref/spell/chaos-hammer)). None of an
insinuator's supernatural or spell-like class abilities function unless he has invoked the power of
an outsider, and the alignment of the being invoked may affect how some abilities function.

**Replaces:** Aura of evil

**Detect Balance (Sp)**

**Ability:** At will, an insinuator can detect strong moral leanings. This functions as
[detect evil](ref/spell/detect-evil) or [detect good](ref/spell/detect-good), but does not actually
reveal the target's alignment, only whether the target is neutral (rather than good or evil) and the
relative strength of that aura.

**Alters:** Detect good

**Smite Impudence (Su)**

**Flavor:** An insinuator can beseech the forces empowering him to punish their shared enemies.

**At 10th Level:** The insinuator can smite fourt times a day.

**At 13th Level:** The insinuator can smite five times a day.

**At 17th Level:** The insinuator can smite six times a day.

**At 19th Level:** The insinuator can smite seven times a day.

**At 4th Level:** The insinuator can smite twice a day.

**At 7th Level:** The insinuator can smite three times a day.

**Gained:** At 1st Level

**Replaces:** Smite good

**Special:** The smite effect remains until the target is defeated or the next time the insinuator
rests and regains his uses of this ability.

**Swift:** The insinuator chooses one target within sight to smite. An insinuator cannot use smite
against a target that shares an alignment with the outsider he has invoked for the day. The
insinuator adds his Charisma bonus on his attack rolls and [half](ref/misc/fractions-and-rounding)
his insinuator level on all damage rolls made against the target of his smite. If the target is an
outsider, dragon, or divine spellcaster with an alignment opposed to that of the outsider he has
invoked for the day, the bonus damage on the first successful attack increases to 1 point of damage
per antipaladin level the insinuator has. Regardless of the target, the smite attack automatically
bypasses any [damage reduction](ref/rule/damage-reduction) the creature might possess. In addition,
each time the insinuator declares a smite, he gains a number of
[temporary hit points](ref/rule/temporary-hit-points) equal to his antipaladin level.

**Usage:** Once a day.

**Usage:** Once a day.

**Selfish Healing (Su)**

**Gained:** At 2nd Level

**Replaces:** Touch of corruption

**Swift:** An insinuator can heal his wounds by touch. This is treated exactly like the paladin's
[lay on hands](ref/ability/lay-on-hands) class feature, except it can be used only to heal the
insinuator and cannot be used on other creatures.

**Aura of Ego (Su)**

**Gained:** At 3rd Level

**Passive:** An insinuator radiates an aura that bolsters allies and deters enemies. Each ally
within 10 feet gains a +2 morale bonus on saving throws against fear effects. Enemies within 10 feet
take a -2 penalty on saving throws against fear effects. This ability functions only while the
insinuator is conscious, not if he is unconscious or dead.

**Replaces:** Aura of cowardice

**Stubborn Health (Ex)**

**Gained:** At 3rd Level

**Passive:** An insinuator takes only half damage from diseases and poisons, and none of his ability
scores can be reduced below 1 by these effects.

**Replaces:** Plague bringer

**Greeds (Su)**

**Ability:** An insinuator can heal himself of certain conditions. This functions as the _mercy_
paladin class ability, but these _mercies_ can only be applied to the insinuator himself.

**Gained:** At 3rd Level

**Replaces:** Cruelty

**Channel Energy (Su)**

**Alters:** Channel negative energy

**Gained:** At 4th Level

**Standard:** An insinuator can [channel negative energy](ref/ability/channel-energy), treating his
antipaladin level as his effective [cleric](ref/class/cleric) level. If he invokes a neutral
outsider for the day, he may instead chose during the invocation to channel positive energy, but
treats his effective cleric level as half his antipaladin level. Using this ability consumes two
uses of his selfish healing ability. This is a Charisma-based ability.

**Bonus Feats**

**Ability:** An insinuator gains one bonus feat, which must be selected from the list of combat
feats or [Skill Focus](ref/feat/skill-focus).

**Gained:** At 4th Level

**Repeat:** You gain a new combat or Skill Focus feat., 7, 3

**Replaces:** Antipaladin spells

**Ambitious Bond (Sp)**

**Ability:** An insinuator gains a divine bond with either a bonded weapon or an outsider servant.
This functions as the antipaladin's _fiendish boon_ with the following modifications.

**Gained:** At 5th Level

**Bonded Weapon**

**Ability:** This functions as the antipaladin ability, except the first special ability added to a
weapon must correspond to the alignment of the outsider the insinuator has invoked for that day:
[anarchic](ref/magic-enh/anarchic) (chaos), [axiomatic](ref/magic-enh/axiomatic) (law), or
[unholy](ref/magic-enh/unholy) (evil). Additional special abilities may be applied if any equivalent
bonus remains.

**Outsider Servant**

**Ability:** This functions as the antipaladin ability, except the insinuator gains a new outsider
servant each day, whose alignment must match the alignment of the outsider invoked for the day. The
outsider servant functions as much as an agent for the patron invoked by the insinuator as an ally
of the insinuator himself, and may turn against him if he violates his patron's alignment or
interests.

**Aura of Ambition (Su)**

**Gained:** At 8th Level

**Passive:** Enemies within 10 feet of an insinuator take a -1 penalty on all saving throws. All
allies within 10 feet gain a +1 bonus on all saving throws. This penalty does not stack with the
penalty from aura of the crusader. This ability functions only while the insinuator is conscious,
not if he is unconscious or dead.

**Replaces:** Aura of despair

**Aura of Glory (Su)**

**Free:** An insinuator can expend two uses of his _smite impudence_ ability to grant the ability to
_smite impudence_ to all allies within 10 feet, using his bonuses. Allies must use this _smite
impudence_ ability before the start of the insinuator's next turn, and the bonuses last for 1
minute.

**Gained:** At 11th Level

**Replaces:** Aura of vengeance

**Aura of Belief (Su)**

**Gained:** At 14th Level

**Passive:** An insinuator's weapons are treated as chaos-aligned while he invokes a chaotic
outsider, law-aligned when he invokes a lawful outsider, or evil-aligned while he invokes an evil
outsider. If he invokes an outsider with more than one alignment aura, the insinuator must choose
during the initial invocation which alignment his weapon radiates.

**Replaces:** Aura of sin

**Aura of Indomitability (Su)**

**Gained:** At 17th Level

**Passive:** An insinuator gains DR 10 that is bypassed by the alignment opposite of the outsider he
has invoked for the day, or DR 5/- while invoking a neutral outsider.

**Replaces:** Aura of depravity

**Personal Champion (Su)**

**Ability:** In addition, he can invoke a new outsider patron by meditating for 10 minutes.

**Gained:** At 20th Level

**Passive:** An insinuator becomes a living embodiment of his selfish desires. His damage resistance
from aura of indomitability increases to 15 (or 10 while invoking a neutral outsider). Whenever he
uses _smite impudence,_ he adds twice his full Charisma bonus to the attack roll and doubles his
effective bonus damage gained from the smite.

**Replaces:** Unholy champion

**Ex-Insinuators**

**Info:** An insinuator who willfully commits selfless acts or engages in violence that doesn't
further his own ends loses all class features (including his outsider servant, but not bonus feats
or weapon, armor, and shield proficiencies). He can't progress any further in levels as an
insinuator. He regains his abilities and advancement potential if he atones for his faltering
ambition (see the [atonement](ref/spell/atonement) spell). If he violates the code of conduct of his
invoked outsider patron, he must similarly seek atonement from outsiders of that alignment again.
