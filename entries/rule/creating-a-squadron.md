+++
id = "ref/rule/creating-a-squadron"
kind = "rule"
title = "Creating a Squadron"
source_ids = ["pathfinder-59-the-price-of-infamy"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "creating_a_squadron", path = "json/rules_campaign_types10.json" },
]
[[sources]]
publication = "pathfinder-59-the-price-of-infamy"
page = "65"

[fields]
kind = "none"
+++

A squadron consists of a number of individual ships, each commanded by a captain. The squadron (and
its captains) are in turn commanded by a single commodore. A squadron can have no more ships than
its commodore's Charisma modifier + 3.

Each squadron and its statistics is listed in its fleet's stat block under a separate subheading. On
the fleet sheet, each squadron is recorded in its own squadron box. Follow the steps below to fill
out a squadron box.

**Step 1 - Name the Squadron:** Record the squadron's name at the top of the box - this name can be
whatever you want.

**Step 2 - Determine the Configuration:** Record the number of ships in the squadron, along with the
type of ships in the squadron. Record how many hits each ship contributes to that squadron's total
hits. Ship type determines how many hits each ship contributes. All of the ships in a squadron must
be the same type of ship. The types of ships available for use in a fleet are listed under
[Ships and Ship Statistics](ref/rule/ships-and-ship-statistics). The hits per ship for these ships
are listed below.

> 1 Hit per Ship: [Raft](ref/rule/ss-raft), [rowboat](ref/rule/ss-rowboat),
> [ship's boat](ref/rule/ss-ships-boat)\
> 2 Hits per Ship: [Keelboat](ref/rule/ss-keelboat)\
> 3 Hits per Ship: [Junk](ref/rule/ss-junk), [longship](ref/rule/ss-longship),
> [sailing ship](ref/rule/ss-sailing-ship)\
> 4 Hits per Ship: [Galley](ref/rule/ss-galley), [warship](ref/rule/ss-warship)

**Step 3 - Select Commodore:** List the name of the squadron's commodore, along with her Charisma
modifier and [Profession (sailor)](ref/skill/profession-any) skill modifier. An admiral can never
serve as a commodore. If a commodore is also a significant character (either a PC or a significant
named NPC), that squadron gains a +2 bonus on all attack rolls, damage rolls, and morale checks. (As
a general rule, most NPC fleets should have 2-4 significant named NPCs serving as commodores.)

**Step 4 - Determine Hits:** A squadron's hits equals the number of ships in the squadron multiplied
by the number of hits each ship contributes. For example, a squadron of five rafts would have only 5
hits (since a raft is only a 1-hit ship), whereas a squadron of five warships would have 20 hits
(since a warship is a 4-hit ship). This number is temporarily reduced by disabled ships and
permanently reduced by sunken ships.

**Step 5 - Determine Morale:** Morale for each squadron fluctuates during a battle. A newly
consigned squadron's starting morale score is equal to the party's
[Infamy score](ref/rule/infamy-and-disrepute-scores) divided by 10 (round down), with a minimum
morale score of 1 and a maximum score of 10. An NPC fleet's squadron has a starting morale score of
3 points. If a squadron's morale score is ever reduced to 0, the squadron mutinies and is lost - it
cannot be "repaired" in this case, and can only be replaced by a new squadron. A single squadron's
morale score can never be higher than 10.

**Step 6 - Determine Defense Value:** A squadron's Defense Value (DV) is equal to 10 + the
commodore's Profession (sailor) skill check modifier, further increased by some flagship boons.

**Step 7 - Determine Attack Value:** A squadron's Attack Value is equal to its commodore's
Profession (sailor) check. This value can be increased by flagship boons or the presence of a
significant commodore.

**Step 8 - Determine Damage:** A squadron deals 1d6 points of damage to a fleet on a successful
attack, plus an additional point of damage per ship in the squadron. This damage can be further
modified by flagship boons and the presence of significant commodores.

**Step 9 - Determine Morale Check:** A squadron's base morale check is equal to its commodore's
Charisma modifier, further modified by flagship boons and the presence of significant commodores.
Each time that squadron has a ship become disabled, add +1 to its loss count. Each time a squadron
has a ship sink, add +1 to its loss count. Each time an entire squadron is destroyed or mutinies,
add +1 to each surviving squadron's loss count. A squadron's total morale check is equal to its base
check minus its loss count.
