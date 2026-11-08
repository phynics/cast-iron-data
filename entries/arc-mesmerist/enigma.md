+++
id = "ref/arc-mesmerist/enigma"
kind = "archetype"
title = "Enigma"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "enigma", path = "json/archetypes_mesmerist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/mesmerist" },
]

[fields]
kind = "archetype"
replaces = ["Consummate liar", "Painful stare", "Manifold tricks", "Glib lie", "Rule minds"]
alters = ["Hypnotic stare", "Touch treatment"]
+++

**Sources:** Ultimate Intrigue pg 36\
An enigma spends his life dedicated to developing psychic abilities that allow him to operate
unnoticed. While the target of a mesmerist's _hypnotic stare_ might not realize that the mesmerist
is the source of the strange thoughts invading his mind, an enigma takes that mental obfuscation to
a more extreme level. Enigmas often end up serving as master spies and infiltration experts.

**Solipsism (Su)**

**Ability:** Whenever the enigma uses _hypnotic stare_ on a creature, instead of applying a penalty
on the creature's saving throws, the enigma begins to fade from the creature's view. Until the
enigma's next turn, the enigma gains the effects of [concealment](ref/rule/concealment) against that
creature (unless it can see invisible creatures). Starting on the enigma's next turn, he gains the
effect of [invisibility](ref/spell/invisibility) against that creature. These effects last as long
as the enigma continues to use his _hypnotic stare,_ but if he takes an action that would end
_invisibility,_ it ends his _hypnotic stare_ immediately. The enigma can reinstate this effect
whenever he wishes, but each time it begins with 1 round of concealment.

**Alters:** Hypnotic stare

**At 8th Level:** Attacks that would end _invisibility_ do not end the enigma's _hypnotic stare,_
and after 1 round of concealment, he gains the benefits of
[greater invisibility](ref/spell/invisibility-greater) against the target of his stare.

**Gained:** At 1st Level

**Special:** For the purpose of _bold stare_ improvements, the enigma's _hypnotic stare_ always has
a penalty of -1.

**Veiled Steps**

**Passive:** An enigma gains a bonus to his Stealth checks equal to 1/4 his mesmerist level (minimum
+1).

**Replaces:** Consummate liar

**Enigmatic Stare (Su)**

**At 8th Level:** This penalty increases to - 6.

**Passive:** The target of an enigma's _hypnotic stare_ takes a -4 penalty on Perception checks to
notice the enigma.

**Replaces:** Painful stare

**Transfer Affliction (Su)**

**Alters:** Touch treatment

**At 14th Level:** The enigma can instead expend one use of _touch treatment_ to replicate the
effects of [bestow curse](ref/spell/bestow-curse), delivered as a touch attack as part of using this
ability.

**Gained:** At 3rd Level

**Special:** _Transfer affliction_ is a mind-affecting effect.

**Standard:** The enigma can afflict others with the harmful conditions that he endures. This
ability functions as the _touch treatment_ ability, but can only be used to remove harmful
conditions from the enigma, not other creatures. In order to remove these harmful effects, the
enigma must succeed at a touch attack against another creature. The creature touched gains the
chosen harmful effect for whatever duration it would have afflicted the enigma and the effect is
removed from the enigma, unless the creature succeeds at a Will save (DC = 10 + 1/2 the enigma's
mesmerist level + his Charisma modifier). Using this ability is always a standard action.

**Sneak Attack (Ex)**

**Ability:** An enigma gains the [sneak attack](ref/ability/sneak-attack) ability of a rogue,
starting at +1d6 damage.

**Gained:** At 5th Level

**Replaces:** Manifold tricks

At 9th level: Sneak attack damage +2d6.

At 13th level: Sneak attack damage +3d6.

At 17th level: Sneak attack damage +4d6.

**Detection Void (Su)**

**Ability:** An enigma can elude detection spells (spells with &quot&detect&quot& in their name). A
creature using this sort of magic against the enigma must succeed at a caster level check against a
DC equal to 15 + the enigma's class level to succeed (as if the enigma was under the effect of a
[nondetection](ref/spell/nondetection) spell); failure means the magic fails to detect the enigma,
as if he did not exist.

**Gained:** At 11th Level

**Replaces:** Glib lie

**Absentia (Su)**

**Gained:** At 20th Level

**Passive:** All creatures adjacent to the enigma subconsciously ignore him. Adjacent creatures are
always treated as [flat-footed](ref/rule/flat-footed) to the enigma and are not considered to be
directly observing the enigma for the purpose of the Stealth skill. This effect ends immediately if
the enigma makes a successful attack against any creature, but automatically resumes at the
beginning of his next turn.

**Replaces:** Rule minds
