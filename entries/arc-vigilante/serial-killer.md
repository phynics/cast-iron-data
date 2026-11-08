+++
id = "ref/arc-vigilante/serial-killer"
kind = "archetype"
title = "Serial Killer"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "serial_killer", path = "json/archetypes_vigilante.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/vigilante" },
]

[fields]
kind = "archetype"
replaces = ["Unshakable", "4th- and 14th-level vigilante talents, 9th- and 19th-level social talents", "Startling appearance", "6th-level vigilante talent", "7th-level social talent", "Frightening appearance", "12th-level vigilante talent", "Stunning appearance"]
alters = ["Vigilante specialization"]
+++

**Sources:** Horror Adventures pg 71\
Some vigilantes adopt an innocent guise to cloak their acts of brutal murder.

**Alignment**

**Info:** A serial killer's vigilante identity must be evil. A serial killer whose vigilante
identity becomes nonevil cannot gain new levels as a vigilante but retains all of her class
abilities.

**Vigilante Specialization**

**Alters:** Vigilante specialization

**Info:** A serial killer must choose the stalker specialization. Her _hidden strike_ is considered
equivalent to a [sneak attack](ref/ability/sneak-attack) with the same number of dice for the
purpose of meeting prerequisites or using abilities that depend on sneak attack.

**Thwart Pursuit (Ex)**

**Gained:** At 3rd Level

**Passive:** A serial killer adds 1/2 her vigilante level as a bonus on all checks in
[a chase](ref/rule/chases) and to the DCs of Diplomacy checks to gather information about her and
checks to track her or notice her tracks (though not to the DC of the
[profiler's](ref/arc-investigator/profiler) expert profiler ability).

**Replaces:** Unshakable

**Studied Target (Ex)**

**Ability:** A serial killer gains the _studied target_ ability of a [slayer](ref/class/slayer) 3
levels lower, including the ability to study multiple targets simultaneously at the appropriate
levels. The serial killer does not provoke attacks of opportunity when attempting a
[coup de grace](ref/misc/helpless) against a studied target.

**Gained:** At 4th Level

**Replaces:** 4th- and 14th-level vigilante talents, 9th- and 19th-level social talents

**Studied Target (Ex)**

**Flavor:** Text from the slayer class ability.

**Free:** You can discard this connection to a studied target, allowing you to study another target
in its place.

**Immediate:** If you deal sneak attack damage to a target, you can study that target immediately,
allowing you to apply your studied target bonuses against that target (including to the normal
weapon damage roll).

**At 7th Level:** You can now choose to study a target as a **swift action**.

**Move:** You can study an opponent you can see. You then gain a bonus on Bluff, Knowledge,
Perception, Sense Motive, and Survival checks attempted against that opponent, and a bonus on weapon
attack and damage rolls against it; these bonuses are equal to 1 +
[one-fifth](ref/misc/fractions-and-rounding) of your slayer level. The DCs of slayer class abilities
against that opponent increase by 1 + one-fifth of your slayer level. You can only maintain these
bonuses against a certain number of opponents at a time (equal to 1 + one-fifth of your slayer
level); these bonuses remain in effect until either the opponent is dead or you study a new target.

**Charming (Ex)**

**Ability:** A serial killer gains the [charm](ref/hex/charm) hex as if she were a witch of her
vigilante level, but she can't affect animals. The DC is based on her Charisma, and the ability is
nonmagical.

**Gained:** At 5th Level

**Replaces:** Startling appearance

**Death Attack (Ex)**

**Ability:** A serial killer gains the ability to make a _death attack_ as if she were an
[assassin](ref/pclass/assassin) (DC = 10 + 1/2 her vigilante level + her Charisma modifier).

**Gained:** At 6th Level

**Replaces:** 6th-level vigilante talent

**Death Attack (Ex)**

**Ability:** If an assassin studies his victim for 3 rounds and then makes a sneak attack with a
melee weapon that successfully deals damage, the sneak attack has the additional effect of possibly
either paralyzing or killing the target (assassin's choice). Studying the victim is a **standard
action**. The _death attack_ fails if the target detects the assassin or recognizes the assassin as
an enemy (although the attack might still be a sneak attack if the target is denied his Dexterity
bonus to his Armor Class or is flanked). If the victim of such a _death attack_ fails a Fortitude
save (DC 10 + the assassin's class level + the assassin's Int modifier) against the kill effect, she
dies. If the saving throw fails against the paralysis effect, the victim is rendered
[helpless](ref/misc/helpless) and unable to act for 1d6 rounds plus 1 round per level of the
assassin. If the victim's saving throw succeeds, the attack is just a normal sneak attack.

Once the assassin has completed the 3 rounds of study, he must make the _death attack_ within the
next 3 rounds. If a _death attack_ is attempted and fails (the victim makes her save) or if the
assassin does not launch the attack within 3 rounds of completing the study, 3 new rounds of study
are required before he can attempt another _death attack._

**Flavor:** Text from the assassin prestige class ability.

**Calling Card (Ex)**

**Ability:** When a serial killer slays a humanoid with a _coup de grace_ or _death attack,_ she can
leave a telltale token or clue behind identifying this death as her work. The serial killer chooses
her calling card when she gains this ability, and the first time she uses it in an area where she
has renown (as per the [renown](ref/soctalent/renown) social talent), it becomes associated with her
killings. After that, once citizens of a new settlement find this calling card, the serial killer
immediately establishes the settlement as an area of renown for her vigilante identity without
spending additional time to spread tales, and the Intimidate bonus from renown increases by 2. She
still must spend time to establish her social identity's renown.

**Gained:** At 7th Level

**Replaces:** 7th-level social talent

**Grisly Murder (Ex)**

**Ability:** A serial killer gains [Dreadful Carnage](ref/feat/dreadful-carnage) as a bonus feat,
and if she leaves a calling card, the murder is so horrifying that creatures examining the corpse
are affected as per [nightmare](ref/spell/nightmare) that night (DC = 10 + 1/2 the serial killer's
vigilante level + her Charisma modifier). The _[nightmare](ref/spell/nightmare)_ affects a number of
creatures equal to the serial killer's Charisma modifier, starting with the first creature to
examine the corpse.

**Gained:** At 11th Level

**Replaces:** Frightening appearance

**Quiet Death (Ex)**

**Ability:** A serial killer gains the _quiet death_ class feature as if she were an assassin.

**Gained:** At 12th Level

**Replaces:** 12th-level vigilante talent

**Quiet Death (Ex)**

**Ability:** Whenever an assassin kills a creature using his _death attack_ during a surprise round,
he can also make a Stealth check, opposed by Perception checks of those in the vicinity to prevent
them from identifying him as the assailant. If successful, those nearby might not even notice that
the target is dead for a few moments, allowing the assassin to avoid detection.

**Flavor:** Text from the assassin prestige class ability.

**Swift Death (Ex)**

**Ability:** A serial killer gains the _swift death_ class feature as an assassin.

**Gained:** At 17th Level

**Replaces:** Stunning appearance

**Swift Death (Ex)**

**Ability:** Once per day, an assassin can make a _death attack_ against a foe without studying the
foe beforehand. He must still sneak attack his foe using a melee weapon that deals damage.

**Flavor:** Text from the assassin prestige class ability.
