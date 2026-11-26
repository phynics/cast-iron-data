+++
id = "ref/arc-wizard/spirit-whisperer"
kind = "archetype"
title = "Spirit Whisperer"
aon = "ArchetypeDisplay.aspx?FixedName=Wizard%20Spirit%20Whisperer"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spirit_whisperer", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]
[[sources]]
publication = "advanced-class-guide"
page = "133"

[fields]
kind = "archetype"
features = [
  { anchor = "arcane-bond" },
  { anchor = "spirit-link", level = 1 },
  { anchor = "spirit-hex", level = 5 },
]
trades = [
  { replaces = "Spellbooks class feature", feature = "spellbooks", by = ["arcane-bond"] },
  { replaces = "Arcane school", feature = "arcane-school", by = ["spirit-link"] },
  { replaces = "Bonus feat gained at 20th level", feature = "bonus-feats", levels = [20], by = ["spirit-link"] },
  { alters = "Arcane bond", feature = "arcane-bond", by = ["arcane-bond"] },
  { alters = "Bonus feats", feature = "bonus-feats", levels = [5, 10, 15], by = ["spirit-hex"] },
]
+++

Spirit whisperers are a breed apart among wizards, and are often mistaken for witches. While spirit
whisperers do gain and store their spells by communing with familiars, the spirits they gain
guidance from are somewhat closer to the world and more direct than the powers with which witches
typically traffic. These wizards treat such spirits as mentors and friends, conversing with them
rather than appeasing them in the effort to gain and use arcane knowledge.

## Arcane Bond (Ex) {#arcane-bond}

When a spirit whisperer chooses an arcane bond, he must choose the familiar arcane bond, and the
familiar gains the spirit animal ability of his selected spirit (see spirit link, below). The spirit
whisperer does not need a spellbook, but instead stores and prepares his spell by communing with the
familiar as the [witch's](ref/class/witch) familiar class feature (_Advanced Player's Guide_ 67).
This ability alters arcane bond and replaces the spellbooks class feature.

## Spirit Link (Su) {#spirit-link}

At 1st level, a spirit whisperer forms a mystical bond with a spirit. The spirit whisperer picks a
spirit from the [shaman's list of spirits](ref/ability/shaman-spirits) (see page 37). At 1st level,
he gains a spirit ability granted by that spirit. At 8th level, he gains the greater spirit ability
granted by that spirit. At 20th level, the spirit whisperer gains the manifestation ability granted
by the spirit. He uses his wizard level as his shaman level for determining the effects and DCs of
abilities granted by the spirit. In addition, he uses his Intelligence modifier in place of his
Wisdom modifier for these abilities. He does not gain hexes, spirit magic spells, or the true spirit
ability typically granted to a shaman by these spirits. This ability replaces arcane school and the
bonus feat gained at 20th level.

## Spirit Hex {#spirit-hex}

At 5th level, a spirit whisperer can select one hex from the list of those granted by his chosen
spirit. He uses his wizard level as his shaman level when determining the effects and DC of this
hex. In addition, he uses his Intelligence modifier in place of his Wisdom modifier for these hexes.
At 10th and 15th level, he can select another hex from those granted by his spirit. Each hex
selected in this way replaces the bonus feat gained at that level. This ability alters bonus feats.
