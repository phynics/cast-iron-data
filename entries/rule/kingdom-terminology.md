+++
id = "ref/rule/kingdom-terminology"
kind = "rule"
title = "Kingdom Terminology"
source_ids = ["ultimate-campaign"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "kingdom_terminology", path = "json/rules_campaign_types04.json" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Campaign pg 198

Kingdoms have attributes that describe and define them. These are tracked on a kingdom sheet, like a
character's statistics are on a character sheet.

**Alignment:** Like a PC, your kingdom has an alignment, which you decide when you form the kingdom.
The kingdom's alignment represents the majority outlook and behavior of the people within that
kingdom when they're considered as a group. (Individual citizens and even some leaders may be of
different alignments.)

When you decide on your kingdom's alignment, apply the following adjustments to the kingdom's
statistics: Chaotic: +2 Loyalty; Evil: +2 Economy; Good: +2 Loyalty; Lawful: +2 Economy; Neutral:
Stability +2 (apply this twice if the kingdom's alignment is simply Neutral, not Chaotic Neutral or
Lawful Neutral).

A kingdom's alignment rarely changes, though at the GM's option, it can shift through the actions of
its rulers or its people.

**Build Points:** Build points (or BP for short) are the measure of your kingdom's resources -
equipment, labor, money, and so on. They're used to acquire new hexes and develop additional
buildings, settlements, and terrain improvements. Your kingdom also consumes BP to maintain itself.

**Consumption:** Consumption indicates how many BP are required to keep the kingdom functioning each
month. Your kingdom's Consumption is equal to its Size, modified by settlements and terrain
improvements (such as Farms and Fisheries). Consumption can never go below 0.

**Control DC:** Some kingdom actions require a check (1d20 + modifiers) to succeed - this is known
as a control check. The base DC for a control check is equal to 20 + the kingdom's Size in hexes +
the total number of districts in all your settlements + any other modifiers from special
circumstances or effects. Unless otherwise stated, the DC of a kingdom check is the Control DC.

**Economy:** This attribute measures the productivity of your kingdom's workers and the vibrancy of
its trade, both in terms of money and in terms of information, innovation, and technology. Your
kingdom's initial Economy is 0 plus your kingdom's alignment and leadership modifiers.

**Kingdom Check:** A kingdom has three attributes: Economy, Loyalty, and Stability. Your kingdom's
initial scores in each of these attributes is 0, plus modifiers for kingdom alignment, bonuses
provided by the leaders, and any other modifiers.

Many kingdom actions and events require you to attempt a kingdom check, either using your Economy,
Loyalty, or Stability attribute (1d20 + the appropriate attribute + other modifiers). You cannot
take 10 or take 20 on a kingdom check. Kingdom checks automatically fail on a natural 1 and
automatically succeed on a natural 20.

**Loyalty:** Loyalty refers to the sense of goodwill among your people, their ability to live
peaceably together even in times of crisis, and to fight for one another when needed. Your kingdom's
initial Loyalty is 0 plus your kingdom's alignment and any modifiers from your kingdom's leadership
role.

**Population:** Actual population numbers don't factor into your kingdom's statistics, but can be
fun to track anyway. The population of each settlement is described in
[Settlements and Districts](ref/rule/settlements-and-districts).

**Size:** This is how many hexes the kingdom claims. A new kingdom's Size is 1.

**Stability:** Stability refers to the physical and social well-being of the kingdom, from the
health and security of its citizenry to the vitality of its natural resources and its ability to
maximize their use. Your kingdom's initial Stability is 0 plus your kingdom's alignment and
leadership modifiers.

**Treasury:** The Treasury is the amount of BP your kingdom has saved and can spend on activities
(much in the same way that your character has gold and other valuables you can spend on gear). Your
Treasury can fall below 0 (meaning your kingdom's costs exceed its savings and it is operating in
debt), but this increases Unrest (see [Kingdom Upkeep Phase](ref/rule/kingdom-upkeep-phase)).

**Turn:** A kingdom turn spans 1 month of game time. You make your kingdom checks and other
decisions about running your kingdom at the end of each month.

**Unrest:** Your kingdom's Unrest indicates how rebellious your citizens are. Your kingdom's initial
Unrest is 0. Unrest can never fall below 0 (anything that would modify it to less than 0 is wasted).
Subtract your kingdom's Unrest from all Economy, Loyalty, and Stability checks.

If your kingdom's Unrest is 11 or higher, the kingdom begins to lose control of hexes it has
claimed.

If your kingdom's Unrest ever reaches 20, the kingdom falls into anarchy (see Kingdom Upkeep Phase).
