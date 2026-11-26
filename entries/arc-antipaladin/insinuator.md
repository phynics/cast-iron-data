+++
id = "ref/arc-antipaladin/insinuator"
kind = "archetype"
title = "Insinuator"
aon = "ArchetypeDisplay.aspx?FixedName=Antipaladin%20Insinuator"
source_ids = ["agents-of-evil"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "insinuator", path = "json/archetypes_antipaladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/antipaladin" },
]
[[sources]]
publication = "agents-of-evil"
page = "20"

[fields]
kind = "archetype"
features = [
  { anchor = "code-of-conduct" },
  { anchor = "invocation", level = 1 },
  { anchor = "detect-balance", level = 1 },
  { anchor = "smite-impudence", level = 1 },
  { anchor = "selfish-healing", level = 2 },
  { anchor = "aura-of-ego", level = 3 },
  { anchor = "stubborn-health", level = 3 },
  { anchor = "greeds", level = 3 },
  { anchor = "channel-energy", level = 4 },
  { anchor = "ambitious-bond", level = 5 },
  { anchor = "aura-of-ambition", level = 8 },
  { anchor = "aura-of-glory", level = 11 },
  { anchor = "aura-of-belief", level = 14 },
  { anchor = "aura-of-indomitability", level = 17 },
  { anchor = "personal-champion", level = 20 },
]
trades = [
  { replaces = "Aura of evil", feature = "aura-of-evil", by = ["invocation"] },
  { replaces = "Smite good", feature = "smite-good", by = ["smite-impudence"] },
  { replaces = "Touch of corruption", feature = "touch-of-corruption", by = ["selfish-healing"] },
  { replaces = "Aura of cowardice", feature = "aura-of-cowardice", by = ["aura-of-ego"] },
  { replaces = "Plague bringer", feature = "plague-bringer", by = ["stubborn-health"] },
  { replaces = "Cruelty", feature = "cruelty", by = ["greeds"] },
  { replaces = "Antipaladin spells", feature = "spells" },
  { replaces = "Aura of despair", feature = "aura-of-despair", by = ["aura-of-ambition"] },
  { replaces = "Aura of vengeance", feature = "aura-of-vengeance", by = ["aura-of-glory"] },
  { replaces = "Aura of sin", feature = "aura-of-sin", by = ["aura-of-belief"] },
  { replaces = "Aura of depravity", feature = "aura-of-depravity", by = ["aura-of-indomitability"] },
  { replaces = "Unholy champion", feature = "unholy-champion", by = ["personal-champion"] },
  { alters = "Detect good", feature = "detect-good", by = ["detect-balance"] },
  { alters = "Channel negative energy", feature = "channel-negative-energy", by = ["channel-energy"] },
]
+++

Between the selfless nobility of paladins and the chaotic menace of antipaladins, there exists a
path of dedicated self-interest. Shunning the ties that bind them to a single deity, insinuators
embrace whatever forces help them achieve their own agenda and glory, borrowing power to emulate
divine warriors.

## Alignment {#alignment}

Any evil.

## Code of Conduct {#code-of-conduct}

An insinuator must always work toward his own self-interest, enrichment, or glory, and must also
abide by the moral strictures of whatever outsider they have chosen to invoke that day (see
invocation below). If the insinuator breaks an invoked outsider's code, he cannot invoke outsiders
of that same alignment until he seeks [atonement](ref/spell/atonement), although outsiders of other
alignments may still heed his call.

## Invocation (Ex) {#invocation}

At the start of each day, an insinuator can meditate for 10 minutes to contact and barter with an
outsider to empower him for a day. An insinuator can freely invoke an outsider of his own alignment.
He can instead invoke an outsider within one step of his own alignment by succeeding at a Diplomacy
or Knowledge (religion) skill check (DC = 15 + the insinuator's antipaladin level). While invoking
the power of an outsider, the insinuator radiates an alignment aura that matches that of the
outsider's, and becomes vulnerable to alignment-based effects that target that outsider's alignment
(such as smite evil or _[chaos hammer](ref/spell/chaos-hammer)_). None of an insinuator's
supernatural or spell-like class abilities function unless he has invoked the power of an outsider,
and the alignment of the being invoked may affect how some abilities function.

This ability replaces aura of evil.

## Detect Balance (Sp) {#detect-balance}

At will, an insinuator can detect strong moral leanings. This functions as
_[detect evil](ref/spell/detect-evil)_ or _[detect good](ref/spell/detect-good)_, but does not
actually reveal the target's alignment, only whether the target is neutral (rather than good or
evil) and the relative strength of that aura. This ability alters detect good.

## Smite Impudence (Su) {#smite-impudence}

Once per day, an insinuator can beseech the forces empowering him to punish their shared enemies. As
a swift action, the insinuator chooses one target within sight to smite.

An insinuator cannot use smite against a target that shares an alignment with the outsider he has
invoked for the day. The insinuator adds his Charisma bonus on his attack rolls and
[half](ref/misc/fractions-and-rounding) his insinuator level on all damage rolls made against the
target of his smite. If the target is an outsider, dragon, or divine spellcaster with an alignment
opposed to that of the outsider he has invoked for the day, the bonus damage on the first successful
attack increases to 1 point of damage per antipaladin level the insinuator has.

Regardless of the target, the smite attack automatically bypasses any
[damage reduction](ref/rule/damage-reduction) the creature might possess. In addition, each time the
insinuator declares a smite, he gains a number of
[temporary hit points](ref/rule/temporary-hit-points) equal to his antipaladin level.

The smite effect remains until the target is defeated or the next time the insinuator rests and
regains his uses of this ability.

