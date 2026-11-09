+++
id = "ref/rule/effect-word-descriptions"
kind = "rule"
title = "Effect Word Descriptions"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "effect_word_descriptions", path = "json/rules_opt_magic03.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "167"

[fields]
kind = "none"
+++

Effect words determine the overall outcome of a wordspell. A wordspell can contain more than one
effect word, and it is possible for their effects to counteract one another. Effect words use the
following format.

**Name:** This is the name of the effect word. Each word belongs to a group of similar words, noted
in parentheses. Unless otherwise noted, an individual wordspell cannot contain two effect words from
the same group.

**School:** This entry lists the school of magic that the effect word belongs to.

**Level:** This entry lists the classes that can learn the effect word and what level the word is
for members of that class. Note that an individual wordspell can contain no words of a level higher
than the wordspell.

**Duration:** This line lists the duration of the effect word.

**Saving Throw:** If the effect allows a saving throw, it is noted here along with the effect of a
successful save.

**Spell Resistance:** If the effect word allows [spell resistance](ref/rule/spell-resistance), it is
noted here.

**Target Restrictions:** Some effect words can only be combined with specific target words when
arranging wordspells. If this is the case, the specific target words are noted here.

**Description:** This paragraph describes the effects of the word when arranged in a wordspell.

**Boost:** If the effect word can be boosted by the boost meta word, the effects are listed here.
See the meta word section for more details.
