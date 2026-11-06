+++
id = "ref/rule/steps-of-bargaining"
kind = "rule"
title = "The 5 Steps of Bargaining"
source_ids = ["ultimate-campaign"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "steps_of_bargaining", path = "json/rules_subsystems01.json" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Campaign pg 138

### Step 1: Seller Sets the Asking Price

The seller suggests a price to the buyer. If the **Asking Price** is more than 150% of the item's
actual value, the buyer simply refuses to bargain. The lowest amount the seller will accept is 75%
of this Asking Price.

### Step 2: Evaluate Item

The buyer chooses to attempt either an [Appraise](ref/skill/appraise) check to estimate the item's
value or a [Sense Motive](ref/skill/sense-motive) check opposed by the seller's
[Bluff](ref/skill/bluff) check (with failure meaning the buyer believes the seller is being fair).
If the seller's price is the same as the buyer's estimation of the item's value, no Sense Motive
check is needed and the buyer believes the seller.

A group of items can be sold as a unit. If the buyer is dealing with a mix of items she can appraise
and others she can only guess about, she uses either Appraise or Sense Motive, depending on which
she has more skill ranks in.

The GM can allow a PC to substitute an appropriate Knowledge skill for Appraise or Sense Motive,
such as [Knowledge (arcana)](ref/skill/knowledge-arcana) for selling a rare book about magic. He may
also assign modifiers to skill checks to reflect expertise or ignorance about a specific type of
item, good roleplaying, or insulting behavior toward an NPC buyer or seller.

### Step 3: Determine Undercut

The **Undercut Percentage** is a portion of the item's price or value used to determine the buyer's
Initial and Final Offers.

To determine the _Undercut Percentage,_ have the buyer attempt a Bluff check opposed by the seller's
Sense Motive check. The _Undercut Percentage_ is 2%, plus 1% for every point by which the Bluff
check exceeds the Sense Motive check (minimum 0%).

### Step 4: Set Offers

The **Initial Offer** is the buyer's first counteroffer to the seller's _Asking Price._

The **Final Offer** is the largest amount the buyer is willing to pay. Though the seller and buyer
negotiate back and forth, the buyer won't exceed this offer. For example, if the seller's _Asking
Price_ is 1,000 gp, the buyer's _Initial Offer_ may be 800 gp and the _Final Offer_ 900 gp. These
offers are determined by how much the buyer thinks the item is worth compared to the seller's
_Asking Price._

> **Fair (Appraise or Sense Motive):** If the seller's _Asking Price_ is less than or equal to the
> amount that the buyer thinks the item is worth, subtract the _Undercut Percentage_ from the
> seller's price to get the _Final Offer,_ and subtract 2 × the _Undercut Percentage_ to get the
> _Initial Offer._

> **Unfair (Appraise):** If the result of the buyer's Appraise check leads her to believe the item
> is worth less than the seller's _Asking Price,_ subtract the _Undercut Percentage_ from the
> buyer's estimate of the item's value to get the _Final Offer,_ and subtract 2 × the _Undercut
> Percentage_ to get the _Initial Offer._

> **Unfair (Sense Motive):** If the result of the buyer's Appraise check leads her to believe the
> seller's _Asking Price_ is too high, subtract 2 × the _Undercut Percentage_ from the seller's
> _Asking Price_ to get the _Final Offer,_ and subtract 4 × the _Undercut Percentage_ to get the
> _Initial Offer._

### Step 5: Bargain

The buyer begins bargaining by countering the seller's price with her _Initial Offer._ This step
repeats until the buyer and seller agree on a price or one side ends negotiations.

> **Counteroffer Is Less Than Final Offer:** If the seller counters with a price that is less than
> the buyer's _Final Offer,_ have the seller attempt a [Diplomacy](ref/skill/diplomacy) check (DC
> 15 + the buyer's Charisma modifier). Success means the buyer accepts the seller's counteroffer and
> buys the item. Failure means the buyer holds at her _Initial Offer._ The seller can try again, but
> the Diplomacy check DC increases by 5 unless the seller lowers his price.
>
> **Counteroffer Equals Final Offer:** If the seller counters with a price that is the same as the
> buyer's _Final Offer,_ have the seller attempt a Diplomacy check (20 + the buyer's Charisma
> modifier). Success means the buyer accepts the seller's counteroffer and buys the item. Failure
> means the buyer counteroffers at a price between the _Initial Offer_ and the _Final Offer._ The
> seller can try again, but the Diplomacy DC increases by 5 unless the seller lowers his price.
>
> **Counteroffer Exceeds Final Offer:** If the seller counters with a price higher than the buyer's
> _Final Offer,_ have the seller attempt a Diplomacy check (25 + the buyer's Charisma modifier).
> Success means the buyer counteroffers at a price between the _Initial Offer_ and the _Final
> Offer._ Failure means the buyer holds at her _Initial Offer._ Failure by 5 or more means the buyer
> is insulted and lowers her offer or refuses to deal with the seller. The seller can try again, but
> the Diplomacy DC increases by 5 unless the seller lowers his price.
