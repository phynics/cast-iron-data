+++
id = "ref/arc-investigator/majordomo"
kind = "archetype"
title = "Majordomo"
aon = "ArchetypeDisplay.aspx?FixedName=Investigator%20Majordomo"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "majordomo", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "35"

[fields]
kind = "archetype"
features = [
  { anchor = "paper-trail", level = 1 },
  { anchor = "delegate" },
  { anchor = "inspired-manager", level = 3 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["paper-trail"] },
  { replaces = "All instances of trap sense", feature = "trap-sense", by = ["inspired-manager"] },
  { replaces = "Alchemy", feature = "alchemy", by = ["delegate"] },
  { replaces = "swift alchemy", feature = "swift-alchemy", by = ["delegate"] },
]
+++

A majordomo is a skilled individual able to keep the complex operations of a noble's holdings
running on a day-to-day basis. In a world of intrigue where the loyalties of staff can be bought and
sold, sometimes it takes the skills of an investigator to follow the byzantine paper trails and
prevent embezzling and espionage within the estates of the elite.

## Paper Trail (Ex) {#paper-trail}

A majordomo is trained to uncover forgeries and trace down discrepancies in paperwork in order to
ferret out intrigue. She adds half her investigator level (minimum 1) to Linguistics and Profession
checks to spot a forgery, deal with paperwork, and notice discrepancies in paperwork.

A majordomo who analyzes the handwriting of a document and succeeds at a Linguistics check against a
DC equal to 20 + the writer's Bluff bonus gets a hunch about whether the document's writer was lying
or otherwise nervous. This ability doesn't work if the document was dictated to someone who thought
the contents were legitimate.

This ability replaces trapfinding.

## Delegate (Ex) {#delegate}

In order to perform all the necessary tasks of her household, a majordomo quickly learns how to
delegate. At 1st level and every 3 investigator levels thereafter, a majordomo gains a bonus
teamwork feat. As a standard action, she can grant all allies within 30 feet who can see or hear her
one of these teamwork feats (even if they don't meet the prerequisites) for a number of rounds equal
to 3 + her investigator level. She can use this ability once per day at 1st level, plus an
additional time at 4th level and every 3 levels thereafter.

At 4th level, a majordomo can use her delegate ability and designate a single noncombat task that
could make use of the teamwork feat (for instance, designating the
[Cooperative Crafting](ref/feat/cooperative-crafting) feat and a session of crafting). As long as
the allies pursue the task uninterrupted, instead of experiencing the benefits for a number of
rounds equal to 3 + the majordomo's investigator level, her allies retain the benefits until the
task is complete, to a maximum of 8 hours. Additionally, the majordomo can use her delegate ability
as a move action instead of a standard action.

At 7th level, a majordomo can use her delegate ability to grant two teamwork feats to her allies,
instead of one feat. At 10th level, she can also use her delegate ability as a swift action. At 13th
level, she can grant up to three teamwork feats to her allies when she uses delegate.

At 16th level, she can spend 1 minute and use her delegate ability to grant a single teamwork feat
to all of her allies until the next time she recovers uses of her delegate ability. As usual for
multiple uses of the same ability, if she later uses delegate to grant three teamwork feats, the two
uses don't stack to grant four bonus teamwork feats, but the longer-duration teamwork feat returns
after the three shorter-duration feats expire.

This ability replaces the alchemy and swift alchemy abilities. Additionally, a majordomo can't take
the [alchemist discovery](ref/invtalent/alchemist-discovery) investigator talent or any discovery
that affects or involves alchemy.

## Inspired Manager (Ex) {#inspired-manager}

At 3rd level, a majordomo knows how to make just about any work task more efficient, from cleaning a
great hall after a big party to crafting a magic item.

Whenever an ally begins a workday task such as Craft, Profession, magic item creation,
[spell research](ref/rule/adding-spells-to-a-wizards-spellbook), managing a kingdom, using the
[downtime](ref/rule/downtime) rules, or other similar tasks, the majordomo can spend one use of
inspiration and 1 minute of planning to create a plan for that ally. If the ally chooses to follow
the majordomo's plan and attempts the task on the same day, if the task would normally take at least
4 hours, it instead takes 30 minutes less time, and if the task would normally take at least 8
hours, it instead takes 1 hour less time.

If using the [kingdom-building rules](ref/rule/kingdom-building) from _Pathfinder RPG Ultimate
Campaign_, at 3rd level, the majordomo counts her Intelligence score as 2 higher when determining
the bonus she provides in a kingdom leadership role.

Her effective Intelligence score increases by an additional 2 at 6th level and every 3 investigator
levels thereafter.

This ability replaces all instances of trap sense.