At 4th level and at every 3 levels thereafter, the insinuator can use smite one additional time per
day, to a maximum of seven times per day at 19th level. This ability replaces smite good.

## Selfish Healing (Su) {#selfish-healing}

Beginning at 2nd level, an insinuator can heal his wounds by touch. This is treated exactly like the
paladin's [lay on hands](ref/ability/lay-on-hands) class feature, except it can be used only to heal
the insinuator and cannot be used on other creatures. This ability replaces touch of corruption.

## Aura of Ego (Su) {#aura-of-ego}

At 3rd level, an insinuator radiates an aura that bolsters allies and deters enemies. Each ally
within 10 feet gains a +2 morale bonus on saving throws against fear effects. Enemies within 10 feet
take a -2 penalty on saving throws against fear effects. This ability functions only while the
insinuator is conscious, not if he is unconscious or dead. This ability replaces aura of cowardice.

## Stubborn Health (Ex) {#stubborn-health}

At 3rd level, an insinuator takes only half damage from diseases and poisons, and none of his
ability scores can be reduced below 1 by these effects. This ability replaces plague bringer.

## Greeds (Su) {#greeds}

Beginning at 3rd level, an insinuator can heal himself of certain conditions. This functions as the
mercy paladin class ability, but these mercies can only be applied to the insinuator himself. This
ability replaces cruelty.

## Channel Energy (Su) {#channel-energy}

At 4th level, an insinuator can [channel negative energy](ref/ability/channel-energy), treating his
antipaladin level as his effective [cleric](ref/class/cleric) level. If he invokes a neutral
outsider for the day, he may instead chose during the invocation to channel positive energy, but
treats his effective cleric level as half his antipaladin level. Using this ability consumes two
uses of his selfish healing ability. This is a Charisma-based ability. This ability alters channel
negative energy.

## Bonus Feats {#bonus-feats}

At 4th level, an insinuator gains one bonus feat, which must be selected from the list of combat
feats or [Skill Focus](ref/feat/skill-focus). At 7th level and every 3 antipaladin levels
thereafter, the insinuator gains one additional combat or Skill Focus feat. This ability replaces
antipaladin spells.

## Ambitious Bond (Sp) {#ambitious-bond}

At 5th level, an insinuator gains a divine bond with either a bonded weapon or an outsider servant.
This functions as the antipaladin's fiendish boon with the following modifications.

### Bonded Weapon {#bonded-weapon}

This functions as the antipaladin ability, except the first special ability added to a weapon must
correspond to the alignment of the outsider the insinuator has invoked for that day:
_[anarchic](ref/magic-enh/anarchic)_ (chaos), _[axiomatic](ref/magic-enh/axiomatic)_ (law), _or_
_[unholy](ref/magic-enh/unholy)_ (evil). Additional special abilities may be applied if any
equivalent bonus remains.

### Outsider Servant {#outsider-servant}

This functions as the antipaladin ability, except the insinuator gains a new outsider servant each
day, whose alignment must match the alignment of the outsider invoked for the day. The outsider
servant functions as much as an agent for the patron invoked by the insinuator as an ally of the
insinuator himself, and may turn against him if he violates his patron's alignment or interests.

## Aura of Ambition (Su) {#aura-of-ambition}

At 8th level, enemies within 10 feet of an insinuator take a -1 penalty on all saving throws. All
allies within 10 feet gain a +1 bonus on all saving throws. This penalty does not stack with the
penalty from aura of the crusader. This ability functions only while the insinuator is conscious,
not if he is unconscious or dead. This ability replaces aura of despair.

## Aura of Glory (Su) {#aura-of-glory}

At 11th level, an insinuator can expend two uses of his smite impudence ability to grant the ability
to smite impudence to all allies within 10 feet, using his bonuses. Allies must use this smite
impudence ability before the start of the insinuator's next turn, and the bonuses last for 1 minute.
Using this ability is a free action. This ability replaces aura of vengeance.

## Aura of Belief (Su) {#aura-of-belief}

At 14th level, an insinuator's weapons are treated as chaos-aligned while he invokes a chaotic
outsider, law-aligned when he invokes a lawful outsider, or evil-aligned while he invokes an evil
outsider. If he invokes an outsider with more than one alignment aura, the insinuator must choose
during the initial invocation which alignment his weapon radiates. This ability replaces aura of
sin.

## Aura of Indomitability (Su) {#aura-of-indomitability}

At 17th level, an insinuator gains DR 10 that is bypassed by the alignment opposite of the outsider
he has invoked for the day, or DR 5/— while invoking a neutral outsider. This ability replaces aura
of depravity.

## Personal Champion (Su) {#personal-champion}

At 20th level, an insinuator becomes a living embodiment of his selfish desires. His damage
resistance from aura of indomitability increases to 15 (or 10 while invoking a neutral outsider).
Whenever he uses smite impudence, he adds twice his full Charisma bonus to the attack roll and
doubles his effective bonus damage gained from the smite. In addition, he can invoke a new outsider
patron by meditating for 10 minutes. This ability replaces unholy champion.

## Ex-Insinuators {#ex-insinuators}

An insinuator who willfully commits selfless acts or engages in violence that doesn't further his
own ends loses all class features (including his outsider servant, but not bonus feats or weapon,
armor, and shield proficiencies). He can't progress any further in levels as an insinuator. He
regains his abilities and advancement potential if he atones for his faltering ambition (see the
_[atonement](ref/spell/atonement)_ spell). If he violates the code of conduct of his invoked
outsider patron, he must similarly seek atonement from outsiders of that alignment again.
