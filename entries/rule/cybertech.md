+++
id = "ref/rule/cybertech"
kind = "rule"
title = "Cybertech"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cybertech", path = "json/rules_campaign_types10.json" },
]
[[sources]]
publication = "technology-guide"
page = "35"

[fields]
kind = "none"
+++

Cybertech is a form of technology that must be surgically implanted into a host body before it
functions. Cybertech takes up a special set of slots that correspond to a creature's body. Most
cybertech is designed for a creature with a humanoid shape - installing cybertech in a
non-humanoid-shaped body is more difficult, but possible.

Each piece of cybertech has an implantation value that indicates how invasive the implant is. The
total combined implantation values of all cybertech implanted in a single creature can't exceed
either that creature's Constitution score or Intelligence score - a creature's Constitution sets the
physical limit of what its body can accept in the form of cybernetic implants, while the creature's
Intelligence sets the mental limit of what its brain can control. An implant whose implantation
value would cause the total to exceed either of these two scores does not function but still takes
up a body slot. In addition, as long as a character has cybernetic implants installed whose combined
implantation exceeds his Constitution or Intelligence, he takes a -4 penalty on all saving throws.

A creature with neither a Constitution score nor an Intelligence score cannot receive benefits from
cybertech, but a creature with only one of these scores can.

Installing a piece of cybertech takes a number of hours equal to the cybertech's implantation value
if the installation is done by hand - certain technological items can speed this installation time.
The target must be willing or helpless during the entire installation, at the end of which the
installer attempts a Heal check against the cybertech's Install DC - this specific value is listed
for each cybertech item. On a success, the target takes Constitution damage equal to the cybertech's
implantation value and the cybertech immediately activates. On a failed check, the target still
takes the Constitution damage but the installation fails; a new attempt to install the cybertech can
be made, although it's wise to wait for the Constitution damage to heal before trying again.

Cybertech can be extracted using the same procedure as implanting it, with a failed Heal check
indicating the attempt to extract the item failed. Fortunately, extraction is a simpler task than
installment, and Heal checks to remove cybertech gain a +10 bonus. Extracting a piece of cybertech
from a dead body requires no Heal check but takes a number of rounds equal to the cybertech's
implantation value. You can only install or extract a single piece of cybertech at a time.

An NPC generally charges an amount equal to 1/10 the total price of a piece of cybertech for the
service of installing the item.

Each piece of cybertech has a full description, including a set of abbreviated statistics at the
start. This information is organized as follows.

**Price:** This is the cost in gold pieces to buy the implant if it's available for sale. This value
does not include the cost to have the object surgically implanted. As with magic items, a piece of
cybertech can be sold by PCs for half this value.

**Slot:** This is the part of the body into which the cybertech must be implanted. A single slot can
only ever host a single piece of cybertech. Cybertech slots are separate from normal magic item
slots and do not count as being used for the purposes of worn magic items.

**Weight:** This is the weight of the cybertech in pounds. Once installed, the cybertech's weight
does not count against a creature's encumbrance or maximum load.

**Install:** This is the Heal check DC required to successfully implant or remove the cybertech from
a creature.

**Implantation:** A numerical value indicating how invasive the cybertech is. The higher the number,
the more invasive the cybertech. Implantation influences the time and difficulty of installing and
removing the cybertech.

**Description:** This section describes the cybertech's appearance and abilities.

**Construction:** Certain requirements must be met for a character to craft cybertech. These
requirements generally consist of having a feat and access to
[a manufacturing facility](ref/rule/crafting-high-tech-items).

**Craft:** This is the Craft DC required to create the cybertech. It is also the Knowledge
(engineering) DC to correctly identify the cybertech.

**Cost:** This is the cost in gold pieces to create the item. Generally this cost is equal to half
the price of the item
