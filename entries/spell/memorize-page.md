+++
id = "ref/spell/memorize-page"
kind = "spell"
title = "Memorize Page"
aon = "SpellDisplay.aspx?ItemName=Memorize%20Page"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "memorize_page", path = "json/spells14.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "187"

[fields]
kind = "spell"
school = "enchantment"
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "10 minutes"
components = "V, S, F (the page to be memorized)"
range = "touch"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Arcanist, Bard, Mesmerist, Occultist, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, S, F (the page to be memorized)
Range: touch
Duration: instantaneous
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one living creature
Descriptors: mind-affecting
:::

The target gains a perfect memory of the page you used as a focus component. The target can
visualize this page as easily as looking at it in person, including minute details visible to close
scrutiny by the naked eye. The memory of the page includes text and images, such as a drawing or a
map. Someone unfamiliar with the language on the page (or even an illiterate person) could relay
what is written simply by copying the shapes of the letters so another person can read them.

The maximum number of pages that a particular target can memorize through repeated castings of this
spell is equal to the target's Intelligence modifier (minimum 1); any attempts beyond this limit
have no effect, although the target's memory of a page could be erased (using
[modify memory](ref/spell/modify-memory) or a similar effect) to effectively make room for a
different one.

A creature that memorizes magical writing (such as a scroll or a page from a spellbook) cannot
borrow, duplicate, or retain any of the magic in the writing. However, this would allow a wizard to
copy a spell into his spellbook so he could prepare the spell from his book (assuming the spell
takes up only one page in a spellbook).
