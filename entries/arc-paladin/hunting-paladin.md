+++
id = "ref/arc-paladin/hunting-paladin"
kind = "archetype"
title = "Hunting Paladin"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Hunting%20Paladin"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hunting_paladin", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "70"

[fields]
kind = "archetype"
replaces = ["1st-level use of smite evil", "Aura of resolve"]
alters = ["Armor proficiencies", "Detect evil", "Smite evil", "Spells"]
+++

Hunting paladins are tenacious trackers and stealthy stalkers in pursuit of evildoers.

**Gained class skills:** kna, per, stl, sur

**Lost class skills:** diplo, heal, kno, spc

**Weapon and Armor Proficiency**

**Alters:** Armor proficiencies

**Info:** A hunting paladin is not proficient with heavy armor.

**Hunt Evil (Su)**

**Ability:** Once per day, a hunting paladin can designate a single evil creature within her sight
or one that she has determined to be evil by declaring it the target of her hunt and following its
tracks; this allows her to add her Charisma modifier as a bonus on Survival checks to follow that
creature's tracks and on Perception and Stealth checks opposed by the target of her hunt. She can
sense her target's presence and location, which lets her pinpoint her target's location when within
10 feet; if the target has [concealment](ref/rule/concealment), she can roll twice and use the
better result on rolls to determine whether she misses due to the concealment. She gains
[uncanny dodge](ref/ability/uncanny-dodge) as per the [barbarian](ref/class/barbarian) class feature
against her target.

**Replaces:** 1st-level use of smite evil

**Special:** If the hunting paladin targets a nonevil creature with _hunt evil,_ the ability fails
and it is wasted. This ability ends after 24 hours (unless she spends the next day's use of this
ability to continue hunting the same target), after the hunting paladin or the target is killed or
when she designates a new target for her hunt.

**Detect Evil (Su)**

**Ability:** A hunting paladin cannot use this ability as a move action. However, when a hunting
paladin has successfully followed a creature's tracks for at least 1 minute, she can discern whether
the tracked creature's alignment was evil, as if she had cast [detect evil](ref/spell/detect-evil)
in its presence and concentrated for 3 rounds.

**Alters:** Detect evil

**Smite Evil (Su)**

**Alters:** Smite evil

**At 4th Level:** A hunting paladin gains this ability at 4th level, and it functions at her paladin
level - 3. She can expend a daily use of _smite evil_ to gain an additional daily use of _hunt
evil._ She can use _smite evil_ and _hunt evil_ against the same target.

**Spells**

**Ability:** For each level of spell she can cast, a hunting paladin can prepare and cast one spell
per day from the ranger spell list rather than the paladin spell list.

**Alters:** Spells

**Tireless Aura (Su)**

**Gained:** At 8th Level

**Passive:** A hunting paladin becomes immune to [fatigue](ref/misc/fatigued) and sleep effects, and
allies within 10 feet gain a +4 bonus on saving throws to avoid becoming fatigued or falling asleep.

**Replaces:** Aura of resolve
