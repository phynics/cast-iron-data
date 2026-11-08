+++
id = "ref/arc-alchemist/fermenter"
kind = "archetype"
title = "Fermenter"
source_ids = ["potions-and-poisons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fermenter", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]

[fields]
kind = "archetype"
replaces = ["Poison resistance", "the discovery gained at 10th level", "Poison use", "Swift poisoning"]
+++

**Sources:** Potions and Poisons pg 8\
Little more than moonshiners to some, fermenters focus their efforts on imbibing substances,
learning from the resulting effects on their bodies, and infusing this knowledge into their skill
sets. Fermenters consider themselves living experiments and accept the risks and benefits inherent
in their work.

**Substance Tolerance (Ex)**

**At 10th Level:** The bonus to resist addiction increases to +4, and the fermenter suffers no
penalties at all from drinking tinctures, including conditions and other non-numerical penalties
([starlight juice](ref/eq-misc/starlight-juice) would not make her dazzled, for example).
Additionally, she can consume a number of alcoholic beverages equal to one plus four times her
Constitution modifier before becoming sickened.

**At 8th Level:** The bonus to resist addiction increases to +3.

**Gained:** At 2nd Level

**Passive:** Whenever a fermenter consumes a drug, she gains a +2 bonus on her saving throw to
resist becoming [addicted](ref/rule/addiction). Whenever she consumes a tincture, she gains its
usual benefits, but all penalties imposed are reduced by 1. (If the tincture's penalties instead
impose a condition or another penalty that is not numerical, such as the penalties imposed by
starlight juice, this ability has no effect at 2nd level.) Additionally, the fermenter can consume a
number of alcoholic beverages equal to one plus three times her Constitution modifier before
becoming [sickened](ref/misc/sickened) for 1 hour per drink above this maximum.
([Normal rules for drunkenness can be found here.](ref/rule/drunkenness))

**Replaces:** Poison resistance, the discovery gained at 10th level

**Volatile Bombs (Ex)**

**Flavor:** A fermenter under the influence can make her bombs more potent, but they also become
unstable and more difficult to aim.

**At 13th Level:** The penalty becomes -4.

**At 19th Level:** The penalty increases to -5.

**At 7th Level:** The penalty increases to -3.

**Gained:** At 2nd Level

**Passive:** As long as the fermenter is under the effects of a drug or tincture, or has imbibed an
alcoholic drink in the past 10 minutes, her bombs deal 1 additional point of damage per damage die.
While this ability is in effect, she also takes a -2 penalty on attack rolls made with her bombs.

**Replaces:** Poison use

**Batch Brew (Ex)**

**Ability:** A fermenter learns how to brew tinctures in larger batches. Whenever she creates a
tincture using Craft (alchemy), she can simultaneously create a number of additional tinctures equal
to her Intelligence modifier. She expends resources for each tincture separately, but she attempts a
single Craft check and applies the result to each tincture being brewed.

**Gained:** At 6th Level

**Replaces:** Swift poisoning
