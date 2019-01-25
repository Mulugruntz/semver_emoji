# semver_emoji
Like semver, but with emojis!


# What does it do?
Instead of using numbers in [semver](https://semver.org/), let's use emojis!
Emojizing a semver is deterministic! You always get the same result from the same "classic" semver.

Each product has its own semver, though!

Version 4.8.15 from product A will have different emojis than 4.8.15 from  product B.

# Some examples!!
See the following:

* Product 1.0.0 : 👉🏼.🧔🏽.🈺
* Product 1.0.1 : 👉🏼.🧔🏽.🦒
* Product 1.0.2 : 👉🏼.🧔🏽.🐤
* Product 1.1.0 : 👉🏼.👍🏿.🍖
* Product 1.2.0 : 👉🏼.🧜🏼‍♂️.🌓
* Product 1.2.1 : 👉🏼.🧜🏼‍♂️.🚴‍♂️
* Product 2.0.0 : 🕒.👨🏻‍🎨.👮🏾‍♀️

# Please note

* It is easy to see if 2 semvers are related
* It becomes hard to order versions (Should 👉🏼 come before or after 🕒? Especially as it depends on the product)
* Depending on where you print the emojis, you may need to do some transformation.
* Some systems don't support some emojis (like the flags, or the skin colour, or the gender)

# Improvements

* PyPI package
* Provide a custom set of emojis to pick from (to constrain from the full set)
* Include/exclude families/versions/features of emojis
* Return other formats besides `str` (like `tuple` or the same as `semver` package)
* Return other types of output (like `":fountain_pen:"` for :fountain_pen:)
* Unit-tests
