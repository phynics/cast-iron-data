+++
id = "ref/rule/offensive-manifestation-full-round-action"
kind = "rule"
title = "Offensive Manifestation (Full-Round Action)"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "offensive_manifestation_full_round_action", path = "json/rules_campaign_types08.json" },
]

[fields]
kind = "none"
+++

**Sources:** Occult Adventures pg 202

This type of manifestation is a direct attack on an opponent, a thought-form creature, or both. An
offensive manifestation can attack a variety of defenses, depending on the number of MP spent and
the desires of its creator. Creating an offensive manifestation requires three steps.

**Step 1-Create Sensory Effects:** Combatants creating psychic manifestations are limited only by
their imaginations as to the look, sound, feel, and smell of each manifestation; these sensory
effects guide combatants in their later choices. For example, if a combatant envisions an offensive
manifestation as a giant ball of lava he throws at his opponent, that might suggest that the attack
should force a Reflex saving throw rather than targeting the opponent's AC. Regardless of the
effect's form, damage dealt by a manifestation is always untyped damage, and can be mitigated only
by defensive manifestations.

**Step 2-Determine Attack Type:** By default, an offensive manifestation acts as either a melee or
ranged attack (creator's choice) that resolves against a single target's AC. The creator can have
the manifestation resolve against touch AC instead by increasing the cost by 2 MP.

Alternatively, the creator can instead force both his opponent and any thought-form creature it
controls to attempt a saving throw to avoid the effect; this increases the cost by 1 MP. The DC is
equal to 10 + the total number of MP spent + the Intelligence, Wisdom, or Charisma bonus of the
creator (whichever is highest). The creator chooses which kind of saving throw - Fortitude, Reflex,
or Will - the target must attempt. By default, a successful save negates the manifestation's damage,
but the creator can increase the cost by an additional 1 MP to cause the manifestation to deal half
damage on a successful save.

If an offensive manifestation's effects can be negated or reduced with a saving throw, the creator
can increase the cost to have the manifestation apply a condition.

**Step 3-Determine Damage and Conditions:** After determining the manifestation's attack type, the
creator determines its number of damage dice. The creator must spend at least 1 MP on damage, which
grants the manifestation 1 damage die, but she can spend more to increase the number of dice, as
shown on the table below.

|MP Spent on Damage|Number of Damage Dice|
| --- | --- |
|1 MP|1 die|
|2 MP|4 dice|
|3 MP|6 dice|
|4 MP|8 dice|
|5 MP|10 dice|
|6 MP|12 dice|
|7 MP|14 dice|
|8 MP|16 dice|
|9 MP|1 die per creator's manifesting level (maximum 20 dice)|

The manifestation's damage die type depends on the source of the manifestation's MP. Psychic spells
and [spell-like abilities](ref/umr/spell-like-abilities) sacrificed grant d8s. Arcane spells and
other spell-like abilities grant d6s. All other methods of generating MP (including mixed methods)
grant d4s. If the manifestation's attack resolves against AC or touch AC, a natural 20 on the attack
roll threatens a critical hit for double damage.

If the manifestation allows a saving throw, the creator can spend additional MP to add one condition
from the list below (she must still spend at least 1 MP on damage). A successful saving throw always
negates the condition. Conditions gained in a psychic duel end if the duel ends before the
condition's normal duration expires. The conditions below otherwise follow the normal rules for
those conditions, with the following exceptions and additions.

**Blinded (3 MP):** Affected creatures are blinded for 1 round; they can't use offensive
manifestations that require saves.

**Confused (3 MP):** The affected creatures are confused for 1 round, breaking concentration
automatically. If an affected creature is forced to attack the nearest creature, it attacks its
opponent's thought-form creature if one exists, or the opponent if not. A confused combatant never
attacks her own thought-form creature, or vice versa. This condition can be applied only to
manifestations that require Will saves.

**Dazed (4 MP):** The affected creatures are dazed for 1 round. A dazed combatant can continue to
concentrate on thought-form creatures and create defensive manifestations, but can't create
thought-form creatures or offensive manifestations. This condition can be applied only to
manifestations that require Will saves.

**Entangled (2 MP):** The affected creatures are entangled until they take a full-round action to
end this condition. This condition can be applied only to manifestations that require Reflex saves.

**Nauseated (4 MP):** The affected creatures are nauseated for 1 round. A nauseated creature can
create only defensive manifestations. This condition can be applied only to manifestations that
require Fortitude saves.

**Shaken (1 MP):** The affected creatures are shaken for 1d4 rounds. This condition can be applied
only to manifestations that require Will saves.
