+++
id = "ref/arc-hunter/colluding-scoundrel"
kind = "archetype"
title = "Colluding Scoundrel"
aon = "ArchetypeDisplay.aspx?FixedName=Hunter%20Colluding%20Scoundrel"
source_ids = ["antiheros-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "colluding_scoundrel", path = "json/archetypes_hunter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/hunter" },
]
[[sources]]
publication = "antiheros-handbook"
page = "11"

[fields]
kind = "archetype"
replaces = ["Animal focus", "Second animal focus", "Master hunter"]
replaces_features = ["animal-focus", "second-animal-focus", "master-hunter"]
+++

The colluding scoundrel is a canny and conniving skirmisher, manipulating her enemies and leveraging
her allies for her own benefit. A Free Captain ordering her crew to occupy foes and thus expose the
enemy to her attacks might take this archetype, and colluding scoundrels have proven to be
formidable members of the Wasp Queens, as their giant wasp companions draw out opponents to fall
under the Wasp Queens' stinging blades. In any case, the colluding scoundrel rarely concerns herself
overmuch with her allies' well-being.

**Scapegoat (Ex)**

**Action:** Swift Action

**Flavor:** A colluding scoundrel is adept at redirecting a foe's hostility toward another creature,
creating openings for her own attacks.

**Replaces:** Animal focus

**Special:** This is a mind-affecting effect. The effect ends if the colluding scoundrel falls
unconscious or is slain.

**Usage:** 1 time/day per hunter level

At 8th level: The penalty -4.

At 15th level: The penalty -6.

A colluding scoundrel can target one foe within 30 feet and designate one willing ally adjacent to
that foe as a scapegoat. For the following minute, the target takes a -2 penalty on attacks against
any creature other than the designated scapegoat, and the target has a 10% spell failure chance on
spells that don't target the scapegoat or include the scapegoat in their area of effect.

The colluding scoundrel can designate her animal companion as a scapegoat without it counting
against her daily uses of this ability.

**Backstabber (Ex)**

**Ability:** A colluding scoundrel deals 2d6 additional points of damage on attacks against a target
threatened by an ally currently designated as the scapegoat.

**At 15th Level:** This increases to 3d6 points of damage.

**Gained:** At 8th Level

**Replaces:** Second animal focus

**Special:** This is precision damage and is not multiplied on a critical hit, but it does stack
with [sneak attack](ref/ability/sneak-attack) and similar effects.

**Master Backstabber (Ex)**

**Flavor:** A colluding scoundrel becomes a master at dispatching distracted targets.

**Gained:** At 2nd Level

**Replaces:** Master hunter

**Special:** Whether or not the target succeeds, it cannot be targeted by this ability again (by any
colluding scoundrel) for 24 hours.

**Standard:** She can make a single attack against a foe that is taking the penalties of her
scapegoat ability and is adjacent to an ally currently designated as the scapegoat. If the attack
hits, the target takes damage normally and must succeed at a Fortitude saving throw (DC = 10 + half
the colluding scoundrel's level + her Wisdom modifier) or be slain.
