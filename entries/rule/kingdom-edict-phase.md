+++
id = "ref/rule/kingdom-edict-phase"
kind = "rule"
title = "Kingdom Edict Phase"
source_ids = ["ultimate-campaign"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "kingdom_edict_phase", path = "json/rules_campaign_types04.json" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Campaign pg 206

The Edict phase is when you make proclamations on expansion, improvements, taxation, holidays, and
so on.

**Step 1-Assign Leadership:** Assign PCs or NPCs to any vacant leadership roles or change the roles
being filled by particular PCs or closely allied NPCs (see
[Leadership Roles](ref/rule/leadership-roles)).

**Steps 2 and 3-Claim and Abandon Hexes:** For your kingdom to grow, you must claim additional
hexes. You can only claim a hex that is adjacent to at least 1 other hex in your kingdom. Before you
can claim it, the hex must first be explored, then cleared of monsters and dangerous hazards (see
Steps 2 and 3 of [Founding a Settlement](ref/rule/founding-a-settlement) for more details). Then, to
claim the hex, spend 1 BP; this establishes the hex as part of your kingdom and increases your
kingdom's Size by 1. [Table 4-4: Improvement Edicts](ref/rule/improvement-edicts) tells you the
maximum number of hexes you can claim per turn.

You may abandon any number of hexes to reduce your kingdom's Size (which you may wish to do to
manage Consumption). Doing so increases Unrest by 1 for each hex abandoned (or by 4 if the hex
contained a settlement). This otherwise functions like losing a hex due to unrest
([see Step 4 of the Upkeep phase](ref/rule/upkeep-phase)).

**Step 4-Build Terrain Improvements:** You may spend BP to build terrain improvements like Farms,
Forts, Roads, Mines, and Quarries (see [Terrain Improvements](ref/rule/terrain-improvements)).

You may also prepare a hex for constructing a settlement. Depending on the site, this may involve
clearing trees, moving boulders, digging sanitation trenches, and so on. See the Preparation Cost
column on [Table 4-6: Terrain and Terrain Improvements](ref/rule/terrain-improvements) to determine
how many BP this requires.

[Table 4-4: Improvement Edicts](ref/rule/improvement-edicts) tells you the maximum number of terrain
improvements you can make per turn.

**Step 5-Create and Improve Settlements:** You may create a settlement in a claimed hex (see
[Founding a Settlement](ref/rule/founding-a-settlement)).
[Table 4-4: Improvement Edicts](ref/rule/improvement-edicts) tells you the maximum number of
settlements you can establish per turn.

You may construct a building in any settlement in your kingdom. The list of available building types
can be found [here](ref/rule/building-descriptions). When a building is completed, apply its
modifiers to your kingdom sheet. [Table 4-4: Improvement Edicts](ref/rule/improvement-edicts) tells
you the maximum number of buildings you can construct in your kingdom per turn. The first House,
Mansion, Noble Villa, or Tenement your kingdom builds each turn does not count against that limit.

**Step 6-Create Army Units:** You may create, expand, equip, or repair army units (see
[Mass Combat](ref/rule/mass-combat)).

**Step 7-Issue Edicts:** Select or adjust your edict levels (see [Edicts](ref/rule/edicts)).

Example: Jessica's kingdom has no vacant leadership roles, so nothing happens in Step 1. The leaders
don't want to spend BP and increase Size right now, so in Step 2 they don't claim any hexes. In Step
3, the leaders construct a Farm in one of the kingdom's prepared hexes (Consumption -2, Treasury -2
BP). In Steps 5 and 6, the leaders continue to be frugal and do not construct settlement
improvements or create armies. In Step 7, the leaders issue a Holiday edict of one national holiday
(Loyalty +1, Consumption +1) and set the Promotion edict level to "none" (Stability -1, Consumption
+0). Looking ahead to the Income phase, Jessica realizes that an average roll for her Economy check
would be a failure (10 on the 1d20 + 52 Economy - 4 Unrest = 58, less than the Control DC of 60),
which means there's a good chance the kingdom won't generate any BP this turn. She decides to set
the Taxation edict to "heavy" (Economy +3, Loyalty -4). At the end of this phase, the kingdom has
Economy 55, Loyalty 42, Stability 55, Unrest 4, Consumption 4, and Treasury 5 BP.
