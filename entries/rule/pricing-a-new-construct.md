+++
id = "ref/rule/pricing-a-new-construct"
kind = "rule"
title = "Pricing a New Construct"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pricing_a_new_construct", path = "json/rules_adv_magic01.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "112"

[fields]
kind = "none"
+++

This section provides guidelines for those seeking to calculate the costs of crafting their own
constructs. As a rough guideline, a construct's price is equal to its challenge rating squared, then
multiplied by 500 gp. Constructs with a fractional CR rating base their price on that fraction of
500 gp. For example, a CR 1/2 construct has a price of 250 gp. The cost of magical supplies for the
[Craft Construct](ref/feat/craft-construct) feat is half this price, with the construct taking 1 day
to create per 1,000 gp of the construct's base price. Some constructs, particularly golems, have
additional raw material costs that must be paid in full, regardless of whether the creator possesses
the Craft Construct feat. Raw materials typically cost somewhere between 5% and 10% of the
construct's base price.

Constructs with multiple special abilities cost more to create. The first special ability is
included in the construct's base cost. The next two special abilities increase the calculated price
by +1/2 CR per ability. Thereafter, any additional special abilities add +1 CR per ability. Examples
of special abilities include having a higher DR value than a typical construct of its CR (above DR 5
for CRs 1-8, above DR 10 for CR 9+), monster statistics that exceed those recommended for the
[construct's CR](ref/rule/step-2-target-statistics), the standard golem immunity to magic, DR or
[hardness](ref/umr/hardness) that can't be overcome by all adamantine weapons, ability to be fully
healed by a single spell, and most special attacks and special qualities.

Particularly powerful special abilities, such as an [iron golem's](ref/monster/golem-iron-golem)
exceptionally high attack bonus, count as two lesser abilities. Animated objects are a special
case - their base price is not increased by any abilities paid for with Construction Points (see the
[Animated Object monster entry](ref/monster/animated-object)), since these abilities are already
factored into an animated object's CR. In addition, golems and homunculi created with extra Hit
Dice, the [advanced](ref/template/advanced) template, or
[shield guardian](ref/family/shield-guardian) abilities should all be priced as described in the
Bestiary, rather than by adjusting pricing for their new CR.

Abilities that weaken or potentially place a construct at a disadvantage rarely reduce the
construct's price. An exception is the **berserk** ability. Constructs that have a chance of going
berserk receive -1 CR adjustment to their calculated price if control can be reestablished (like a
[flesh golem](ref/monster/golem-flesh-golem)) or -2 CR adjustment for permanent loss of control
(like a [clay golem](ref/monster/golem-clay-golem)).

The following is an example of the calculated costs for creating a stone golem (CR 11). A stone
golem's special abilities are golem immunity to magic, full healing from
[transmute mud to rock](ref/spell/transmute-mud-to-rock), a high to-hit bonus (+22 vs. the +19
typical for CR 11), and the ability to slow its foes. Further, since its spell vulnerabilities are
not tied to common spells or effects, its immunity to magic cost is doubled, giving the stone golem
a total of 5 special abilities. The first special ability doesn't affect the cost, the next two
increase the cost by +1/2 CR each, and the final two each increase the cost by +1 CR individually,
making its effective CR for pricing equal to 14. This produces a calculated price of 98,000 gp,
rounded up to an even 100,000 gp.

When designing a new construct, keep in mind that the above pricing formula only serves as a
guideline. As with magic items, construct pricing remains more art than science, and like magic
items, compare new constructs to existing ones for guidance. If you're not sure, err on the side of
a higher price.
