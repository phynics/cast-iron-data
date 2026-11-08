+++
id = "ref/arc-slayer/velvet-blade"
kind = "archetype"
title = "Velvet Blade"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "velvet_blade", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]

[fields]
kind = "archetype"
replaces = ["Track", "Swift tracker"]
alters = ["Armor proficiency", "Studied target"]
+++

**Sources:** Ultimate Intrigue pg 70\
Velvet blades specialize in infiltrating the upper echelons of society, mingling with nobles and
courtiers, and killing them. Velvet blades are often born into the aristocracy, with an intricate
understanding of the inner workings of upper-class society. Though a few velvet blades are unhinged
maniacs who enjoy preying on their peers, most of these well-heeled slayers assume a professional
demeanor and hire themselves out to other nobles or well-connected criminal organizations.

**Gained class skills:** diplo, kno

**Lost class skills:** kd

**Armor Proficiency**

**Alters:** Armor proficiency

**Info:** A velvet blade is not proficient with medium armor or shields.

**Studied Socialite (Ex)**

**Alters:** Studied target

**Flavor:** A velvet blade focuses her studies on social infiltration rather than brute force,
believing it is easier to kill an opponent quietly and unprepared than in a loud battle.

**Passive:** She adds her _studied target_ bonus on Bluff, Diplomacy, Disguise, Intimidate,
Knowledge, Perception, Sense Motive, Stealth, and Survival checks against _studied_ opponents, as
well as to the DCs of slayer class abilities she uses against such opponents.

**Special:** She never gains a bonus on weapon attack and damage rolls from her _studied target_
ability.

**Courtly Graces (Ex)**

**Flavor:** A velvet blade spends long hours memorizing etiquette and family lineages of royalty and
other prominent families.

**Passive:** She gains a bonus on Knowledge (nobility) checks equal to
[half](ref/misc/fractions-and-rounding) her slayer level (minimum +1).

**Replaces:** Track

**Treacherous Blade (Ex)**

**Ability:** She gains the [Betrayer](ref/feat/betrayer) feat as a bonus feat, whether or not she
meets the prerequisites. Additionally, when making her first attack against a _studied target_ that
believes her to be harmless or to be an ally, the attack counts as a sneak attack, even if the
target isn't flanked or denied its Dexterity bonus to AC, and the velvet blade gains +2d6 sneak
attack damage.

**Flavor:** A velvet blade can capitalize on how others underestimate her and allow her close to
them, assuming she is harmless.

**Gained:** At 7th Level

**Special:** Even if she immediately attacks the target again (such as by continuing a full attack),
only the first attack gains these benefits, since the target immediately realizes the velvet blade
is something more than she seemed.

At 10th level: The sneak attack damage +3d6.

At 15th level: The sneak attack damage +4d6.

At 20th level: The sneak attack damage +5d6.

**Silent Dispatch (Ex)**

**Ability:** She gains the [silent dispatch](ref/vigtalent/silent-dispatch) vigilante talent without
meeting the talent's prerequisites.

**Flavor:** A velvet blade becomes adept at taking out her targets quietly.

**Gained:** At 11th Level

**Replaces:** Swift tracker
