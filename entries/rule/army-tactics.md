+++
id = "ref/rule/army-tactics"
kind = "rule"
title = "Army Tactics"
source_ids = ["ultimate-campaign"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "army_tactics", path = "json/rules_campaign_types05.json" },
]
[[sources]]
publication = "ultimate-campaign"
page = "237"

[fields]
kind = "none"
+++

Tactics are options an army can use to influence aspects of a battle. A newly recruited army doesn't
know any of these tactics unless specified by the GM. An army learns new tactics by being victorious
in battle (see [Victory, Rout, or Defeat](ref/rule/victory-rout-or-defeat)). An army can know a
number of tactics equal to half its ACR, minimum 0.

When a battle begins, the commander selects one tactic to use for that battle (if the army doesn't
know any tactics, the army uses the standard tactic). At the start of each Ranged or Melee phase,
the commander may try to change tactics by attempting a DC 15 Morale check. Success means the army
uses the new tactic for that phase (and the modifiers from the old tactic cease); failure means the
army continues to use its current tactic. The effects of tactics end when the battle does.

As with battlefield conditions, gaining benefits from a tactic is subject to GM discretion. (For
example, you may not get the expert flankers benefit if you cannot actually flank your enemy).

Tactics marked with an asterisk (\*) are default tactics all armies know; these do not count toward
the number of tactics an army knows.

**Cautious Combat:** Your army fights cautiously in order to maintain morale. Decrease its OM by 2,
and add 2 to all its Morale checks.

**Cavalry Experts:** Your army's OM increases by 2 against armies that aren't mounted. The army must
have the mount resource to use this tactic.

**Defensive Wall:** Your army fights defensively, taking actions to protect fellow units as needed.
Decrease its OM by 2, and increase its DV by 2.

**Dirty Fighters:** Your army uses trickery and unfair tactics to gain an advantage at the start of
a battle. For one Melee phase this battle, its OM increases by 6. (After that Melee phase, the
opposing army knows to be ready for such tricks.)

**Expert Flankers:** Your army is skilled at surrounding the foe and distracting them, at the cost
of spreading out too much and being more vulnerable. Increase its OM by 2, and decrease its DV by 2.

**False Retreat:** Once per battle, your army can make a false retreat, luring a target enemy army
deeper into your territory. On the phase your army makes a false retreat, it doesn't attempt an
Offense check. On the phase after it uses this tactic, increase its OM and DV by 6 against the
target army.

**Full Defense:** Your army focuses on total defense of the battlefield. Increase its DV by 4, and
decrease its OM by 4.

**Relentless Brutality:** Your army throws caution to the wind and attacks with savage and gory
vigor. Increase its OM by 4, and decrease its DV by 4.

**Siegebreaker:** Your army targets another army's siege engines in an attempt to destroy them. If
your army damages the target army, your army attempts a second Offense check; if successful, destroy
one of the target's siege engines. This tactic has no effect on enemy armies without siege engines.

**Sniper Support:** Your army holds some ranged units in reserve to attack a target enemy army
during the Melee phase. If your army damages the target army in the Melee phase, it deals 2
additional points of damage from these ranged attacks. The army must have ranged attacks to use this
tactic.

**Spellbreaker:** Your army has specialists who can disrupt enemy spellcasting. Increase its DV by 4
against armies with the spellcasting ability.

**Standard\*:** Your army's attacks have no additional modifiers to its OM, DV, or damage.

**Taunt:** Your army is skilled at taunting its opponents, provoking stupid mistakes and
overconfidence in battle. The target army must attempt a Morale check (DC = 10 + your army's ACR) at
the start of each Melee or Ranged phase; failure means it reduces its OM and DV against your army by
2 for that phase. If the target army succeeds at two of these Morale checks, it's immune to this
tactic for the remainder of the battle.

**Withdraw\*:** Your army tries to escape from all armies attacking it. The army attempts an opposed
Morale check against each army attacking it to maintain discipline (any army may voluntarily fail
this check), but doesn't need to attempt the usual Morale check to change tactics when switching to
withdraw. If all of these checks are successful, your army may withdraw from the battlefield or
treat the phase as a Ranged phase. If only some are successful, you may withdraw or treat the phase
as a Ranged phase, but enemy armies in the battle may attack you as if you were in Melee. Whether or
not the checks are successful, reduce your army's OM and DV by 2 for the rest of this phase.
